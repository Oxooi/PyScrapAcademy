# PyScrapAcademy

This script can be used to scrape a webpage, extract the contents into multiple markdown files and store them in a newly created folder. The script is written in Python3 and requires the following modules:

## Dependencies

This web scraper relies on the following Python libraries:

- [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/): A library for pulling data out of HTML and XML files, making it easy to navigate and search the parse tree.
- [Requests](https://pypi.org/project/requests/): A library for making HTTP requests in Python, providing a simple and convenient way to interact with web services.
- [PyYAML](https://pypi.org/project/PyYAML/): A YAML parser and emitter for Python, allowing you to easily read and write YAML files.

## Features

- Scrape links from a web page
- Save the list of links to a text file
- Extract content from each link
- Save the content of each link in a separate Markdown file
- Organize the scraped content into folders

## Installation

1. Clone the repository:

> `git clone https://github.com/Oxooi/HTBAcademy_Scraping.git`

2. Change the directory to the project folder:

> `cd HTBAcademy_Scraping`

3. Install the required dependencies:

> `pip install -r requirements.txt`

## Configuration

1. Rename the `config.example.yaml` file to `config.yaml` in the `config` folder.
2. Open the `config.yaml` file and set the following parameters:

- `url`: The URL of the web page you want to scrape
- `file`: The name of the text file where the list of links will be saved
- `cookies`: The cookies to use for requests (htb_academy_session)

## Usage

Run the script with the following command:

> `python bot.py`

The script will create a `results` folder containing the scraped content organized in subfolders.
