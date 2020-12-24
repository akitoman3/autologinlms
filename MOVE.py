import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start_chrome():
    # chromedriverのPATHを指定（Pythonファイルと同じフォルダの場合）
    driver_path = 'C:\Program Files (x86)\chromedriver\chromedriver.exe'

    # Chrome起動
    #driver = webdriver.Chrome(driver_path)
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window() # 画面サイズ最大化

    # ログインURL
    url = 'https://lms.gifu-nct.ac.jp/login/index.php'
    driver.get(url)

    return driver

def login_google(driver):

    #ログイン情報
    login_id = "IDいれる"
    login_pw = "PASSWORDいれる"

    #最大待機時間（秒）
    wait_time = 30

    ### IDを入力
    login_id_xpath = '//*[@id="username"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("username").send_keys(login_id)

    ### パスワードを入力
    login_pw_xpath = '//*[@id="password"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(1) # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath('//BUTTON[@type="submit"]').click()
    time.sleep(1)

    url2 = 'https://lms.gifu-nct.ac.jp/course/view.php?id=4076'
    driver.get(url2)
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="module-59760"]/div/div/div[2]/div[1]/a/span').click()
    time.sleep(1)

    driver.find_element_by_xpath('//BUTTON[@type="submit"]').click()
    time.sleep(1)

    #温度

    driver.find_element_by_xpath('//INPUT[@name="q368935:1_answer"]').send_keys("36.4")
    driver.find_element_by_xpath('//INPUT[@type="checkbox"]').click()
    driver.find_element_by_xpath('//INPUT[@name="q368935:3_answer"]').send_keys("特になし")
    time.sleep(1)

    driver.find_element_by_xpath('//INPUT[@type="submit"]').click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div[1]/div[3]/div/div/form').click()
    time.sleep(1)

    driver.find_element_by_xpath('//INPUT[@CLASS="btn btn-primary"]').click()
    time.sleep(3)
if __name__ == '__main__':
    # Chromeを起動
    driver = start_chrome()

    # ログイン
    login_google(driver)

    browser.close()
    browser.quit()
