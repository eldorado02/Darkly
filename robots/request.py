#!/usr/bin/env python3

import requests
import sys
import io
import urllib.parse as parse


def parse_line_of_href(line: str, n) -> str:
    """Clean up all href and quote"""
    first_comma = line.find('"', n)
    second_comma = line.find('"', first_comma + 1)
    return (line[first_comma + 1:second_comma])

def filter_all_url(response: str) -> list[str]:
    """Filter only important href not all href like ../ or we will be found
    in infinite recurisivity"""
    stream = io.StringIO(response)
    all_href = list()
    for line in stream:
        n = line.find("href")
        if n != -1:
            href_clean = parse_line_of_href(line, n)
            if (href_clean != "../"):
                all_href.append(href_clean)
    return (all_href)


def get_flag(base_url) -> str:
    """Get flag recursively until found in README in all href"""
    r = requests.get(base_url)
    all_href = filter_all_url(r.text)
    for href in all_href:
        if href == "README":
            resp = requests.get(f"{base_url}{href}")
            if resp.text.find("your flag") != -1:
                print(resp.text, end="")
                print(base_url)
                sys.exit(0)
            return (resp.text)
        else:
            get_flag(f"{base_url}{href}")
    return ""

def main():
    """Main Function"""
    assert len(sys.argv) > 1, "Parametere must be address or url"
    
    address = sys.argv[1]
    all_href = get_flag(f"http://{address}:80/.hidden/")

if __name__ == "__main__":
    main()
    
