from pages.todo_page import TodoPage

#Scenario- Add the items
def test_add_todo(page):
    todo = TodoPage(page)
    todo.navigate("https://todomvc.com/examples/react/dist/#/")
    todo.add_todo("Buy Groceries")

#Scenario- Delete the item
def test_delete_todo(page):
    todo = TodoPage(page)
    todo.navigate("https://todomvc.com/examples/react/dist/#/")
    todo.add_todo("Buy Groceries")
    todo.add_todo("Read a Book")
    todo.delete_todo("Read a Book")

#Scenario- All Clear the items
def test_clear_all(page):
    todo = TodoPage(page)
    todo.navigate("https://todomvc.com/examples/react/dist/#/")
    todo.add_todo("Buy Groceries")
    todo.add_todo("Read a Book")
    todo.mark_completed("Buy Groceries")  # complete first
    todo.mark_completed("Read a Book")
    todo.clear_all_todo()


