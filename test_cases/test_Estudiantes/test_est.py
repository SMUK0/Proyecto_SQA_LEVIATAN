from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
class TestEstudiantes:
   
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')
       
        botonInicio = self.driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']")
        botonInicio.click()
        time.sleep(2)
        correo=self.driver.find_element(By.XPATH, "//input[@id='email']")
        correo.send_keys("juan.perez@gmail.com")
       
        contrasena=self.driver.find_element(By.XPATH,"//input[@id='password']")
        contrasena.send_keys("pass123")
       
        botonIniciar=self.driver.find_element(By.XPATH,"//button[@class='sc-ivxoEo fnmODh']")
        botonIniciar.click()
       
        time.sleep(2)
       
 
    def teardown_method(self):
 
        self.driver.quit()
        print("Prueba visual completada")
 
    def test_verify_contenido_inicio(self):
        botonUsuario = self.driver.find_element(By.XPATH, "//li//span[text()='Estudiantes']")
        botonUsuario.click()
        time.sleep(2)
        botonAgregar = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        botonAgregar.click()
        time.sleep(2)
        
        nombreEst=self.driver.find_element(By.XPATH,"//div[@class='mb-3']//input[@name='nombre']")
        nombreEst.send_keys("Kevin")
        time.sleep(2)
        apellidoEst=self.driver.find_element(By.XPATH,"//div[@class='mb-3']//input[@name='apellido']")
        apellidoEst.send_keys("Rivera")
        time.sleep(2)
        
        fecha_nacimiento=self.driver.find_element(By.XPATH,"//div[@class='mb-3']//input[@name='fecha_nacimiento']")
        fecha_nacimiento.send_keys("11/03/2005")
        time.sleep(2)
       
        curso = self.driver.find_element(By.XPATH, "//select[@name='curso_id']//option[@value='1']")
        curso.click()
        time.sleep(2)
        agregarEst = self.driver.find_element(By.XPATH, "//div[@class='modal-footer']//button[text()='Agregar Estudiante']")
        agregarEst.click()
        
        time.sleep(3)
        
