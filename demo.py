from selenium.webdriver import Chrome, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.amazon.in/")
search_Mob = driver.find_element_by_id("twotabsearchtextbox").send_keys("Mobiles")

#Reason for putting static wait as to see the indexing (only for viewing purpose), we have to remove it for real time scenarios.
time.sleep(5)


# #Approach 1 : via the list
# Where we have to click 4th Element only
# Reason of putting the index as 5:
#   - Indexing start from 1
#   - at index 2, we have one suggestion as 'electronics'

#saving the results in list
auto_suggestion_list = driver.find_elements_by_xpath("//div[@id='suggestions-template']//div")

# printing the value which we are clicking
print(auto_suggestion_list[5].text)
auto_suggestion_list[5].click()


#Approach 2 : via Mouse hover
# autosearch = driver.find_element_by_xpath("//div[@id = 'issDiv4']/span[contains(text(),'under 20000 rupees')]")
#
# mouse_hower = ActionChains(driver)
# mouse_hower.move_to_element(autosearch).click()
# mouse_hower.perform()


driver.close()






