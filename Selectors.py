import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome()

with Chrome() as driver:
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    url = driver.current_url
    title = driver.title
    print(title)
    print(url)

    departments = driver.find_element_by_id("block_top_menu")
    women_department = driver.find_element_by_class_name("sf-with-ul").click()
    time.sleep(3)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]/img")).perform()
    time.sleep(3)
    dress_name = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]/img").click()
    print(dress_name)

