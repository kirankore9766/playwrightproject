from pages.Login_page import LoginPage
from pages.Dashboard_page import DashboardPage
from pages.codesecuirty_page import CodeSecurityPage
from pages.codedoc_page import CodeDocPage


def test_end_to_end(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    codesecurity = CodeSecurityPage(page)
    codedoc = CodeDocPage(page)

    login.open_site()

    login.login(
        "kirankore057@gmail.com",
        "Pass@1234"
    )

    dashboard.wait_for_dashboard()

    codesecurity.click_view_all()

    codedoc.click_generate_documentation()

    codedoc.click_continue()

    print("End-to-End test completed")