def test_add_fake_todos(todo_page, fake_todos):
    for item in fake_todos:
        todo_page.add_todo(item)
    todo_page.expect_item_count(5)

def test_add_static_todos(todo_page, static_todos):
    for item in static_todos:
        todo_page.add_todo(item)
    todo_page.expect_item_count(5)