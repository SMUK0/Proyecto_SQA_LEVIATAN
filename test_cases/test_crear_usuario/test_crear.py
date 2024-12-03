from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
class TestInterfaz:
   
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
        botonUsuario = self.driver.find_element(By.XPATH, "//li//span[text()='Usuarios']")
        botonUsuario.click()
        time.sleep(2)
        botonAgregar = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-4 mb-4']")
        botonAgregar.click()
        time.sleep(2)
        
        nombre=self.driver.find_element(By.XPATH,"//input[@id='nombre']")
        nombre.send_keys("Juan")
        time.sleep(2)
        apellido=self.driver.find_element(By.XPATH,"//input[@id='apellido']")
        apellido.send_keys("Alcachofa")
        time.sleep(2)
        password=self.driver.find_element(By.XPATH,"//input[@id='password']")
        password.send_keys("E296437512c$")
        time.sleep(2)
        botonRol = self.driver.find_element(By.XPATH, "//select[@id='rol_id']")
        botonRol.click()
        time.sleep(2)
        botonPadre = self.driver.find_element(By.XPATH, "//select[@id='rol_id']//option[@value='3']")
        botonPadre.click()
        time.sleep(2)
        agregarUsuario = self.driver.find_element(By.XPATH, "//div[@class='modal-footer']//button[@class='btn btn-primary']")
        agregarUsuario.click()
        time.sleep(2)
        
        usuario_nombre = "Juan Alcachofa"
        filas = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover table-bordered']//tbody//tr")
        
        ultima_fila = filas[-1]
        
        nombre_en_tabla = ultima_fila.find_element(By.XPATH, ".//td[1]").text
        
        # Aseguramos que el nombre encontrado en la tabla coincide con el nombre ingresado
        assert nombre_en_tabla == usuario_nombre, f"ERROR: El usuario {usuario_nombre} no se encuentra en la tabla de usuarios. Se encontró: {nombre_en_tabla}"
        
        time.sleep(4)