import re
from playwright.sync_api import Page, Browser, BrowserContext, sync_playwright, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

# Run with firefox headed and slow motion
# pytest tests/test_launch_browsers_command.py -v --browser firefox --headed --slowmo 50
# pytest tests/test_launch_browsers_command.py -v --browser chromium --headed --slowmo 50
# pytest tests/test_launch_browsers_command.py -v --browser webkit --headed --slowmo 50
# pytest tests/test_launch_browsers.py -v --browser chromium --browser firefox --browser webkit