class CodeDocPage:

    def __init__(self, page):
        self.page = page

    def click_generate_documentation(self):

        self.page.wait_for_selector(
            "button:has-text('Generate documentation')",
            timeout=60000
        )

        self.page.get_by_role(
            "button",
            name="Generate documentation"
        ).click()

        print("Clicked Generate documentation")

    def click_continue(self):

        self.page.wait_for_selector(
            "text=Choose repository and branch",
            timeout=60000
        )

        self.page.get_by_role(
            "button",
            name="Continue"
        ).click()

        print("Continue clicked")