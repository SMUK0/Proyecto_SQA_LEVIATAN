from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1:8000/')
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='sc-dntaoT cwKVBc']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("maria.garcia@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("pass123")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='sc-ivxoEo fnmODh']").click()
time.sleep(2)
# BOTON PARA ASISTENCIAS
driver.find_element(By.XPATH, "//span[contains(text(),'Asistencias')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//select[@class='form-select']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//select[@class='form-select']").click()
time.sleep(2)
# driver.find_element(By.XPATH, "//select[@id='cursoSelect']/option[text() = 'Rojo - Primero']").click()
#time.sleep(2)
#driver.find_element(By.XPATH, "//button[contains(text(),'Marcar Todos como Presentes')]").click()
#time.sleep(2)
#driver.find_element(By.XPATH, "//button[contains(text(),'Marcar Todos como Ausentes')]").click()
#time.sleep(2)
#driver.find_element(By.XPATH, "//button[contains(text(),'Marcar Todos como Tarde')]").click()
#time.sleep(2)
# BOTON PARA UNA ASISTENCIA DE ESTUDIANTE - INDIVIDUAL
#driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Asistencia')]").click()
#time.sleep(2)








# BOTON PARA NOTAS
driver.find_element(By.XPATH, "//span[contains(text(),'Notas')]").click()
time.sleep(2)
# BOTON PARA NOTIFICACIONES
driver.find_element(By.XPATH, "//span[contains(text(),'Notificaciones')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-primary mb-3']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//select[@name='estudiante_id']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@name='mensaje']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(2)
