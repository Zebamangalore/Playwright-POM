import re
from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright, expect

with sync_playwright() as playwright:
    # ----Chromium------
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )
    page.screenshot(path="./reports/screenshots/chromium.png")
    browser.close()

    # ----Firefox------
    browser = playwright.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )
    page.screenshot(path="./reports/screenshots/firefox.png")
    browser.close()

    # ----Webkit------
    browser = playwright.webkit.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )
    page.screenshot(path="./reports/screenshots/webkit.png")
    browser.close()
