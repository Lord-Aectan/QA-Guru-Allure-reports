import allure
from allure_commons.types import Severity
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s


#Чистый Selene (без шагов)
def test_search_issue_without_steps(browser_start):
    browser.open('https://github.com/Lord-Aectan/QA-Guru-Allure-reports')
    s('#issues-tab').click()
    s(by.partial_text('#1')).should(be.visible)


#Лямбда шаги через with allure.step
def test_search_issue_with_steps(browser_start):
    with allure.step('Открываем репозиторий'):
        browser.open('https://github.com/Lord-Aectan/QA-Guru-Allure-reports')

    with allure.step('Ищем id issue-tab и переходим в него по клику'):
        s('#issues-tab').click()

    with allure.step('Проверяем, что отображается issue под номером #1'):
        s(by.partial_text('#1')).should(be.visible)


#Шаги с декоратором @allure.step
def test_decorator_search_issue(browser_start):
    open_repository()
    search_issue_tab('#issues-tab')
    should_see_issue_with_number('#1')

@allure.step('Открываем репозиторий')
def open_repository():
    browser.open('https://github.com/Lord-Aectan/QA-Guru-Allure-reports')


@allure.step('Ищем id {issue_tab} и переходим в него по клику')
def search_issue_tab(issue_tab):
    s(f'{issue_tab}').click()


@allure.step('Проверяем, что отображается issue под номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(f'{number}')).should(be.visible)


#Разметка тестов всеми аннотациями
@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Daniil Moiseenko')
@allure.feature('Задачи в репозитории')
@allure.story('Отображается issue с конкретным номером ')
@allure.link('https://github.com/Lord-Aectan/QA-Guru-Allure-reports')
def test_decorator_labels():
    browser.open('https://github.com/Lord-Aectan/QA-Guru-Allure-reports')
    s('#issues-tab').click()
    s(by.partial_text('#1')).should(be.visible)