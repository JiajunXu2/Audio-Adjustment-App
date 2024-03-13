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
"""
for urls in restricted_urls:
    domain = urlparse(urls).netloc
    print(domain)
"""
 
chrome = webdriver.Chrome()
chrome.get("https://www.google.com/")
while True:
    active_window = chrome.switch_to.window(chrome.window_handles[0])
    domain = urlparse(active_window.current_url)
    if domain in restricted_urls:
        chrome.close()
    
    time.sleep(2)


