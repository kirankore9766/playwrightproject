from playwright.sync_api import expect, sync_playwright

CLEVERBALANCE_URL = "https://app.cleverbalance.ai/"
EMAIL = "kirankore057@gmail.com"
PASSWORD = "Pass@9766"


def test_first_bank_reconciliation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto(CLEVERBALANCE_URL)

        page.get_by_placeholder("Enter your email").fill(EMAIL)
        page.get_by_placeholder("Minimum 8 characters").fill(PASSWORD)
        page.get_by_role("button", name="Login").click()

        page.wait_for_load_state("networkidle")

        page.get_by_text("View all").click()
        page.get_by_text("New reconciliation").click()

        page.wait_for_url("**/products/reconciliation/new**", timeout=60000)
        expect(page.get_by_role("heading", name="New reconciliation")).to_be_visible()

        page.get_by_text("Choose reconciliation type").click()
        page.get_by_text("Bank reconciliation", exact=True).click()

        expect(page.get_by_text("Bank statement vs books")).to_be_visible()

        page.get_by_text("Uplod file",exact=True).click()

        browser.close()
