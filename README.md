[![PyPI Downloads](https://static.pepy.tech/badge/mailgrab)](https://pepy.tech/projects/mailgrab)
![PyPI](https://img.shields.io/pypi/v/mailgrab?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/nanaelie/mailgrab?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/nanaelie/mailgrab?style=flat-square)
![License](https://img.shields.io/github/license/nanaelie/mailgrab?style=flat-square)
![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square)

# mailgrab

**mailgrab** is a Python tool designed to extract email addresses from web pages or text files. It uses regular expressions for email extraction and Playwright for web scraping. This tool is perfect for collecting email addresses from multiple sources.

## Features

- Extracts email addresses from a URL or text file
- Uses **Playwright** for headless web scraping
- Searches with **regular expressions**
- Simple **command-line interface (CLI)**
- Can be used as a **Python module**

## Installation

Install `mailgrab` from [PyPI](https://pypi.org/project/mailgrab/):

```bash
pip install mailgrab
````

> ⚠️ Make sure to install [Playwright](https://playwright.dev/python/docs/intro) browsers:

```bash
python -m playwright install
```

## Usage

### CLI (Command Line)

```sh
$ mailgrab --help                            
usage: mailgrab [-h] (--url WEBSITE_URL | --file PATH_TO_FILE) [-v]

Collection of emails in text file or website page.

options:
  -h, --help           show this help message and exit
  --url WEBSITE_URL    Website url to read and extract emails
  --file PATH_TO_FILE  Path to file to read and extract emails
  -v, --version        show program's version number and exit
```

#### Examples

```bash
mailgrab --url "https://example.com"        # Extract emails from https://example.com
mailgrab --file "file.txt"                  # Extract emails from file.txt
mailgrab -v                                 # Show program's version
```

### As a Python module

```python
import mailgrab as mgb  # or from mailgrab import *

# Validate the path to a file containing emails
path = mgb.validate_path("file.txt")

# Read file content
with open(path, "r") as f:
    content = f.read()

# Extract emails from content
emails = mgb.extract_emails(content)

# Display emails using the built-in printer
mgb.print_emails(emails)
```

## CLI Example Output

```bash
[¤] Found 3 unique email address(es):

 1) contact@example.com
 2) info@example.org
 3) support@sample.net
```

## Path validation

When using the `--file` option or `validate_path()` function, mailgrab ensures:

* the path exists,
* it is a valid file,
* it can be opened for reading.

If not, a `MailgrabError` with a clear message is raised.

## Contributing

Want to improve this project? Awesome!
Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

