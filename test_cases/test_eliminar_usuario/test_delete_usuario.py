from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestDelete:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
       
        botonInicio = self.driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']")
        botonInicio.click()
        time.sleep(2)
        
        correo = self.driver.find_element(By.XPATH, "//input[@id='email']")
        correo.send_keys("juan.perez@gmail.com")
        
        contrasena = self.driver.find_element(By.XPATH, "//input[@id='password']")
        contrasena.send_keys("pass123")
        
        botonIniciar = self.driver.find_element(By.XPATH, "//button[@class='sc-ivxoEo fnmODh']")
        botonIniciar.click()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_verify_contenido_inicio(self):
        botonUsuario = self.driver.find_element(By.XPATH, "//li//span[text()='Usuarios']")
        botonUsuario.click()
        time.sleep(4)
        
        botonEliminar = self.driver.find_element(By.XPATH, "//td[text()='ja5695@example.com']/following-sibling::td//button[contains(@class, 'btn-danger')]")
        botonEliminar.click()
        time.sleep(2)

        confirmar = self.driver.find_element(By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm swal2-styled']")
        confirmar.click()
        time.sleep(2)

        
        filas_actualizadas = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover table-bordered']//tbody//tr")
        assert len(filas_actualizadas) == 3, "La fila no fue eliminada correctamente."
