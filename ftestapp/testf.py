# from selenium import webdriver
# import unittest
# from selenium.webdriver.common.keys import Keys
# import time
# from django.test import LiveServerTestCase


# cWait=3

# class PageTest(LiveServerTestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()

# 	#def tearDown(self):
# 		#self.browser.quit()

# 	def check_rows_table(self,row_text):
# 		start_time = time.time()
# 		while time.time() - start_time<cWait:
# 			time.sleep(0.5)
# 			try:
# 				table = self.browser.find_element_by_id('regtbl')
# 				rows = table.find_elements_by_tag_name('tr')
# 				self.assertIn(row_text,[row.text for row in rows])
# 				return
# 			except (AssertionError, WebDriverException) as e:
# 				if time.time()- start_time<cWait:
# 					raise e

# 	def test_start_list_and_retrieve_it(self):
# 		self.browser.get(self.live_server_url)
# 		self.assertIn('PC Starter Facts', self.browser.title)
# 		headerText = self.browser.find_element_by_tag_name('h1').text
# 		self.assertIn('PC Starter Facts', headerText)
# 		#USERINFO
# 		UName = self.browser.find_element_by_id('name')
# 		UProc = self.browser.find_element_by_id('proc')
# 		UMobo = self.browser.find_element_by_id('mobo')
# 		UGpu = self.browser.find_element_by_id('gpu')
# 		UDescrip = self.browser.find_element_by_id('desc')
# 		submt = self.browser.find_element_by_id('subbtn')
# 		self.assertEqual(UName.get_attribute('placeholder'),'Enter your name here.')
# 		#User Name
# 		UName.click()
# 		UName.send_keys('Jay-ar Saballa')
# 		time.sleep(0.5)
# 		#Processor
# 		UProc.click()
# 		UProc.send_keys('Ryzen 5 2600')
# 		time.sleep(0.5)
# 		#Motherboard
# 		UMobo.click()
# 		UMobo.send_keys('B450 Mortar Max')
# 		time.sleep(0.5)
# 		#GPU
# 		UGpu.click()
# 		UGpu.send_keys('GTX 1660 Super')
# 		time.sleep(0.5)
# 		#Description
# 		UDescrip.click()
# 		UDescrip.send_keys('Editting and Gaming')
# 		time.sleep(0.5)

# 		submt.click()
# 		time.sleep(0.1)

# 		#NextEntry
# 		UName = self.browser.find_element_by_id('name')
# 		UProc = self.browser.find_element_by_id('proc')
# 		UMobo = self.browser.find_element_by_id('mobo')
# 		UGpu = self.browser.find_element_by_id('gpu')
# 		UDescrip = self.browser.find_element_by_id('desc')
# 		submt = self.browser.find_element_by_id('subbtn')
# 		self.assertEqual(UName.get_attribute('placeholder'),'Enter your name here.')
# 		#User Name
# 		UName.click()
# 		UName.send_keys('Jing')
# 		time.sleep(0.5)
# 		#Processor
# 		UProc.click()
# 		UProc.send_keys('Ryzen 3 3400G')
# 		time.sleep(0.5)
# 		#Motherboard
# 		UMobo.click()
# 		UMobo.send_keys('B450 Tomahawk')
# 		time.sleep(0.5)
# 		#GPU
# 		UGpu.click()
# 		UGpu.send_keys('GTX 1050 Ti')
# 		time.sleep(0.5)
# 		#Description
# 		UDescrip.click()
# 		UDescrip.send_keys('Web Browsing')
# 		time.sleep(0.5)

# 		submt.click()
# 		time.sleep(0.1)

# 		self.check_rows_table('1: Jay-ar Saballa Ryzen 5 2600 B450 Mortar Max GTX 1660 Super Editting and Gaming')
# 		self.check_rows_table('2: Jing Ryzen 3 3400G B450 Tomahawk GTX 1050 Ti Web Browsing')

# 	def test_next_entry(self):
# 		self.browser.get(self.live_server_url)
# 		time.sleep(1)
# 		self.assertIn('PC Starter Facts', self.browser.title)
# 		headerText = self.browser.find_element_by_tag_name('h1').text
# 		self.assertIn('PC Starter Facts', headerText)
# 		UName = self.browser.find_element_by_id('name')
# 		UProc = self.browser.find_element_by_id('proc')
# 		UMobo = self.browser.find_element_by_id('mobo')
# 		UGpu = self.browser.find_element_by_id('gpu')
# 		UDescrip = self.browser.find_element_by_id('desc')
# 		submt = self.browser.find_element_by_id('subbtn')
# 		self.assertEqual(UName.get_attribute('placeholder'),'Enter your name here.')
# 		#User Name
# 		UName.click()
# 		UName.send_keys('Jing')
# 		time.sleep(0.5)
# 		#Processor
# 		UProc.click()
# 		UProc.send_keys('Ryzen 3 3400G')
# 		time.sleep(0.5)
# 		#Motherboard
# 		UMobo.click()
# 		UMobo.send_keys('B450 Tomahawk')
# 		time.sleep(0.5)
# 		#GPU
# 		UGpu.click()
# 		UGpu.send_keys('GTX 1050 Ti')
# 		time.sleep(0.5)
# 		#Description
# 		UDescrip.click()
# 		UDescrip.send_keys('Web Browsing')
# 		time.sleep(0.5)

# 		submt.click()
# 		time.sleep(0.1)

# 		self.check_rows_table('1: Jing Ryzen 3 3400G B450 Tomahawk GTX 1050 Ti Web Browsing')
# #if __name__ == '__main__':
# 	#unittest.main(warnings='ignore')
