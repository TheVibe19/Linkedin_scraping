from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

#Login into LinkedIn account
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

#ADD the names of the companies to the list
Company_names=["meta","microsoft"]

for name in Company_names: 
    #Get details about the company
    driver.get("https://www.linkedin.com/company/"+name+"/about/")
    start = time.time()

    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll=finalScroll
        finalScroll+=1000
        time.sleep(5)
        end=time.time()

        if round(end-start)>5:
            break


    src = driver.page_source
    
    soup = BeautifulSoup(src,  "html.parser")
    intro = soup.find('dl', {'class': 'overflow-hidden'})
    
    About="About"+name+"\n"+intro.get_text().strip();
    file1=open("CompanyData.txt","a")
    file1.write("\n"+About+"\n\n")
    file1.close()  

    #GET THE CEOS OF THE COMPANY

    driver.get("https://www.google.com/search?q=ceo+of+"+name+"&rlz=1C1GCEA_enIN976IN976&oq=ceo+of+visa&aqs=chrome.0.69i59j0i512l3j69i60l4.1521j1j7&sourceid=chrome&ie=UTF-8")
    
    start = time.time()

    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll=finalScroll
        finalScroll+=1000
        time.sleep(5)
        end=time.time()

        if round(end-start)>1:
            break
            
    src = driver.page_source
    
    soup = BeautifulSoup(src,  "html.parser")   
    ceo = soup.find('div', {'class': 'Z0LcW'})
    CEO_NAME=""
    if ceo==None:
        ceo1=soup.find('div', {'class': 'LGOjhe'})
        CEO_NAME = (ceo1.get_text().strip())
        
    else:
        CEO_NAME = (ceo.get_text().strip())
        
    file1=open("CompanyData.txt","a")
    file1.write("\n"+"CEO of "+name+" is "+CEO_NAME+"\n\n")
    file1.close()  
    
    #Founders of the Company

    driver.get("https://www.google.com/search?q=founder+of+"+name+"&rlz=1C1GCEA_enIN976IN976&oq=ceo+of+visa&aqs=chrome.0.69i59j0i512l3j69i60l4.1521j1j7&sourceid=chrome&ie=UTF-8")
    
    start = time.time()

    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll=finalScroll
        finalScroll+=1000
        time.sleep(5)
        end=time.time()

        if round(end-start)>1:
            break
            
    src = driver.page_source
    
    soup = BeautifulSoup(src,  "html.parser")   
    founder = soup.find('div', {'class': 'EDblX DAVP1'})
    Founders=""
    if(founder==None):
        Founders="Not found, CEO is "+CEO_NAME
    else:
        Founders=founder.get_text().strip()
        
    file1=open("CompanyData.txt","a")
    file1.write("\n Founders: "+Founders+"\n\n")
    file1.close()   



    #Get the Employees of the Company that you may know

    driver.get("https://www.linkedin.com/company/"+name+"/people/")
    start = time.time()

    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        initialScroll=finalScroll
        finalScroll+=1000
        time.sleep(5)
        end=time.time()

        if round(end-start)>5:
            break


    src = driver.page_source
    
    soup = BeautifulSoup(src,  "html.parser")
    intro = soup.find('div', {'class': 'artdeco-card pv5 pl5 pr1 mt4'})
    profs=intro.find_all("div", {'class': 'org-people-profile-card__profile-title t-black lt-line-clamp lt-line-clamp--single-line ember-view'})
    profs_pos=intro.find_all("div", {'class': 'lt-line-clamp lt-line-clamp--multi-line ember-view'})
    Employee=""
    for i in range(len(profs)):
        Employee+="\n"+profs[i].get_text().strip()
        Employee+="\n"+profs_pos[i].get_text().strip()+"\n"

    file1=open("CompanyData.txt","a")
    file1.write("Employess of the Company You may Know: \n"+Employee+"\n\n\n\n\n\n")
    file1.close()      
        
    