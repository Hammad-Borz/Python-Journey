from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")

    quote = page.locator(".text").first.text_content()

    print(quote)

    browser.close()
