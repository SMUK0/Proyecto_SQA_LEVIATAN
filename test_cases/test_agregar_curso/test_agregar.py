from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCurso:

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
        
        botonCursos = self.driver.find_element(By.XPATH, "//li//span[text()='Cursos']")
        botonCursos.click()
        time.sleep(3)
        
        agregar = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mb-3']")
        agregar.click()
        time.sleep(2)
        
        nombreCurso = self.driver.find_element(By.XPATH, "//input[@name='nombre']")
        nombreCurso.send_keys("gris")
        time.sleep(2)
        
        grado = self.driver.find_element(By.XPATH, "//select[@name='grado']")
        grado.click()  
        time.sleep(1)
        
        opcionGrado = self.driver.find_element(By.XPATH, "//option[text()='3er Grado']")
        opcionGrado.click()
        time.sleep(1)
        
        
        botonAgregarCurso = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        botonAgregarCurso.click()
        time.sleep(3)
        
        curso_esperado = "rosado"
        
        cursos = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover table-bordered']//tbody//tr//td[1]")
        nombres_cursos_actuales = [curso.text for curso in cursos]
        
        assert curso_esperado in nombres_cursos_actuales, f"Error: El curso '{curso_esperado}' no fue agregado correctamente. Cursos actuales: {nombres_cursos_actuales}"
            
            
                    
            
        
        
        