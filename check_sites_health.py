import re
import argparse
from datetime import timedelta, datetime

import whois
import requests


def parse() -> bytes:
    parser = argparse.ArgumentParser(
        description='''Simple site monitoring script.
        Check http status code (200 is OK) and expiration date
        (no least than 30 days)''')
    parser.add_argument('target',
                        type=str,
                        help="path to the url list (txt)")
    args = parser.parse_args()
    return args.target


def adapt_urls(urls):
    http = re.compile(r"^(http|https)://")
    transform = lambda url: "http://{}".format(url)
    return [url if http.match(url) else transform(url) for url in urls]


def load_urls4check(path):
    with open(path, 'r') as opened_file:
        return [url.strip() for url in opened_file]


def is_server_respond_with_200(url):
    try:
        http_ok = 200
        return requests.get(url).status_code == http_ok
    except requests.exceptions.ConnectionError:
        return "Failed to establish a new connection: unknown url!!!"


def get_domain_expiration_date(url):
    try:
        domain = whois.whois(url)
        date_delta = timedelta(days=30)
        domain_date = domain.expiration_date
        return (domain_date - date_delta) > datetime.now()
    except TypeError:
        return "Failed to determine expiration date. Unknown url!!!"


def main():
    url_list = parse()
    raw_urls = load_urls4check(url_list)
    urls = adapt_urls(raw_urls)
    for url in urls:
        status_code = is_server_respond_with_200(url)
        expr_date = get_domain_expiration_date(url)
        print("Domain: {}".format(url))
        print("HTTP (Code 200): {}".format(status_code))
        print("Expiration date (at least 30 days): {}".format(expr_date))
        print('==========================================================')


if __name__ == '__main__':
    main()
