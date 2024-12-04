# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestInterfazPadres:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/login')
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_notas_modulo(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("carlos.lopez@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Notas')]").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Notas')]").text
        esperada = "Notas de los Estudiantes"
        assert esperada in actual, f"ERROR, actual: {actual}, esperado: {esperada}"
        print(f"actual: {actual}, esperado: {esperada}")
        self.driver.find_element(By.XPATH, "//select[@id = 'materia']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@id = 'materia']").click()

        for i in range(1,6):
            self.driver.find_element(By.XPATH, f"//select[@id = 'materia']//option[{i}]").click()
            time.sleep(2)
    
    def test_estadisticas_modulo(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("carlos.lopez@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Estadísticas')]").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Estadísticas')]").text
        esperada = "Estadísticas de los Estudiantes"
        assert esperada in actual, f"ERROR, actual: {actual}, esperado: {esperada}"
        print(f"actual: {actual}, esperado: {esperada}")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Entrenar')]").click()
        time.sleep(7)
        actual = self.driver.find_element(By.XPATH, "//div[@class = 'Toastify__toast Toastify__toast-theme--light Toastify__toast--success']").text
        esperada = "Modelo entrenado exitosamente."
        assert esperada in actual, f"ERROR, actual: {actual}, esperado: {esperada}"
        print(f"actual: {actual}, esperado: {esperada}")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Generar')]").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH, "//h4[contains(text(),'Ciencias')]").text
        esperada = "Ciencias Naturales"
        assert esperada in actual, f"ERROR, actual: {actual}, esperado: {esperada}"
        print(f"actual: {actual}, esperado: {esperada}")
        






