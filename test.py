import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#Enter your path to chromedriver
ser = Service(executable_path="your/path/to/chromedriver")
driver = webdriver.Chrome(chrome_options=opt, service=ser)

#Change data
id_zoom_conf_1 = "1234567890"
passwd_zoom_conf_1 = "Keo3U0JrYOURPASSWORDjVNU21BZz09"
nickname_zoom_conf_1 = "Jim Jim"

#Change data
email_google_meet_1 = "your@email.com"
passwd_google_meet_1 = "passWoR*D!1"
link_google_meet_1 = "https://meet.google.com/your-link"

def zoom_template_1():   
    #Start the window
    driver.maximize_window()
    driver.get(f'https://zoom.us/wc/{id_zoom_conf_1}/join?')
    time.sleep(10)
    
    #Entering conference passwd
    passwd_zoom = driver.find_element(By.XPATH, '//*[@type="password"]')
    passwd_zoom.clear()
    passwd_zoom.send_keys(passwd_zoom_conf_1)
    time.sleep(2)
    
    #Entering nickname
    name_zoom = driver.find_element(By.XPATH, '//*[@type="text"]')
    name_zoom.clear
    name_zoom.send_keys(nickname_zoom_conf_1)
    time.sleep(2)
    
    #Entering the conference
    name_zoom.send_keys(Keys.ENTER)
    
def google_meet__template_1():
    #Start the window
    driver.maximize_window()
    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-637459560%3A1682357100161121&continue=https%3A%2F%2Fclassroom.google.com&ifkv=AQMjQ7QT_f_kZwvAWH_s94pG6Nqj3PFRL_7aUZMqdCKfWvtdgi0xBaSZqXxUDLPQpOI3SksRMK0a&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin")    
   
    #Email filling
    time.sleep(5)
    email_gc = driver.find_element(By.XPATH,'//*[@type="email"]')
    email_gc.clear()
    email_gc.send_keys(email_google_meet_1)
    email_gc.send_keys(Keys.ENTER)
    time.sleep(2)

    #Passwd filling
    passwd_gc = driver.find_element(By.XPATH,'//*[@type="password"]')
    passwd_gc.clear()
    passwd_gc.send_keys(passwd_google_meet_1)
    passwd_gc.send_keys(Keys.ENTER)
    time.sleep(10)

    #Off mic
    driver.get(link_google_meet_1)
    time.sleep(10)
    micro_off=driver.find_element(By.CLASS_NAME, "dP0OSd")
    micro_off.click()
    time.sleep(5)
    #Off cam
    cam_off=driver.find_element(By.CLASS_NAME, "GOH7Zb")
    cam_off.click()
    time.sleep(5)
    
    #connect
    connet_meet=driver.find_element(By.XPATH, "//span[text()='Join']") #"//span[text()='Присоединиться']"
    connet_meet.click()
    
   
try:
    zoom_template_1()
    
    # #Waiting time 5400 sec - 90 minutes
    time.sleep(5400)
    
    google_meet__template_1()    
    
    #Waiting time 5400 sec - 90 minutes
    time.sleep(5400)
    
    
except Exception as ex:
    #Print exeptions
    print(ex)

finally:
    driver.close()
    driver.quit()
    
