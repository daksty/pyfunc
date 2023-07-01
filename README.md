# pyfunc
Simple command line tools

# pyfunc

pyfunc is a Python command-line tool that provides various functionalities and utilities for different tasks. It is designed to be versatile and easy to use. This README file provides information on how to use pyfunc and outlines its features.

## Installation

1. Clone the pyfunc repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

pyfunc can be used by running the `pyfunc.py` script with Python. Here are some examples of how to use pyfunc:

1. Generating a fake identity:
   ```
   python pyfunc.py fake_identity
   ```
   This command will generate a fake name, email, address, phone number, and image URL.

2. Finding links on a website:
   ```
   python pyfunc.py website_link
   ```
   This command will prompt you to enter a website URL and then display all available links on that website.

3. Extracting a ZIP file:
   ```
   python pyfunc.py zip_file
   ```
   This command will prompt you to enter the path to a ZIP file and attempt to extract it. If the ZIP file is password-protected, it will ask for the passwords file path.

4. Retrieving the device temperature:
   ```
   python pyfunc.py temperature
   ```
   This command will display the current temperature of the device.

5. Printing the content of a file:
   ```
   python pyfunc.py print_file
   ```
   This command will prompt you to enter the path to a file and display its content.

These are just a few examples of the functionalities provided by pyfunc. For a complete list of available commands, you can run `python pyfunc.py --help`.

## Features

- **Fake Identity Generation:** Generate fake names, emails, addresses, phone numbers, and image URLs.
- **Website Link Extraction:** Extract all available links from a given website URL.
- **ZIP File Extraction:** Extract ZIP files and attempt to find the password from a passwords.txt file.
- **Device Temperature:** Retrieve the temperature of the device (supported on Windows, Linux, and Android).
- **File Content Printing:** Print the content of a file.
- **IP Location Lookup:** Get the location information for a given IP address.
- **URL Shortening:** Shorten long URLs using the TinyURL API.
- **File/Directories Operations:** Create new files or directories, rename existing files, and copy files.

Feel free to explore the tool and utilize its functionalities for your various tasks.

## Contributors

- Creator: @daksty
- GitHub: [https://www.github.com/daksty](https://www.github.com/daksty)
- Discord: ravenishandsome#4807

## License

This project is licensed under the [MIT License](LICENSE).

Please note that this tool is provided as-is without any warranty. Use it at your own risk.
