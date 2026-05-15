# Playwright-POM
POM FRAMEWORK + CI/CD PIPELINE  
Objective:  Build a structured Page Object Model framework for the SauceDemo app, add environment-based config, dynamic test data, and a working GitHub Actions CI/CD pipeline.
Tasks:
1. Create a pages/ folder with base_page.py (BasePage class), login_page.py (LoginPage), and inventory_page.py (InventoryPage) using POM.
2. Write 3 test flows in tests/: (1) successful login, (2) failed login with invalid credentials, (3) add an item to cart and verify cart count.
3. Add a .env file and config.py that reads BASE_URL, USERNAME, PASSWORD, BROWSER, and HEADLESS from environment variables.
4. Create a conftest.py that parametrizes the browser fixture across Chromium and Firefox, and add a Faker-based test data fixture.
5. Create .github/workflows/ui-tests.yml: install Python deps, install Playwright browsers, run pytest, and upload the HTML report as an artifact.
6. Confirm the CI pipeline passes on GitHub (push to main branch or open a PR).
