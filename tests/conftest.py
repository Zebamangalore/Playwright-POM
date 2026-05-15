import pytest
import json
from faker import Faker
from playwright.sync_api import Page
from config import BROWSERS, HEADLESS, BASE_URL
from pages.todo_env_page import TodoPage
from playwright.sync_api import sync_playwright

def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        metafunc.parametrize("browser_name", BROWSERS)

@pytest.fixture(scope="function")
def browser_name(request):
    return request.param

def pytest_configure(config):
    # ── Unregister pytest-playwright's plugin so it stops
    #    interfering with our own browser_name parametrization ──
    config.pluginmanager.unregister(name="playwright")

@pytest.fixture(scope="function")
def page(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(
            headless=HEADLESS,
            slow_mo=500
        )
        context = browser.new_context(base_url=BASE_URL)
        pg      = context.new_page()

        yield pg

        context.close()
        browser.close()

# @pytest.fixture(scope="session")
# def browser_type_launch_args():
#     return {"headless": HEADLESS, "slow_mo":500}
#
# @pytest.fixture(scope="session")
# def browser_context_kwargs(browser_type_launch_args):
#     return {**browser_type_launch_args, "base_url":BASE_URL}

@pytest.fixture(scope="function", autouse=True)
def trace_each(page: Page, request):
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    trace_name = request.node.name.replace("/", "_")
    page.context.tracing.stop(path=f"./reports/traces/{trace_name}.zip")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome=yield
    report=outcome.get_result()
    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page")
        if page:
            safe_name = item.name.replace("/", "_")
            page.screenshot(
                path=f"./reports/screenshot/Fail_{safe_name}.png",
            full_page = True)
            print(f"\n📸 Failure screenshot saved: FAIL_{safe_name}.png")

# def pytest_addoption(parser):
#     pass  # Playwright already adds --browser

# def pytest_configure(config):
#     # Only inject if user didn't already pass --browser
#     if not any("--browser" in arg for arg in config.invocation_params.args):
#         config.option.browser = BROWSERS

@pytest.fixture(scope="function")  # ✅ matches page's scope
def todo_page(page):
    tp = TodoPage(page)
    tp.page.goto(BASE_URL)
    return tp

fake = Faker()

@pytest.fixture(scope="function")
def fake_todos():
    return [fake.sentence(nb_words=5) for _ in range(5)]

@pytest.fixture(scope="function")
def static_todos():
    with open("test_data/todos.json") as f:
        data = json.load(f)
    return data["todos"]


