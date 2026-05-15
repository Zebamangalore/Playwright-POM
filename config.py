from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL:str = os.getenv("BASE_URL")
BROWSER:str = os.getenv("BROWSER").lower()
HEADLESS:bool = os.getenv("HEADLESS").lower() in ("true", "t", "1", "yes")

if BROWSER == "all":
    BROWSERS = ["chromium", "firefox", "webkit"]
else:
    BROWSERS = [b.strip() for b in BROWSER.split(",")]