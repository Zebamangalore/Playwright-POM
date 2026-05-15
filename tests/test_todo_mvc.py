import re
import pytest
from playwright.sync_api import Page, expect

URL = "https://demo.playwright.dev/todomvc"


# ══════════════════════════════════════════════════════════════════════════════
# Shared helpers
# ══════════════════════════════════════════════════════════════════════════════

def add_todo(page: Page, text: str) -> None:
    page.get_by_placeholder("What needs to be done?").fill(text)
    page.keyboard.press("Enter")


def get_item(page: Page, text: str):
    return page.get_by_test_id("todo-item").filter(has_text=text)


# ══════════════════════════════════════════════════════════════════════════════
# Test 1 — Add Todo
# ══════════════════════════════════════════════════════════════════════════════

def test_add_todo(page: Page) -> None:
    page.goto(URL)

    add_todo(page, "Buy groceries")

    item = get_item(page, "Buy groceries")
    expect(item).to_be_visible()
    expect(item).to_have_text("Buy groceries")

    # ✅ No exclamation mark
    expect(page.locator(".todo-count")).to_have_text("1 item left")

    page.screenshot(path="./reports/screenshots/test_add_todo.png")


# ══════════════════════════════════════════════════════════════════════════════
# Test 2 — Complete Todo
# ══════════════════════════════════════════════════════════════════════════════

def test_complete_todo(page: Page) -> None:
    page.goto(URL)

    add_todo(page, "Read a book")

    item = get_item(page, "Read a book")
    checkbox = item.get_by_role("checkbox")

    expect(checkbox).not_to_be_checked()
    checkbox.check()

    expect(checkbox).to_be_checked()
    expect(item).to_have_class(re.compile(r"\bcompleted\b"))

    # ✅ No exclamation mark
    expect(page.locator(".todo-count")).to_have_text("0 items left")

    page.screenshot(path="./reports/screenshots/test_complete_todo.png")


# ══════════════════════════════════════════════════════════════════════════════
# Test 3 — Delete Todo
# ══════════════════════════════════════════════════════════════════════════════

def test_delete_todo(page: Page) -> None:
    page.goto(URL)

    add_todo(page, "Delete me")

    item = get_item(page, "Delete me")
    expect(item).to_be_visible()

    item.hover()
    item.get_by_role("button", name="Delete").click()

    expect(page.get_by_test_id("todo-item")).to_have_count(0)
    expect(page.locator(".footer")).to_be_hidden()

    page.screenshot(path="./reports/screenshots/test_delete_todo.png")


# ══════════════════════════════════════════════════════════════════════════════
# Test 4 — Filter Active
# ══════════════════════════════════════════════════════════════════════════════

def test_filter_active(page: Page) -> None:
    page.goto(URL)

    for todo in ["Task Alpha", "Task Beta", "Task Gamma"]:
        add_todo(page, todo)

    get_item(page, "Task Alpha").get_by_role("checkbox").check()

    page.get_by_role("link", name="Active").click()

    items = page.get_by_test_id("todo-item")
    expect(items).to_have_count(2)

    expect(get_item(page, "Task Alpha")).to_have_count(0)
    expect(get_item(page, "Task Beta")).to_be_visible()
    expect(get_item(page, "Task Gamma")).to_be_visible()

    page.screenshot(path="./reports/screenshots/test_filter_active.png")


# ══════════════════════════════════════════════════════════════════════════════
# Test 5 — Edit Todo
# ══════════════════════════════════════════════════════════════════════════════

def test_edit_todo(page: Page) -> None:
    page.goto(URL)

    add_todo(page, "Original text")

    item = get_item(page, "Original text")
    label = item.locator("label")
    label.dblclick()

    edit_input = item.get_by_role("textbox")
    expect(edit_input).to_be_visible()
    expect(edit_input).to_be_focused()

    edit_input.fill("Updated text")
    page.keyboard.press("Enter")

    # ✅ Re-query by the NEW text — the old filter is now stale
    updated_item = get_item(page, "Updated text")
    expect(updated_item).to_be_visible()
    expect(updated_item).to_have_text("Updated text")

    # Count stays the same — no item was added or removed
    expect(page.locator(".todo-count")).to_have_text("1 item left")

    page.screenshot(path="./reports/screenshots/test_edit_todo.png")