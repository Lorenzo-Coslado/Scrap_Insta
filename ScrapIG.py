
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass

""" Set up """
my_user = "lorenzo@coslado.fr"
my_pwd = getpass.getpass()
keyword = "war"
links=[]
i=0

""" Chemin de mon ChromeDriver """
file_driver = "C:\Program Files\Drivers\chromedriver.exe"


""" Permet de lancer mon chromium """
driver = webdriver.Chrome(file_driver)
driver.get ("https://www.instagram.com")
driver.maximize_window()
sleep(1)

""" Permet d'accepeter les cookies """
cookies = driver.find_element(By.XPATH,"//button[@class='aOOlW  bIiDR  ']")
cookies.click()
sleep(1)

""" Permet d'injecter mon identifiant """
user_name = driver.find_element(By.XPATH,"//input[@name='username']")
user_name.send_keys(my_user)
user_name.send_keys(Keys.ENTER)

""" Permet d'injecter mon mdp """
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys(my_pwd)
password.send_keys(Keys.ENTER)
sleep(5)

""" Permet de lancer ma recherche d'# avec mon keyword """
driver.get ("https://www.instagram.com/explore/tags/" + keyword)
sleep(4)

""" Permet de chercher les différents posts de la recherche """
posts = driver.find_elements(By.XPATH,"//div[@style='position: relative; display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px;']//a[@class='qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq _a6hd']")

""" Permet de remplir ma liste links avec les liens de chaque posts """
for post in posts :
    post = post.get_attribute('href')
    links.append(post)

""" Permet de scraper les différentes data page par page"""
for link in links :
    driver.get(link)
    sleep(3)
    user_account = "@" + str(driver.find_element(By.XPATH,"//a[@class='qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq _acan _acao _acat _acaw _a6hd']").text)
    description = str(driver.find_element(By.XPATH,"//span[@class='_aacl _aaco _aacu _aacx _aad7 _aade']").text)
    like = str(driver.find_element(By.XPATH,"//div[@class='_aacl _aaco _aacw _aacx _aada _aade']").text)
    image_post = str(driver.find_element(By.XPATH,"//img[@class='pytsy3co buh8m867 s8sjc6am ekq1a7f9 f14ij5to mfclru0v']").get_attribute('src'))
    i = i+1

    print("Post numéro : " + str(i) + "\n" + link + "\n" + "Compte : " + user_account + "\n" + "Description : " + description + "\n" + "Likes : " + like + "\n" + "Lien Image : " + image_post + "\n" )
