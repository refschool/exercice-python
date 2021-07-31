from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
options = Options()
# Make it go faster by running headless
# This will remove the web browser GUI from popping up
options.headless = True
driver = webdriver.Firefox(options=options)
# Enter whatever URL you like
driver.get("https://gitcoin.co/{}".format(link.attrs['href']))
# Let the code on their end run
time.sleep(20)
# Save it to a variable
html = driver.page_source
driver.quit()
# And then just paste it right back into beautifulsoup!
projects_soup = BeautifulSoup(html, 'lxml')