Version 17:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import simpledialog

class CleanScraperBot:
    # ... (existing code) ...

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    bot = CleanScraperBot("/path/to/chromedriver")

    # Test on a variety of websites
    test_urls = [
        ("http://example.com", ".css-selector-for-data"),
        # Add more test URLs and CSS selectors here
    ]

    for url, css_selector in test_urls:
        print(f"Testing on {url} with CSS selector {css_selector}")
        bot.navigate(url)
        bot.scrape(css_selector)
        bot.clean_data()
        print(bot.data)

    bot.close()
```

Version 18:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import simpledialog
import asyncio

class CleanScraperBot:
    # ... (existing code) ...

    async def run(self):
        # Test on a variety of websites
        test_urls = [
            ("http://example.com", ".css-selector-for-data"),
            # Add more test URLs and CSS selectors here
        ]

        for url, css_selector in test_urls:
            print(f"Testing on {url} with CSS selector {css_selector}")
            self.navigate(url)
            self.scrape(css_selector)
            self.clean_data()
            print(self.data)

        self.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    bot = CleanScraperBot("/path/to/chromedriver")
    asyncio.run(bot.run())
```
