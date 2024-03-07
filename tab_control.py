from selenium import webdriver

# list of distracting sites to limit
restricted_urls = ["https://www.reddit.com/",
                   ]

chrome = webdriver.Chrome()
print(chrome.window_handles)
#chrome.switch_to.window(chrome.window_handles)
#chrome.get("https://www.youtube.com/")

while True:
    pass
