from selenium import webdriver  
from selenium.webdriver.common.by import By  
from webdriver_manager.chrome import ChromeDriverManager  
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

    

    def test_asignacion_curso(self):
        #Login
        self.driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("juan.perez@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='sc-ivxoEo fnmODh']").click()
        time.sleep(2)
         # BOTON PARA Asignacion_curso
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Asignación de Curso')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mb-3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name = 'maestro_id']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name='maestro_id']/option[text() = 'Maria']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name = 'curso_id']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@name='curso_id']/option[text() = 'Rojo']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        time.sleep(2)
        #Agregado de maestro a curso
        actual = self.driver.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
        print("********", actual)  
        esperada = "Maestro-Curso agregado exitosamente"
        assert esperada == actual, f"ERROR, actual {actual}, esperado: {esperada}"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger btn-sm']").click()
        time.sleep(2)
        #Eliminado
        self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
        print("********", actual)  
        esperada = "Maestro-Curso eliminado exitosamente"
        assert esperada == actual, f"ERROR, actual {actual}, esperado: {esperada}"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)