#import chrome webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
global driver

driver = webdriver.Chrome("C:/Users/vedan/Desktop/chromedriver.exe")
ans=""
driver.get("https://linkedin.com/uas/login")

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("vedantk.kulkarni.cd.mec19@itbhu.ac.in")

pword = driver.find_element(By.ID, "password")
pword.send_keys("Mohak!23")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

profile_urls = ["https://www.linkedin.com/in/pranjali-gupta-36b12b1b4/"]#["https://www.linkedin.com/in/devika-mathur-0a6b4022/","https://www.linkedin.com/in/bibs92/","https://www.linkedin.com/in/puja-kaul-16363059/","https://www.linkedin.com/in/sarvamangala-gupta-601466188/","https://www.linkedin.com/in/amrita-singh-875ba463/","https://www.linkedin.com/in/raveena-singh-a687114b/","https://www.linkedin.com/in/soumyagupta1/","https://www.linkedin.com/in/arooshibajaj/","https://www.linkedin.com/in/ajay-immanuel-00a79b94/","https://www.linkedin.com/in/ravi-singh-0b607062/"]


ans=""
for profile_url in profile_urls:  
    
    #personalinfo
    
    driver.get(profile_url)

    start = time.time()

    initialScroll = 0
    finalScroll = 1000

   

    src = driver.page_source
    
    soup = BeautifulSoup(src,  "html.parser")
        
    
    intro = soup.find('div', {'class': 'mt2 relative'})
    
    
    
    name_loc = intro.find("h1")
    name=name_loc.get_text().strip()
    works_at_loc = intro.find("div", {'class': 'text-body-medium'})
    works_at = works_at_loc.get_text().strip()
    location_loc = intro.find_all("span", {'class': 'text-body-small'})
    location = location_loc[1].get_text().strip()
    str1="\nName -->"+name
    str2="\nWorks At -->"+works_at
    str3="\nLocation -->"+location
    L=str1+str2+str3+"\n Skills \n"
    print(L)
    
    
##SKILLS
    
    driver.get(profile_url+"details/skills/")

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

    

    arr=[]
    location_loc = soup.find_all("span", {'class': 'mr1 t-bold'})
    
    for i in location_loc:
        skl=i.find("span",{'aria-hidden':'true'})
        arr.append(skl.get_text().strip())
    
    arr=list(set(arr))   
    
    for i in arr:
        L+="\n"+i
    ans+="\n"+L  
    
#ConnectRequest
    
    driver.get(profile_url)
    
    #src=driver.page_source
    
    #soup = BeautifulSoup(src,  "html.parser")
    
    all_buttons = driver.find_elements(By.TAG_NAME,"button")
    connect_button = [btn for btn in all_buttons if btn.text == "Connect" ]
    connect_button[0].click()
    all_buttons = driver.find_elements(By.TAG_NAME,"button")
    connect_button = [btn for btn in all_buttons if btn.text == "Add a note" ]
    connect_button[0].click()
    msg="Hey"
    eleid=driver.find_element(By.ID,'custom-message')
    eleid.send_keys(msg)
    all_buttons = driver.find_elements(By.TAG_NAME,"button")
    connect_button = [btn for btn in all_buttons if btn.text == "Send" ]
    connect_button[0].click()
    
print(ans)    
    
file1=open("data.txt","a")
file1.write(ans)
file1.close()    


