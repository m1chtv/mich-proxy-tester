import requests
import time
from telethon import TelegramClient, functions
import re

TELEGRAM_API_ID = '27298269'
TELEGRAM_API_HASH = 'fb47bcb81d6d671b075455b668dd7a8c'
OUTPUT_FILE = 'proxy.txt'
PROXY_FILE = 'mich.txt'

def parse_proxy(proxy_link):
    pattern = re.compile(r'tg://proxy\?server=([^&]*)&port=([^&]*)&secret=([^&]*)')
    match = pattern.match(proxy_link)
    if match:
        return {
            'server': match.group(1),
            'port': match.group(2),
            'secret': match.group(3)
        }
    return None

def get_proxies_from_file(proxy_file):
    with open(proxy_file, 'r') as file:
        proxy_links = file.readlines()
    return [link.strip() for link in proxy_links if link.strip()]

def test_mtproto_proxy(proxy_info):
    client = TelegramClient('proxy_test', TELEGRAM_API_ID, TELEGRAM_API_HASH,
                            proxy=("mtproxy", proxy_info['server'], int(proxy_info['port']), proxy_info['secret']))

    start_time = time.time()
    try:
        client.connect()
        result = client(functions.help.GetNearestDcRequest())
        elapsed_time = time.time() - start_time
        client.disconnect()
        return elapsed_time * 1000
    except Exception as e:
        return None

def save_valid_proxies(proxies):
    with open(OUTPUT_FILE, 'w') as file:
        for proxy in proxies:
            file.write(f"tg://proxy?server={proxy['server']}&port={proxy['port']}&secret={proxy['secret']}\n")

def main():
    proxy_links = get_proxies_from_file(PROXY_FILE)
    valid_proxies = []

    for proxy_link in proxy_links:
        proxy_info = parse_proxy(proxy_link)
        if proxy_info:
            ping = test_mtproto_proxy(proxy_info)
            if ping and ping < 250:
                valid_proxies.append(proxy_info)
                print(f"Proxy {proxy_info['server']} is valid with ping {ping:.2f}ms")
            else:
                print(f"Proxy {proxy_info['server']} is not valid or too slow")
        else:
            print(f"Invalid proxy format: {proxy_link}")

    if valid_proxies:
        save_valid_proxies(valid_proxies)
        print(f"Valid proxies saved to {OUTPUT_FILE}")
    else:
        print("No valid proxies found.")

if __name__ == '__main__':
    main()