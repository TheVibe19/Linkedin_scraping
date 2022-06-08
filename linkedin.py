#import chrome webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
global driver
driver = webdriver.Chrome("C:/Users/vedan/Desktop/chromedriver.exe")

driver.get("https://linkedin.com/uas/login")

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("vedantk.kulkarni.cd.mec19@itbhu.ac.in")

pword = driver.find_element(By.ID, "password")
pword.send_keys("Mohak!23")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

profile_urls = ["https://www.linkedin.com/in/vecha-sumanth/","https://www.linkedin.com/in/vasu-goyal-b3b252153/","https://www.linkedin.com/in/shyam-rathod-424308238/"]
for profile_url in profile_urls:  
    driver.get(profile_url)

    start = time.time()

    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll=finalScroll
        finalScroll+=1000
        time.sleep(5)
        end=time.time()

        if round(end-start)>20:
            break


    src = driver.page_source
    
    soup = BeautifulSoup(src,  "html.parser")

    intro = soup.find('div', {'class': 'mt2 relative'})

    name_loc = intro.find("h1")
    name=name_loc.get_text().strip()
    works_at_loc = intro.find("div", {'class': 'text-body-medium'})
    works_at = works_at_loc.get_text().strip()
    location_loc = intro.find_all("span", {'class': 'text-body-small'})
    location = location_loc[1].get_text().strip()
    str1="Name -->"+name
    str2="\nWorks At -->"+works_at
    str3="\nLocation -->"+location
    file1=open("data.txt","a")
    L=str1+str2+str3
    file1.write(L)
    file1.close()

    print("Name -->", name,
        "\nWorks At -->", works_at,
        "\nLocation -->", location)

