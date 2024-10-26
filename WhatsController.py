from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_service = Service("./chromedriver-win32/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)


driver.get("https://web.whatsapp.com")

input("Escaneie o QR Code e pressione Enter para continuar...")

grupo_nome = "Lançamentos teste"
novo_nome_grupo = "teste"

try:
    grupo = driver.find_element(By.XPATH, f"//span[@title='{grupo_nome}']")
    grupo.click()
    time.sleep(2)
    
    menu_info_grupo = driver.find_element(By.XPATH, "//header//div[@role='button']")
    menu_info_grupo.click()
    time.sleep(2)

    campo_nome_grupo = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    campo_nome_grupo.click()

    campo_nome_grupo.clear()
    campo_nome_grupo.send_keys(novo_nome_grupo)
    
    campo_nome_grupo.send_keys(u'\ue007')  
    print("Nome do grupo alterado com sucesso!")
    
except Exception as e:
    print("Erro ao tentar alterar o nome do grupo:", e)

time.sleep(5)
driver.quit()
