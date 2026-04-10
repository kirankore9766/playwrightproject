class CodeSecurityPage:

    def __init__(self, page):
        self.page = page

    def click_view_all(self):
        
        self.page.locator(
            "div:has-text('CodeSecurity')"
        ).get_by_role(
            "button",
            name="View all"
        ).first.click()

        print("Clicked CodeSecurity View all")