from playwright.sync_api import expect
# ══════════════════════════════════════════════════════════════════
# Test 1 — Add Todo
# ══════════════════════════════════════════════════════════════════
def test_add_todo(todo_page):
    todo_page.add_todo("Buy groceries")

    todo_page.expect_item_visible("Buy groceries")
    todo_page.expect_item_text("Buy groceries")
    todo_page.expect_count_text("1 item left")

    todo_page.take_screenshot("./reports/screenshots/test_add_todo.png")


# ══════════════════════════════════════════════════════════════════
# Test 2 — Complete Todo
# ══════════════════════════════════════════════════════════════════
def test_complete_todo(todo_page):
    todo_page.add_todo("Read a book")

    todo_page.expect_checkbox_not_checked("Read a book")
    todo_page.complete_todo("Read a book")
    todo_page.expect_checkbox_checked("Read a book")
    todo_page.expect_item_completed("Read a book")
    todo_page.expect_count_text("0 items left")

    todo_page.take_screenshot("./reports/screenshots/test_complete_todo.png")


# ══════════════════════════════════════════════════════════════════
# Test 3 — Delete Todo
# ══════════════════════════════════════════════════════════════════
def test_delete_todo(todo_page):
    todo_page.add_todo("Delete me")
    todo_page.expect_item_visible("Delete me")

    todo_page.delete_todo("Delete me")

    todo_page.expect_item_count(0)
    todo_page.expect_footer_hidden()

    todo_page.take_screenshot("./reports/screenshots/test_delete_todo.png")


# ══════════════════════════════════════════════════════════════════
# Test 4 — Filter Active
# ══════════════════════════════════════════════════════════════════
def test_filter_active(todo_page):
    for task in ["Task Alpha", "Task Beta", "Task Gamma"]:
        todo_page.add_todo(task)

    todo_page.complete_todo("Task Alpha")
    todo_page.filter_active()

    todo_page.expect_item_count(2)
    expect_hidden = todo_page.get_item("Task Alpha")
    expect(expect_hidden).to_have_count(0)
    todo_page.expect_item_visible("Task Beta")
    todo_page.expect_item_visible("Task Gamma")

    todo_page.take_screenshot("./reports/screenshots/test_filter_active.png")


# ══════════════════════════════════════════════════════════════════
# Test 5 — Edit Todo
# ══════════════════════════════════════════════════════════════════
def test_edit_todo(todo_page):
    todo_page.add_todo("Original text")
    todo_page.edit_todo("Original text", "Updated text")

    todo_page.expect_item_visible("Updated text")
    todo_page.expect_item_text("Updated text")
    todo_page.expect_count_text("1 item left")

    todo_page.take_screenshot("./reports/screenshots/test_edit_todo.png")