import re
import sys
import time
import playwright
from playwright.sync_api import sync_playwright
import argparse
import os

def validate_path(file_path):
    """ Validate if a given path exists and is accessible. """
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r"):
                    pass
            except Exception as e:
                raise ValueError(f"Error reading '{file_path}': {e}")
            return file_path
        else:
            raise ValueError(f"Error opening '{file_path}': Path is not a file")
    else:
        raise ValueError(f"Error opening '{file_path}': Path doesn't exists")

def get_url_ctn(url: str):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state("networkidle")
            time.sleep(2)
        except playwright.sync_api.Error:
            sys.exit("Connection error: check your network and retry")

        content = page.locator("body").inner_text()
        browser.close()

        content = content.splitlines()
        content = " ".join(content)

        return content.strip()

def extract_emails(content: str) -> list[str]:
    emails = re.findall(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', content)

    return emails

def main():
    parser = argparse.ArgumentParser(
        description="Collection of emails in text file or website page."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", dest="website_url", type=str,
                        help="Website url to read and extract emails")
    group.add_argument("--file", dest="path_to_file", type=str,
                       help="Path to file to read and extract emails")

    args = parser.parse_args()

    if args.website_url:
        content = get_url_ctn(args.website_url)
    else:
        path_to_file = validate_path(args.path_to_file)
        with open(path_to_file, "r") as file:
            content = file.read()

    emails = extract_emails(content=content)
    if emails:
        for index_, email in enumerate(emails, start=1):
            print(f"{index_}) {email}")

    else:
        print("No email address found!")

if __name__ == '__main__':
    main()