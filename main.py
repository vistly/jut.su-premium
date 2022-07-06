from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
config = configparser.ConfigParser()

config.read('config.ini')

chromeOptions = webdriver.ChromeOptions()

if config['DEFAULT']['ad_block'] == '1':
	chromeOptions.add_extension('exp/adblock.crx')
else:
	pass


driver = webdriver.Chrome('driver/chromedriver.exe', chrome_options=chromeOptions)


driver.get('https://jut.su')

sleep(1)
if config['ACCAUNT']['logging_acc'] == '1':
	button_login_start = driver.find_element('xpath','/html/body/div[4]/a').click()

	field_login = driver.find_element('xpath','//*[@id="login_input1"]').send_keys(config['ACCAUNT']['login'])
	field_passw = driver.find_element('xpath','//*[@id="login_input2"]').send_keys(config['ACCAUNT']['password'])

	btn_submit = driver.find_element('xpath','//*[@id="login_submit"]').click()



else:
	pass




while True:
	if config['DEFAULT']['skip_opening'] == '1':
		try:
			driver.find_element('xpath', '//*[@id="my-player"]/div[4]').click()
		except:
			pass

	if config['DEFAULT']['skip_ending'] == '1':
		try:
			driver.find_element('xpath', '//*[@id="my-player"]/div[6]').click()
		except:
			pass



	try:
		lab  = driver.find_element('xpath', '//*[@id="dle-content"]/div/noindex/div/div/div[2]')
		driver.execute_script(f"arguments[0].textContent='скрипт зделан Владом)'", lab)
	except:
		pass

