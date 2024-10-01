#https://www.youtube.com/watch?v=tnrsSJ17ei8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ChromeOptions options = new ChromeOptions();
options.setBinary("/path/to/other/chrome/binary");

browser = webdriver.Chrome(executable_path=r'chromedriver.exe')   #mac https://stackoverflow.com/questions/76928765/attributeerror-str-object-has-no-attribute-capabilities-in-selenium
#driver = webdriver.Chrome('./chromedriver'). #ne marche pas sur Mac

browser.get("https://www.python.org")

print(browser.title)