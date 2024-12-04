from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestInterfaz:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
        
        time.sleep(2)
        

    def teardown_method(self):

        self.driver.quit()
        print("Prueba visual completada")

    def test_verify_contenido_inicio(self):
        botonInicio = self.driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']")
        botonInicio.click()
        time.sleep(2)
        correo=self.driver.find_element(By.XPATH, "//input[@id='email']")
        correo.send_keys("juan.perez@gmail.com")
        
        contrasena=self.driver.find_element(By.XPATH,"//input[@id='password']")
        contrasena.send_keys("pass123")
        
        botonIniciar=self.driver.find_element(By.XPATH,"//button[@class='sc-ivxoEo fnmODh']")
        botonIniciar.click()
       
        time.sleep(4)
        