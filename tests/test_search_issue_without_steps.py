from selene import browser, by, be, have
from selene.support.shared.jquery_style import s


def test_search_issue_without_steps(browser_start):
    browser.open('https://github.com/Lord-Aectan/QA-Guru-Allure-reports')
    s('#issues-tab').click()
    s(by.partial_text('#1')).should(be.visible)
