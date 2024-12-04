from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestMateria:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(2)
       
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
        
            botonMaterias = self.driver.find_element(By.XPATH, "//li//span[text()='Materias']")
            botonMaterias.click()
            time.sleep(3)
            
            nombre_materia = "Historia"
            
            botonEditar = self.driver.find_element(By.XPATH, f"//td[text()='{nombre_materia}']/following-sibling::td//button[contains(@class, 'btn-warning')]")
            botonEditar.click()
            time.sleep(2)
            
            nombre = self.driver.find_element(By.XPATH, "//input[@name='nombre']")
            nuevo_nombre = "Física Avanzada"
            nombre.clear()  
            nombre.send_keys(nuevo_nombre)
            time.sleep(2)
            
            botonGuardar = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
            botonGuardar.click()
            time.sleep(3)
            
            materias = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover table-bordered']//tbody//tr//td[1]")
            nombres_materias = [materia.text for materia in materias]
            
            assert nuevo_nombre in nombres_materias, f"La materia '{nuevo_nombre}' no se actualizó correctamente."
            
            
        
        
        