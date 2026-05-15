import re
from playwright.sync_api import sync_playwright, expect


def add_todo(page, text: str) -> None:
    """Add a single todo item and assert it was counted."""
    page.get_by_placeholder("What needs to be done?").fill(text)
    page.keyboard.press("Enter")


def complete_todo(page, text: str) -> None:
    """Check a todo item and assert it moved to completed state."""
    item = page.get_by_test_id("todo-item").filter(has_text=text)
    checkbox = item.get_by_role("checkbox")
    expect(checkbox).not_to_be_checked()
    checkbox.check()
    expect(checkbox).to_be_checked()
    expect(item).to_have_class("completed")


def assert_count(page, expected: str) -> None:
    """Assert the todo count footer shows the expected text."""
    count = page.locator(".todo-count")
    expect(count).to_be_visible()
    expect(count).to_have_text(expected)
    print(f"✅ Count: {count.inner_text()}")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")

    # ── Step 1: Add 3 items ───────────────────────────────────────────────────
    todos = ["Buy groceries", "Read a Book", "Drink Detox"]
    for i, todo in enumerate(todos, start=1):
        add_todo(page, todo)
        assert_count(page, f"{i} item{'s' if i > 1 else ''} left!")

    page.screenshot(path="./reports/screenshots/chromium_add_to_do.png")

    # ── Step 2: Complete 2 items ──────────────────────────────────────────────
    items_to_complete = ["Buy groceries", "Read a Book"]
    for todo in items_to_complete:
        complete_todo(page, todo)

    assert_count(page, "1 item left!")
    page.screenshot(path="./reports/screenshots/chromium_completed.png")

    # ── Step 3: Clear completed ───────────────────────────────────────────────
    button = page.get_by_role("button", name="Clear completed")
    expect(button).to_have_class("clear-completed")
    button.click()

    page.screenshot(path="./reports/screenshots/chromium_clear_completed.png")

    # ── Step 4: Assert only "Drink Detox" remains ────────────────────────────
    remaining = page.get_by_test_id("todo-item")
    expect(remaining).to_have_count(1)
    expect(remaining.first).to_have_text("Drink Detox")
    assert_count(page, "1 item left!")
    print("✅ Lifecycle complete!")

    browser.close()