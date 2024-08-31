import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import csv
import threading

class BooksToScrapeWebScraper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Books to Scrape Web Scraper")
        self.geometry("900x600")
        self.configure(bg="#f0f0f0")

        self.input_frame = tk.Frame(self, bg="#f0f0f0")
        self.input_frame.pack(side=tk.TOP, fill=tk.X, pady=15)

        self.text_frame = tk.Frame(self)
        self.text_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.button_frame = tk.Frame(self, bg="#f0f0f0")
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

        self.search_label = tk.Label(self.input_frame, text="Enter Book Title:", font=("Arial", 12), bg="#f0f0f0", fg="#333333")
        self.search_label.pack(side=tk.LEFT, padx=10)
        self.search_field = tk.Entry(self.input_frame, width=50, font=("Arial", 12))
        self.search_field.pack(side=tk.LEFT, padx=10)

        self.scrape_button = tk.Button(self.button_frame, text="Scrape Website", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.scrape_website)
        self.scrape_button.pack(side=tk.LEFT, padx=10)
        self.exit_button = tk.Button(self.button_frame, text="Exit", bg="#f44336", fg="white", font=("Arial", 10, "bold"), command=self.on_exit)
        self.exit_button.pack(side=tk.LEFT, padx=10)

        self.text_area = tk.Text(self.text_frame, wrap=tk.WORD, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.text_area.configure(state=tk.DISABLED)
        self.scrollbar = tk.Scrollbar(self.text_frame, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=880, mode="determinate", style="TProgressbar")
        self.progress_bar.pack(side=tk.BOTTOM, pady=10)

        style = ttk.Style()
        style.configure("TProgressbar", thickness=20)

    def on_exit(self):
        if messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
            self.destroy()

    def scrape_website(self):
        search_term = self.search_field.get().strip()
        if not search_term:
            messagebox.showerror("Input Error", "Please enter a book title.")
            return

        self.text_area.configure(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.progress_bar["value"] = 0
        self.scrape_button["state"] = tk.DISABLED

        thread = threading.Thread(target=self.start_scraping, args=(search_term,))
        thread.start()

    def start_scraping(self, search_term):
        try:
            with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Title", "Price", "Rating", "Product Information"])

                for current_page in range(1, 6):
                    url = f"http://books.toscrape.com/catalogue/page-{current_page}.html"
                    self.update_text_area(f"Accessing URL: {url}\n")

                    response = requests.get(url)
                    response.raise_for_status()

                    soup = BeautifulSoup(response.text, "html.parser")
                    products = soup.select("article.product_pod")
                    found_book = False

                    for product in products:
                        title = product.select_one("h3 a")["title"]

                        if search_term.lower() in title.lower():
                            found_book = True
                            price = product.select_one("p.price_color").text
                            rating = product.select_one("p.star-rating")["class"][1]
                            product_info_url = product.select_one("h3 a")["href"]

                            full_product_info_url = f"http://books.toscrape.com/catalogue/{product_info_url}"
                            product_info_response = requests.get(full_product_info_url)
                            product_info_response.raise_for_status()

                            product_info_soup = BeautifulSoup(product_info_response.text, "html.parser")
                            product_info = product_info_soup.select_one("meta[name=description]")["content"].strip()

                            output = f"Title: {title}\nPrice: {price}\nRating: {rating}\nProduct Info: {product_info}\n\n"
                            self.update_text_area(output)

                            writer.writerow([title, price, rating, product_info])

                    self.progress_bar["value"] = (current_page * 100) / 5
                    self.update_idletasks()

                    if not found_book:
                        self.update_text_area(f"No books found on page {current_page} matching the title: {search_term}\n")

            self.update_text_area("Data successfully written to books.csv\n")
        except Exception as e:
            self.update_text_area(f"Error: {e}\n")
        finally:
            self.scrape_button["state"] = tk.NORMAL
            messagebox.showinfo("Success", "Scraping complete!")

    def update_text_area(self, message):
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.insert(tk.END, message)
        self.text_area.configure(state=tk.DISABLED)

if __name__ == "__main__":
    app = BooksToScrapeWebScraper()
    app.mainloop()
