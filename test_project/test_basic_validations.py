import time
import pytest
from playwright.sync_api import Page, expect


def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page().goto("http://rahulshettyacademy.com/")

# chromium headless mode, 1 single context
def test_playwright_shortcut(page: Page):
    page.goto("http://rahulshettyacademy.com/")

@pytest.mark.smoke
def test_negative_login_wrong_password(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("qwertyhjmn") # rahulshettyacademy
    page.get_by_label("Password").fill("123") # learning
    page.get_by_role("combobox").select_option("teach")
    # page.get_by_role("link", name="terms and conditions").check()
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefox(playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("qwertyhjmn")  # rahulshettyacademy
    page.get_by_label("Password").fill("123")  # learning
    page.get_by_role("combobox").select_option("teach")
    # page.get_by_role("link", name="terms and conditions").check()
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    browser.close()


@pytest.mark.regression
def test_child_window_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_tab = new_page.value
        elem_text = child_tab.locator(".red").text_content()
        words = elem_text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"









