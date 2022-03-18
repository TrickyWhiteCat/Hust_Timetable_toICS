from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_ms(driver, username, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i0116'))).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '#idSIButton9').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordInput'))).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#submitButton').click()
    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#idSIButton9'))).click()
    except:
        """"""


def login_ctt(driver, username, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userNameInput'))).send_keys(username)
    driver.find_element(By.ID, 'nextButton').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Password'))).send_keys(password)
    driver.find_element(By.ID, 'submitButton').click()

def main():
    print('¯\_(ツ)_/¯')

if __name__ == '__main__':
    main()