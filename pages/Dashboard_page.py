class DashboardPage:

    def __init__(self, page):
        self.page = page

    def wait_for_dashboard(self):

        self.page.get_by_text(
            "CodeSecurity"
        ).wait_for(timeout=30000)

        print("Dashboard loaded")