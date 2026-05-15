from pages.to_do_page import TodoPage
from playwright.sync_api import expect


# ══════════════════════════════════════════════════════════════════
# Test 1 — Add Todo
# ══════════════════════════════════════════════════════════════════
def test_add_todo(page):
    todo = TodoPage(page)
    todo.navigate()

    todo.add_todo("Buy groceries")

    todo.expect_item_visible("Buy groceries")
    todo.expect_item_text("Buy groceries")
    todo.expect_count_text("1 item left")

    todo.take_screenshot("./reports/screenshots/test_add_todo.png")


# ══════════════════════════════════════════════════════════════════
# Test 2 — Complete Todo
# ══════════════════════════════════════════════════════════════════
def test_complete_todo(page):
    todo = TodoPage(page)
    todo.navigate()

    todo.add_todo("Read a book")

    todo.expect_checkbox_not_checked("Read a book")
    todo.complete_todo("Read a book")
    todo.expect_checkbox_checked("Read a book")
    todo.expect_item_completed("Read a book")
    todo.expect_count_text("0 items left")

    todo.take_screenshot("./reports/screenshots/test_complete_todo.png")


# ══════════════════════════════════════════════════════════════════
# Test 3 — Delete Todo
# ══════════════════════════════════════════════════════════════════
def test_delete_todo(page):
    todo = TodoPage(page)
    todo.navigate()

    todo.add_todo("Delete me")
    todo.expect_item_visible("Delete me")

    todo.delete_todo("Delete me")

    todo.expect_item_count(0)
    todo.expect_footer_hidden()

    todo.take_screenshot("./reports/screenshots/test_delete_todo.png")


# ══════════════════════════════════════════════════════════════════
# Test 4 — Filter Active
# ══════════════════════════════════════════════════════════════════
def test_filter_active(page):
    todo = TodoPage(page)
    todo.navigate()

    for task in ["Task Alpha", "Task Beta", "Task Gamma"]:
        todo.add_todo(task)

    todo.complete_todo("Task Alpha")
    todo.filter_active()

    todo.expect_item_count(2)
    expect_hidden = todo.get_item("Task Alpha")
    expect(expect_hidden).to_have_count(0)
    todo.expect_item_visible("Task Beta")
    todo.expect_item_visible("Task Gamma")

    todo.take_screenshot("./reports/screenshots/test_filter_active.png")


# ══════════════════════════════════════════════════════════════════
# Test 5 — Edit Todo
# ══════════════════════════════════════════════════════════════════
def test_edit_todo(page):
    todo = TodoPage(page)
    todo.navigate()

    todo.add_todo("Original text")
    todo.edit_todo("Original text", "Updated text")

    todo.expect_item_visible("Updated text")
    todo.expect_item_text("Updated text")
    todo.expect_count_text("1 item left")

    todo.take_screenshot("./reports/screenshots/test_edit_todo.png")