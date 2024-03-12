from selenium import webdriver
import time

# list of distracting sites to limit
restricted_urls = ["https://www.reddit.com/",
                   "https://www.instagram.com/",
                   "https://www.tiktok.com/",
                   "https://twitter.com/",
                   "https://www.facebook.com/",
                   ]

chrome = webdriver.Chrome()
chrome.get("https://www.google.com/")
while True:
    if chrome.title in restricted_urls:
        chrome.close()
    print(chrome.title)
    time.sleep(2)

# .send_keys(Keys.CONTROL + 'w')

