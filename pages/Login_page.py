class LoginPage:

    def __init__(self, page):
        self.page = page

    def open_site(self):
        self.page.goto("https://app.everdone.ai/")

    def login(self, email, password):

        self.page.get_by_placeholder(
            "Enter your email"
        ).fill(email)

        self.page.get_by_placeholder(
            "Minimum 8 characters"
        ).fill(password)

        self.page.get_by_role(
            "button",
            name="Login"
        ).click()

        print("Login successful")