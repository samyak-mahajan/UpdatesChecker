from selenium.webdriver import Edge
from moodlechecker import *
"""We are importing selenium modules functions for Edge .You can use your preferred browser ,just read the configuration file for detailed instructions"""
PATH='C:/WebDriver/bin/msedgedriver.exe'
##Edge(executable_path=PATH) make sure you give PATH as an argument!
driver=Edge(executable_path=PATH)

moodle_login()
