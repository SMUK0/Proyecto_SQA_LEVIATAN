# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestInterfaz:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/login')
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_login_administrador(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("juan.perez@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(3.5)
    
    def test_login_maestro(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("maria.garcia@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(3.5)
    
    def test_login_padre(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("carlos.lopez@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(3.5)


