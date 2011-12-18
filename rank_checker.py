# Simple Google rank checker
# Alex Z. 2011
# alex.g.zuniga@gmail.com
# Feel free to use the code as you wish
###
# 1. edit site.csv and replace google with your site
# 2. in edit.csv save your list of keywords
# 3. run this script
# 4. the ranks are saved in rank.csv
###
# requirements:
# - python
# - selenium with the browser driver you want to use
###

from selenium import webdriver
import csv
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

csvr_site = csv.reader(open('site.csv', 'rb'))
csvr_terms = csv.reader(open('terms.csv', 'rb'))
outfile = open('rank.csv', 'wb')
csvwriter = csv.writer(outfile)

for s in csvr_site:
	site = s[0]

print site

for row in csvr_terms:
	print row[0]
	driver.get("https://www.google.com")
	time.sleep(1)
	element = driver.find_element_by_name("q")
	element.click()
	element.clear()
	element.send_keys(row[0])

	time.sleep(5)
	doms = driver.find_elements_by_class_name("l")

	counter = 0
	rank = "not found"
	for dom in doms:
		counter += 1	
		href = dom.get_attribute("href")
		if site in href:
			rank = counter
			break

	csvwriter.writerow([row[0], rank])
	outfile.flush()
	time.sleep(2)
