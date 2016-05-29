#!/usr/bin/env python2

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
    email_control = browser.form.find_control("email")
    password_control = browser.form.find_control("password")
    email_control.value = email
    password_control.value = password
    browser.submit()


def claim(browser):
    for link in browser.links():
        if "claim" in link.url:
            claim_link = link
            break
    res = browser.follow_link(claim_link)


def main():
    email, password = get_login_info()
    print "[*] account used: ", email
    br = mechanize.Browser()
    url = "https://www.packtpub.com/packt/offers/free-learning"
    br.open(url)
    print "[*] logging..."
    login(br, email, password)
    print "[*] claiming book..."
    try:
        claim(br)
        print "[*] succesfully claimed a book!"
    except:
        print "[*] claiming error, probably login details are wrong"


if __name__ == "__main__":
    main()
