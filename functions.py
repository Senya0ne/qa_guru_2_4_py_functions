def print_func_details(func, *args):
    print(f"Function name is: {func.__name__.replace('_', ' ')} \n arguments values is {args}")


def open_browser(browser_name):
    print_func_details(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_func_details(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_details(find_registration_button_on_login_page, page_url, button_text)


open_browser("Firefox")
go_to_companyname_homepage("https://apple.com")
find_registration_button_on_login_page("https://apple.com", "Buy")
