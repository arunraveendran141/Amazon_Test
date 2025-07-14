from time import sleep
from selenium  import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def test_search_device_on_amazon(device_name):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 30)
    short_wait = WebDriverWait(driver, 5)

    driver.get('http://amazon.in')
    wait.until(EC.visibility_of_element_located((By.ID, 'gw-card-layout')))
    print("\nHome Page Loaded")
    try:
        btn_continue_shopping = short_wait.until(EC.presence_of_element_located((By.ID, 'submit')))
        btn_continue_shopping.click()
    except:
        pass
    input_box_element = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    input_box_element.send_keys(device_name)

    btn_search = wait.until(EC.presence_of_element_located((By.ID, 'nav-search-submit-button')))
    btn_search.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@data-component-type="s-result-info-bar"]')))
    print(f"{device_name} searched and result page shown")

    iphone12_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, f'//h2[contains(@aria-label,"{device_name}")]')))
    iphone12_element[0].click()
    print("navigated to Device Page")

    price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#corePriceDisplay_desktop_feature_div span.a-price-whole')))
    print(f"Price for {device_name} : ₹{price_element.text}")


    ## cart option is not available for guest user 
    # btn_add_to_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#newAccordionRow_0 input#add-to-cart-button')))
    # btn_add_to_cart.click()

    sleep(10)
    driver.quit()

