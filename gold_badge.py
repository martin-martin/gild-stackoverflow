import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def auto_login(driver, email, password, URL):
    driver.get(URL)
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
    logging.basicConfig(filename='gol.log',
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO,
                        )

    stackoverflow = 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f'
    URLs = {
        'gis': 'https://gis.stackexchange.com/',
        'open-data': 'https://opendata.stackexchange.com/',
        'cross-validated': 'https://stats.stackexchange.com/',
        'data-science': 'https://datascience.stackexchange.com/',
        'travel': 'https://travel.stackexchange.com/',
        'bitcoin': 'https://bitcoin.stackexchange.com/',
    }
    # declare path to chromedriver executable (located in same folder)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--headless')

    # for now, just pop in the credentials here
    email, password = 'breuss.martin@gmail.com', 'things to learn 8'

    try:
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='{0}/chromedriver'.format(dir_path))
        try:
            driver = auto_login(driver, email, password, stackoverflow)
            logging.info('Logged in @ StackOverflow')
            time.sleep(3)
        except Exception as e:
            logging.warning('FAILED Login @ SO: {0}'.format(e))
        else:
            for platform, url in URLs.items():
                try:
                    driver.get(url)
                    logging.info('Success @ {0}'.format(platform))
                except Exception as e:
                    logging.warning('Failed @ {0}: {1}'.format(platform, e))
                finally:
                    time.sleep(3)
    except Exception as e:
        logging.warning('SCRIPT FAILED: {0}'.format(e))
    finally:
        driver.quit()
