from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options, service=Service("D:\chromedriver_win32\\chromedriver.exe"))


# Open website
driver.get("https://allegro.pl/")
driver.implicitly_wait(5)
# Accept cookies
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='mgn2_14 mp0t_0a m9qz_yp mp7g_oh mse2_40 mqu1_40 mtsp_ib mli8_k4 mp4t_0 m3h2_0 munh_0 m911_5r mefy_5r mnyp_5r mdwl_5r msbw_2 mldj_2 mtag_2 mm2b_2 mqvr_2 msa3_z4 mqen_m6 meqh_en m0qj_5r msts_n7 mh36_16 mvrt_16 mg9e_0 mj7a_0 mjir_sv m2ha_2 m8qd_qh mjt1_n2 b1vf8 mgmw_vz mrmn_qo mrhf_u8 m31c_kb m0ux_fp b14n2 mjru_k4 _158e2_4-oWM mryx_0 mryx_24_x m7er_0k']"))).click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='mgn2_14 mp0t_0a m9qz_yp mp7g_oh mse2_40 mqu1_40 mtsp_ib mli8_k4 mp4t_0 m3h2_0 munh_0 m911_5r mefy_5r mnyp_5r mdwl_5r msbw_2 mldj_2 mtag_2 mm2b_2 mqvr_2 msa3_z4 mqen_m6 meqh_en m0qj_5r msts_n7 mh36_16 mvrt_16 mg9e_0 mj7a_0 mjir_sv m2ha_2 m8qd_qh mjt1_n2 b1vf8 mgmw_vz mrmn_qo mrhf_u8 m31c_kb m0ux_fp b14n2 m7er_0k m7er_56_s mjru_k4 mryx_0 _158e2_4-oWM']"))).click()
# Click on search bar and enter 'Monitor'
driver.find_element(By.XPATH, "//input[@placeholder='czego szukasz?']").send_keys("Monitor")
time.sleep(2)
# Find the proposed text "Monitory" and click
suggestions = driver.find_elements(By.XPATH, "//div[@id='suggestions-listbox']/a/div/div")
for suggestion in suggestions:
    if suggestion.text == "Monitory":
        suggestion.click()
        break
# Assertion to check if correct page is displayed
assert "Monitory" in driver.find_element(By.XPATH, "//h1").text
# Sort by popularity
driver.find_element(By.ID, "allegro.listing.sort").click()
driver.find_element(By.CSS_SELECTOR, "option[value='qd']").click()
time.sleep(2)
# Open product details page
driver.find_element(By.XPATH, "//body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/section[2]/article[1]/div[1]/div[1]/div[2]").click()
# Add product to cart
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
# Go to the cart
driver.find_element(By.XPATH, "//a[contains(text(),'idź do koszyka')]").click()
time.sleep(1)
# Changing number of products to 3
amountOfProducts = driver.find_element(By.XPATH,"//input[@data-box-name='number-picker']")
amountOfProducts.send_keys(Keys.BACKSPACE)
amountOfProducts.send_keys("3")
# Checking that change is correct
assert "3" in driver.find_element(By.XPATH,"//input[@data-box-name='number-picker']").get_attribute("value")
time.sleep(2)
# Click on "DOSTAWA I PŁATNOŚĆ" buttom
driver.find_element(By.CSS_SELECTOR, "button[class='b1vwg b11ha m7er_k4']").click()
# Go back to "Product Listing Page"
driver.back()
driver.back()
driver.back()
# Open cart
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//img[@alt='Koszyk']")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[@class='mgn2_14 mp0t_0a m9qz_yp mp7g_oh mse2_40 mqu1_40 mtsp_ib mli8_k4 mp4t_0 m3h2_0 mryx_0 munh_0 m911_5r mefy_5r mnyp_5r mdwl_5r msbw_2 mldj_2 mtag_2 mm2b_2 mqvr_2 msa3_z4 mqen_m6 meqh_en m0qj_5r mh36_16 mvrt_16 mg9e_0 mj7a_0 mjir_sv m2ha_2 m8qd_qh mjt1_n2 blgl9 mgmw_9u msts_enp mrmn_qo mrhf_u8 m31c_kb m0ux_fp b1jc1 _5537a_qx-4y']")).click().perform()





