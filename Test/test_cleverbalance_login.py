from playwright.sync_api import sync_playwright

def test_cleverbalance_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://app.cleverbalance.ai/")

        # Login
        page.get_by_placeholder("Enter your email").fill("kirankore057@gmail.com")
        page.get_by_placeholder("Minimum 8 characters").fill("Pass@9766")

        page.get_by_role("button", name="Login").click()

        # Wait until dashboard loads
        page.wait_for_load_state("networkidle")

        # Click View all
        page.get_by_text("View all").click()

        page.pause()

test_cleverbalance_login()