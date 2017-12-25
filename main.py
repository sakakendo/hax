import requests
from requests.auth import HTTPDigestAuth
import selenium
from selenium import webdriver

cookie_name = 'session_id'

s = requests.session()
url = "http://sakakendo.pythonanywhere.com/digest"
username = "XXX"
password = "xxx"
res = s.get(url, auth=HTTPDigestAuth(username,password))
res.raise_for_status()
print(res.status_code,res.content)

"""
cookie_value = s.cookies.get(cookie_name)

driver=webdriver.PhantomJS(executable_path="phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver.get(url)
driver.add_cookie({
		'name': cookie_name,
		'value': cookie_value,
		'domain': 'sakakendo.pythonanywhere.com'})
diver.get(url)
"""
