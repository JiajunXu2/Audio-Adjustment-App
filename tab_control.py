from selenium import webdriver
from urllib.parse import urlparse
import time

# list of distracting sites to limit
restricted_urls = ["www.reddit.com",
                   "www.instagram.com",
                   "www.tiktok.com",
                   "twitter.com",
                   "www.facebook.com",
                   ]

# constantly check if new tab is restricted site
chrome = webdriver.Chrome()
chrome.get("https://www.google.com/")
while True:
    print(chrome.window_handles)
    rightmost = len(chrome.window_handles) - 1
    chrome.switch_to.window(chrome.window_handles[rightmost])
    domain = urlparse(chrome.current_url).netloc
    print(domain)
    if domain in restricted_urls:
        chrome.close()
        chrome.switch_to.window(chrome.window_handles[0])
    time.sleep(8)


