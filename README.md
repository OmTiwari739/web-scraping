# Web Scraper

This project, **Web Scraper**, is a Python-based application developed during my internship at Prodigy InfoTech. The application is designed to scrape and extract book data from the "Books to Scrape" website, providing a user-friendly and efficient way to gather information about books.

## Features

- **Dynamic Search Functionality**: Allows users to enter a book title to search and retrieves relevant data from the website.
- **Multithreaded Scraping**: Ensures smooth operation and keeps the GUI responsive during the data extraction process.
- **Real-time Progress Display**: A progress bar updates in real time, providing feedback on the scraping progress.
- **Error Handling**: Manages network errors and invalid inputs, ensuring a stable and user-friendly application.
- **CSV Export**: Automatically saves the extracted data (Title, Price, Rating, and Product Information) into a CSV file for easy access and analysis.
- **User-Friendly Interface**: Built with Tkinter, featuring an intuitive and visually appealing GUI.

## Technology Stack

- **Python**: Core language for the application.
- **Tkinter**: Used for creating the graphical user interface (GUI).
- **Requests and BeautifulSoup**: Libraries for web scraping to extract data from HTML pages.
- **CSV Module**: For exporting the scraped data to a CSV file.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

You also need to install the required Python libraries:

```bash
pip install requests
pip install beautifulsoup4
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/OmTiwari739/Web-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Web-Scraper
   ```

3. Run the application:

   ```bash
   python web_scraper.py
   ```

## Usage

1. **Enter the book title**: Start by entering the title of the book you're looking for in the search field.
2. **Click "Scrape Website"**: The application will begin searching through the "Books to Scrape" website for books matching the entered title.
3. **View results**: Results are displayed in the application and saved to a CSV file for further use.

## Screenshots

![image](https://github.com/user-attachments/assets/f63527ca-62e3-4656-aff3-76b69c22419d)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to contact me via GitHub: [OmTiwari739](https://github.com/OmTiwari739)
