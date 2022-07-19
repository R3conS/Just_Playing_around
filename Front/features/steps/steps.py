from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from behave import *



DRIVER_PATH = 'C:/Users/Megaport/Desktop/Qa analysis/Driver/chromedriver.exe'
driver      = webdriver.Chrome(executable_path= DRIVER_PATH)
MAX_DELAY   = 3  # seconds
INDEX_URL   = 'https://www.ornikar.com/'
CODE_URL    = 'https://www.ornikar.com/code'
PERMISB_URL = 'https://www.ornikar.com/permis'

@given("I'm in /assurance-auto")
def step_impl(context):
    driver.get('https://www.ornikar.com/assurance-auto')
    
@When("I Click on the logo")
def step_imt(context):
    xpath_logo = '/html/body/div[1]/div/div[1]/div/div/div/header/div/a'
    try:
        WebDriverWait(driver, MAX_DELAY).until(EC.presence_of_element_located((By.XPATH, xpath_logo)))
        logo = driver.find_element( "xpath", xpath_logo )
        logo.click()
    except:
        assert False
        
@Then("It should redirect me to the / page")
def step_imt(context):
    current_url = driver.current_url
    assert current_url == INDEX_URL
  
    
@When("I Click on the Code de la route text")
def step_imt(context):
    xpath_Code_de_la_route_text = '//*[@id="__next"]/div/div[1]/div/div/div/header/div/nav/a[1]'
    try:
        WebDriverWait(driver, MAX_DELAY).until(EC.presence_of_element_located((By.XPATH, xpath_Code_de_la_route_text)))
        code_de_la_route_txt = driver.find_element( "xpath", xpath_Code_de_la_route_text )
        code_de_la_route_txt.click()
    except:
        assert False
        
@Then("It should redirect me to the /code page")
def step_imt(context):
    current_url = driver.current_url
    assert current_url == CODE_URL

#################################################################################################################################################
    
@When("I Hover on the Permis de conduire text")
def step_imt(context):
    xpath_Code_de_la_route_text = '//*[@id="__next"]/div/div[1]/div/div/div/header/div/nav/div[1]/div'
    
    try:
        WebDriverWait(driver, MAX_DELAY).until(EC.presence_of_element_located((By.XPATH, xpath_Code_de_la_route_text)))
        permis_conduire_text = driver.find_element( "xpath", xpath_Code_de_la_route_text )
        hover_on_permisdeconduire = ActionChains(driver).move_to_element(permis_conduire_text)
        hover_on_permisdeconduire.perform()
        
    except:
        assert False
        
@Then("It should open a drop items")
def step_imt(context):
    permisB_item_xpath = '//*[@id="__next"]/div/div[1]/div/div/div/header/div/nav/div[1]/div[2]/div[2]/div/li[1]/a'
    driver.find_element( "xpath", permisB_item_xpath )

@When("I Click on Permis B")
def step_imt(context):
    permisB_item_xpath = '//*[@id="__next"]/div/div[1]/div/div/div/header/div/nav/div[1]/div[2]/div[2]/div/li[1]/a'
    permisB_btn        = driver.find_element( "xpath", permisB_item_xpath )
    permisB_btn.click()
        
@Then("It should redirect me to /permis page")
def step_imt(context):
    current_url = driver.current_url
    assert current_url == PERMISB_URL