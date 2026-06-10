from playwright.sync_api import sync_playwright
import pytest


@pytest.mark.skip(reason="Skip for now if needed")
def test_login_everdone():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        # Open site
        page.goto("https://app.everdone.ai/")

        # Login
        page.get_by_placeholder(
            "Enter your email"
        ).fill("kirankore057@gmail.com")

        page.get_by_placeholder(
            "Minimum 8 characters"
        ).fill("Pass@1234")

        page.get_by_role(
            "button",
            name="Login"
        ).click()

        # Wait for dashboard
        page.get_by_text(
            "CodeSecurity"
        ).wait_for(timeout=30000)

        print("Dashboard loaded")

        # Click View all
        page.locator(
            "div:has-text('CodeSecurity')"
        ).get_by_role(
            "button",
            name="View all"
        ).first.click()

        print("Clicked View all")

        # Wait for page
        page.wait_for_selector(
            "button:has-text('Generate documentation')",
            timeout=60000
        )

        print("CodeDoc page loaded")

        # Click Generate documentation
        page.get_by_role(
            "button",
            name="Generate documentation"
        ).click()

        print("Clicked Generate documentation")

        browser.close()