import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from configparser import ConfigParser

configParser = ConfigParser()
configParser.read('../../config/configuration_file.ini')
default_brower = configParser.get('setting', 'default_browser')
print(type(default_brower))
print(default_brower.casefold())

# casefold() string method is used to implement caseless string matching. i.e ignore cases when comparing.
if default_brower.casefold() == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif default_brower.casefold() == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif default_brower.casefold() == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif default_brower.casefold() == "ie":
    driver = webdriver.Ie(IEDriverManager().install())
else:
    print("Browser is not mentioned properly")
driver.maximize_window()

time.sleep(5)