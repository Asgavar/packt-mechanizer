import mechanize
import json

def get_login_info():
    with open("account.json") as account_json:
        account = account_json.read()
    account = json.loads(account)
    email = account["email"]
    password = account["password"]
    return email, password

def login(browser, email, password):
    browser.form = list(browser.forms())[1]    # packt-user-login-form
    # for control in browser.form.controls:
    #     print control
    email_control = browser.form.find_control("email")
    password_control = browser.form.find_control("password")
    email_control.value = email
    password_control.value = password
    # print email_control.value
    # print password_control.value
    browser.submit()

def main():
    email, password = get_login_info()
    br = mechanize.Browser()
    url = "https://www.packtpub.com/packt/offers/free-learning"
    br.open(url)
    login(br, email, password)

if __name__ == "__main__":
    main()
