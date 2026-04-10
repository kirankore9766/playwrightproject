import pytest

BASE_URL = "https://app.everdone.ai/"


@pytest.fixture
def open_login_page(page):

    page.goto(BASE_URL)

    return page


def test_login_valid_user(open_login_page):

    page = open_login_page

    page.get_by_placeholder(
        "Enter your email"
    ).fill("valid@email.com")

    page.get_by_placeholder(
        "Minimum 8 characters"
    ).fill("ValidPass123")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    assert page.get_by_text(
        "CodeSecurity"
    ).is_visible()


def test_login_invalid_password(open_login_page):

    page = open_login_page

    page.get_by_placeholder(
        "Enter your email"
    ).fill("valid@email.com")

    page.get_by_placeholder(
        "Minimum 8 characters"
    ).fill("WrongPass")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    assert page.get_by_text(
        "Invalid"
    ).is_visible()


def test_login_empty_fields(open_login_page):

    page = open_login_page

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    assert page.get_by_text(
        "required"
    ).is_visible()