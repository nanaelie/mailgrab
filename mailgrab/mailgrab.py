import re
import sys
import time
import playwright
from playwright.sync_api import sync_playwright
import argparse
import os

from mailgrab.__version__ import __version__
from mailgrab.exceptions import MailgrabError


def validate_path(file_path):
    """ Validate if a given path exists and is accessible. """
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r"):
                    pass
            except Exception as e:
                raise MailgrabError(f"Error reading '{file_path}': {e}")
            return file_path
        else:
            raise MailgrabError(f"Error opening '{file_path}': Path is not a file")
    else:
        raise MailgrabError(f"Error opening '{file_path}': Path doesn't exists")

def get_url_ctn(url: str):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state("networkidle")
            time.sleep(1)
        except playwright.sync_api.Error as e:
            print("Error: ", e)
            sys.exit(1)

        content = page.locator("body").inner_text()
        browser.close()

        content = content.splitlines()
        content = " ".join(content)

        return content.strip()

def print_emails(emails):
    """Display a formatted, sorted list of unique emails."""
    unique_emails = sorted(set(emails))
    if not unique_emails:
        print("No email addresses found.")
        return

    print(f"\n[¤] Found {len(unique_emails)} unique email address(es):\n")
    for i, email in enumerate(unique_emails, 1):
        print(f"{i:>2}) {email}")

def extract_emails(content: str) -> list[str]:
    emails = re.findall(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', content)

    return emails

def main():
    parser = argparse.ArgumentParser(
        description="Collection of emails in text file or website page.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", dest="website_url", type=str,
                        help="Website url to read and extract emails")
    group.add_argument("--file", dest="path_to_file", type=str,
                       help="Path to file to read and extract emails")
    
    parser.add_argument("-v", "--version", action="version", version=f"mailgrab {__version__}")
    
    args = parser.parse_args()
    
    if args.website_url is not None:
        if not args.website_url.strip():
            print("Erreur : l'URL ne peut pas être vide.")
            sys.exit(1)
            
        content = get_url_ctn(args.website_url.strip())
            
    elif args.path_to_file is not None:
        if not args.path_to_file.strip():
            print("Erreur : le chemin du fichier ne peut pas être vide.")
            sys.exit(1)
            
        try:
            path_to_file = validate_path(args.path_to_file)
        except MailgrabError as e:
            print(e)
            sys.exit(1)
        
        with open(path_to_file, "r") as file:
            content = file.read()

    emails = extract_emails(content=content)
    print_emails(emails)

if __name__ == '__main__':
    main()
