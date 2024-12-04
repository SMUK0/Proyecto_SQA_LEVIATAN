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

    

    def test_asistencias(self):
        #Login
        self.driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("maria.garcia@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("pass123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='sc-ivxoEo fnmODh']").click()
        time.sleep(2)
        # BOTON PARA ASISTENCIAS
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Asistencias')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//select[@class='form-select']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@id='cursoSelect']/option[text() = 'Rojo - Primero']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Marcar Todos como Presentes')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Marcar Todos como Ausentes')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Marcar Todos como Tarde')]").click()
        time.sleep(2)
        # BOTON PARA UNA ASISTENCIA DE ESTUDIANTE - INDIVIDUAL
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Asistencia')]").click()
        time.sleep(2)
        #Confirmacion de registro de asistencias
        actual = self.driver.find_element(By.XPATH, "//div[contains(text(),'Asistencias guardadas correctamente')]").text
        print("********", actual)  
        esperada = "Asistencias guardadas correctamente"
        assert esperada == actual, f"ERROR, actual {actual}, esperado: {esperada}"



    def test_notas(self):
         #BOTON PARA NOTAS
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Notas')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@class='form-select']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@id='curso-select']/option[text() = 'Rojo - Primero']").click()
        time.sleep(2)
        #Abre desplegable
        self.driver.find_element(By.XPATH, "//select[@class='form-select']").click()
        time.sleep(2)
        #Elige materia
        self.driver.find_element(By.XPATH, "//select[@id='materia-select']/option[text() = 'Ciencias Naturales']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select[@id='tipo-select']/option[text() = 'Examen']").click()
        time.sleep(2)
        #Elige brimestre
        self.driver.find_element(By.XPATH, "//select[@id='bimestre-select']/option[@value = '1']").click()
        time.sleep(2)
    #def test_notificaciones(self):
        # BOTON PARA NOTIFICACIONES
     #   self.driver.find_element(By.XPATH, "//span[contains(text(),'Notificaciones')]").click()
      #  time.sleep(2)
       # self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary mb-3']").click()
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, "//select[@name='estudiante_id']").click()
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, "//textarea[@name='mensaje']").click()
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        #time.sleep(2)



#def test_login(self):
  #      self.driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']").click()
  #      time.sleep(2)
    #    self.driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("maria.garcia@gmail.com")
    #    time.sleep(2)
    #    self.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("pass123")
     #   time.sleep(2)
      #  self.driver.find_element(By.XPATH, "//button[@class='sc-ivxoEo fnmODh']").click()
