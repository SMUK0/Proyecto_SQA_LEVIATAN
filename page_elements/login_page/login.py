# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestInterfaz:

    def test_login_administrador_positivo(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("juan.perez@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH, "//div[@class= 'Toastify__toast Toastify__toast-theme--light Toastify__toast--success']").text
        esperada = "Inicio de sesión exitoso!"
        assert esperada in actual, f"ERROR, actual: {actual}, esperado: {esperada}"
        print(f"actual: {actual}, esperado: {esperada}")