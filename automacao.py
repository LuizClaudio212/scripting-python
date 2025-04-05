from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_sigaa(usuario, senha):
    try:
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://sigaa.ifal.edu.br/sigaa/verTelaLogin.do")
        driver.maximize_window()

        time.sleep(3)

        driver.find_element(By.NAME, "user.login").send_keys(usuario)
        driver.find_element(By.NAME, "user.senha").send_keys(senha)
        driver.find_element(By.XPATH, '//input[@type="submit" and @value="Entrar"]').click()

        return "Login realizado com sucesso!"
    
    except Exception as e:
        return f"Erro: {e}"