#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the required modules
from bs4 import BeautifulSoup as bs
import requests
import os
import yaml

# Function to read & return the config file content
def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            yaml_content = yaml.safe_load(file)
            return yaml_content
        except yaml.YAMLError as e:
            print(f"Error while reading YAML file : {e}")
            return None

# Define a class to scrape links and their content from a given URL
class ScrapLinks:
    # Initialize the class with necessary attributes
    def __init__(self, url, file, cookies, links, inte):
        self.url = url
        self.file = file
        self.cookies = cookies
        self.links = links
        self.inte = inte

    # Make a request to the URL and parse the HTML content
    def get(self):
        r = requests.get(self.url, cookies=self.cookies)
        soup = bs(r.content, 'html.parser')
        return soup

    # Get the title of the web page
    def get_title(self):
        title = self.get().title.get_text().strip()
        return title

    # Create a folder with the title of the web page
    # def make_folder(self):
    #     title = self.get_title()
    #     os.mkdir(title)
    #     return title
    def make_folder(self):
        title = self.get_title()

        # Créer le dossier 'results' s'il n'existe pas
        results_path = 'results'
        if not os.path.exists(results_path):
            os.mkdir(results_path)

        # Créer le dossier parent (le nom du module) dans le dossier 'results'
        title_path = os.path.join(results_path, title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)

        return title_path

    # Get a list of links from the web page and save them to a file
    def get_list(self):
        data = self.get().find('div', {'id': 'TOC'}).find_all('a')
        links = [link.get('href') for link in data]
        with open(self.file, 'w') as f:
            for link in links:
                f.write(link + '\n')
        return links


    # Get the content of each link and save it in a separate file
    def get_content(self):
        title = self.get().find(
            'div', {'class': 'training-module'}).find('h1').text.strip()
        data = self.get().find('div', {'class': 'training-module'})
        final = data.decode_contents()

        curr_path = os.getcwd()
        main_dir = os.path.basename(curr_path)
        link_title = title.replace('/', '-')
        new_dir = os.path.join(curr_path, f"{main_dir} - {link_title}")

        os.makedirs(new_dir, exist_ok=True)

        with open(os.path.join(new_dir, f'{self.inte}_{link_title}.md'), 'w', encoding='utf-8') as f:
            f.write(final)

        return title, final

# Define the main function to execute the script
def main():
    yaml_file = "config/config.yaml"
    config = read_yaml_file(yaml_file)

    if not config:
        print("Error while reading the configuration file.")
        print("Make sure that file 'config.yaml' is present in the config file or you renamed : 'config.example.yaml' to 'config.yaml'")
        return

    url = config['url']
    file = config['file']
    cookies = config['cookies']

    links = []
    inte = 1

    scraper = ScrapLinks(url, file, cookies, links, inte)

    # Change the working directory to the title folder or create one if it doesn't exist
    if os.path.exists(scraper.get_title()):
        os.chdir('results')
        os.chdir(scraper.get_title())
    else:
        scraper.make_folder()
        os.chdir('results')
        os.chdir(scraper.get_title())

    # Get the list of links and save them to a file
    links = scraper.get_list()
    
    # Scrape the content of each link and save it to a separate file
    for link in links:
        print(f"[+] Getting content of {link}")
        ScrapLinks(link, file, cookies, links, inte).get_content()
        inte += 1

    # Remove the file containing the list of links
    os.remove(file)

    print("[+] Done")


# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()
