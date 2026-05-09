from playwright.sync_api import sync_playwright

def test_login_everdone():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
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

        # Click CodeSecurity View all
        page.locator(
            "div:has-text('CodeSecurity')"
        ).get_by_role(
            "button",
            name="View all"
        ).first.click()

        print("Clicked CodeSecurity View all")

        # Wait for CodeDoc page
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

        # Wait for repository form
        page.wait_for_selector(
            "text=Choose repository and branch",
            timeout=60000
        )

        print("Repository form loaded")

        # Click Continue (values already selected)
        continue_btn = page.get_by_role(
            "button",
            name="Continue"
        )

        continue_btn.wait_for(timeout=30000)
        continue_btn.click()

        print("Continue clicked")

        # Wait for next process/page
        page.wait_for_timeout(5000)

        browser.close()