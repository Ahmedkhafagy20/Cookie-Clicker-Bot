from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def available_items_number():
	all_items = [driver.find_element_by_id("product" + str(i)) for i in range(17)]
	available_items = 0
	for item in all_items:
		if "unlocked" in item.get_attribute("class"):
			available_items += 1
	return available_items

def filter_cookies_count(cookies_count_item):
	if "million" in cookies_count_item.text or "billion" in cookies_count_item.text or "trillion" in cookies_count_item.text or "quadrillion" in cookies_count_item.text or "quintillion" in cookies_count_item.text:
		cookie_count_number = float(cookies_count_item.text.split(" ")[0])
		cookies_count_factor = cookies_count_item.text.split(" ")[1]
		if cookies_count_factor == "million":
			return int(cookie_count_number * 1000000)
		if cookies_count_factor == "billion":
			return int(cookie_count_number * 1000000000)
		if cookies_count_factor == "trillion":
			return int(cookie_count_number * 1000000000000)
		if cookies_count_factor == "quadrillion":
			return int(cookie_count_number * 1000000000000000)
		if cookies_count_factor == "quintillion":
			return int(cookie_count_number * 1000000000000000000)
	else:
		cookies_count = cookies_count_item.text.split(" ")[0]
		cookies_count = cookies_count.replace(",", "")
		cookies_count = cookies_count.replace(" ", "")

	return cookies_count

def filter_item_price(item_price_element):
	item_price_element_used = item_price_element.text.replace(",", "")
	if len(item_price_element_used.split(" ")) > 1:
		item_price_number = float(item_price_element.text.split(" ")[0])
		item_price_factor = item_price_element.text.split(" ")[1]
		if item_price_factor == "million":
			return int(item_price_number * 1000000)
		if item_price_factor == "billion":
			return int(item_price_number * 1000000000)
		if item_price_factor == "trillion":
			return int(item_price_number * 1000000000000)
		if item_price_factor == "quadrillion":
			return int(item_price_number * 1000000000000000)
		if item_price_factor == "quintillion":
			return int(item_price_number * 1000000000000000000)
	else:
		return item_price_element_used


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")
try:
	bigcookie = WebDriverWait(driver, 300).until(
		EC.presence_of_element_located((By.ID, "bigCookie"))
		)	
	print("Bigcookie found")
except TimeoutException:
	print("Loading Sequence TimedOut")
try:
	cookies = WebDriverWait(driver, 300).until(
		EC.presence_of_element_located((By.ID, "cookies"))
		)	
	print("Bot starts in 30 seconds!!!")
	time.sleep(30)
	print("Bot Started!!")
except TimeoutException:
	print("Loading Sequence TimedOut")
clicking_chain = ActionChains(driver)
clicking_chain.double_click(bigcookie)
loops = int(input("Enter the number of wanted loops:..."))
for i in range(loops + 1):
	cookies_count = filter_cookies_count(cookies)
	clicking_chain.perform()
	items_number = available_items_number()
	if items_number > 0:
		items_list = [driver.find_element_by_id("productPrice" + str(i)) for i in range(items_number,-1,-1)]
		for item in items_list:
			item_price = filter_item_price(item)
			if item_price <= cookies_count:
				upgrading_action = ActionChains(driver)
				upgrading_action.click(item)
				upgrading_action.perform()

		



