import requests




#  configs
key = ("")    #  Your pastebin api_dev_key get it over here https://pastebin.com/doc_api#1
username = ("")    #  Your pastebin username
password = ("")    #  Your pastebin password


#  loging into pastebin
login_data = {
    'api_dev_key': key, 
    'api_user_name': username,
    'api_user_password': password
             }
data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':content,
    'api_paste_name':"paste",
    'api_paste_expire_date': 'see_https://pastebin.com/api',
    'api_user_key': None,
    'api_paste_format': 'see_https://pastebin.com/api'
       }

def upload():
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    return r.text

link = upload()
print(f"Paste URL: {link}")