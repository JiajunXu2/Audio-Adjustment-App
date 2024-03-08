from selenium import webdriver
import time

# list of distracting sites to limit
restricted_urls = ["https://www.reddit.com/",
                   ]

chrome = webdriver.Chrome()
#chrome.switch_to(chrome.window_handles[0])
# chrome.switch_to.window(chrome.window_handles)
chrome.get("https://www.youtube.com/")
print(chrome.title)
while True:
    if chrome.title == "Reddit":
        chrome.close()
    print(chrome.title)
    time.sleep(5)

# .send_keys(Keys.CONTROL + 'w')

