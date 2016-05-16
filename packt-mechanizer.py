import mechanize
import json

def get_login_info():
    with open("account.json") as account_json:
        account = account_json.read()
    account = json.loads(account)
    email = account["email"]
    password = account["password"]
    return email, password
