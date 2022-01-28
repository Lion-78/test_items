# import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_found(browser):
    browser.get(link)
    button = []
    try:
        browser.implicitly_wait(10)
        button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    except:
        assert len(button) > 0, "Button 'Add to basket' is not found"

    # time.sleep(30)