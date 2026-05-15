import re
from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright, expect

with sync_playwright() as playwright:
    # ----Chromium------
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")

    page.get_by_role("link", name="TodoMVC").click()
    page.screenshot(path="./reports/screenshots/chromium_role.png")

    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_label("New Todo Input").fill("Zeba")
    page.screenshot(path="./reports/screenshots/chromium_label.png")
    page.keyboard.press("Enter")
    element = page.get_by_text("Zeba")
    expect(element).to_be_visible()  # assert it exists
    print(element.inner_text())  # read its text
    page.screenshot(path="./reports/screenshots/chromium_text.png")

    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("test")
    page.screenshot(path="./reports/screenshots/chromium_placeholder.png")

    # Step 1 — add a todo item first
    page.get_by_placeholder("What needs to be done?").fill("Buy groceries")
    page.keyboard.press("Enter")

    # Step 2 — NOW .todo-count exists and is visible
    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    print(count.inner_text())  # prints "1 item left"
    page.screenshot(path="./reports/screenshots/chromium_css.png")

    browser.close()

    # # ----Firefox------
    # browser = playwright.firefox.launch(headless=False, slow_mo=50)
    # page = browser.new_page()
    # page.goto("https://playwright.dev/")
    # expect(page).to_have_title(
    #     "Fast and reliable end-to-end testing for modern web apps | Playwright"
    # )
    # page.screenshot(path="./reports/screenshots/firefox.png")
    # browser.close()
    #
    # # ----Webkit------
    # browser = playwright.webkit.launch(headless=False, slow_mo=50)
    # page = browser.new_page()
    # page.goto("https://playwright.dev/")
    # expect(page).to_have_title(
    #     "Fast and reliable end-to-end testing for modern web apps | Playwright"
    # )
    # page.screenshot(path="./reports/screenshots/webkit.png")
    # browser.close()
