def open_browser(browser_name):
    print_function_name_and_arguments(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_function_name_and_arguments(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_function_name_and_arguments(find_registration_button_on_login_page, page_url, button_text)


def print_function_name_and_arguments(function_name, *args):
    function_name = function_name.__name__.title().replace('_', ' ')
    print(f'\nThis function\'s name is: {function_name}.\nFunction arguments are: ')

    for arg in args:
        print(arg)

open_browser("Chrome")
go_to_companyname_homepage("http://web.archive.org/")
find_registration_button_on_login_page("https://archive.org/account/login", "Log in")