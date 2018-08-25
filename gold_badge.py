import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def auto_login(driver, email, password):
    # open the login page
    driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
    # log in: email, password, click
    driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
    # selecting a field to TAB forward from
    pwd = driver.find_element_by_xpath("//input[@id='password']")
    pwd.send_keys(password)
    # trying to access the "Submit" input directly kept yielding errors
    # approach through pressing TAB enough times to access the button
    # like that seems to work fine!
    pwd.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
    return driver


if __name__ == "__main__":
    # declare path to chromedriver executable (located in same folder)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver = webdriver.Chrome('{0}/chromedriver'.format(dir_path))
    # get credentials from open-source-safe environment variables
    email = os.environ.get('SO_USR')
    password = os.environ.get('SO_PWD')
    # print(email, password)  # check whether the credentials are imported

    driver = auto_login(driver, email, password)
    # logging
    with open("gold.log", 'a') as f:
        log = "{0} : successful login\n".format(datetime.datetime.now())
        f.write(log)
