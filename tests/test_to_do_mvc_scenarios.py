import re
from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright, expect

with sync_playwright() as playwright:
    # ----Chromium------
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")

    # Step 1 — add a todo item first
    page.get_by_placeholder("What needs to be done?").fill("Buy groceries")
    page.keyboard.press("Enter")

    # Step 2 — NOW .todo-count exists and is visible
    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    print(count.inner_text())  # prints "1 item left"

    # Step 3 — add a todo item first
    page.get_by_placeholder("What needs to be done?").fill("Read a Book")
    page.keyboard.press("Enter")

    # Step 4 — NOW .todo-count exists and is visible
    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    print(count.inner_text())  # prints "2 item left"

    # Step 5 — add a todo item first
    page.get_by_placeholder("What needs to be done?").fill("Drink Detox")
    page.keyboard.press("Enter")

    # Step 6 — NOW .todo-count exists and is visible
    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    print(count.inner_text())  # prints "3 item left"
    page.screenshot(path="./reports/screenshots/chromium_add_to_do.png")

    # Step 7 — Click Checkbox and assert strikethrough
    item = page.get_by_test_id("todo-item").filter(has_text="Buy groceries")
    checkbox = item.get_by_role("checkbox")
    expect(checkbox).not_to_be_checked()
    checkbox.check()
    expect(checkbox).to_be_checked()
    expect(item).to_have_class("completed")

    page.screenshot(path="./reports/screenshots/chromium_add_to_do_check.png")

    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    print(count.inner_text())  # prints "2 item left"

    # Step 8 — Click on Clear Completed
    button = page.get_by_role("button", name="Clear completed")
    expect(button).to_have_class("clear-completed")
    button.click()

    page.screenshot(path="./reports/screenshots/chromium_clear_completed.png")

    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    print(count.inner_text())  # prints "2 item left"

    browser.close()