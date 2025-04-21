import os
import time
import re 
import glob
import pandas as pd
from tkinter import filedialog,Tk
#webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#openpyxl
from openpyxl import load_workbook
#pypdf2
from PyPDF2 import PdfReader
#dotenv
from dotenv import load_dotenv

# Cargar variables
load_dotenv(dotenv_path=".variables_env") 
usuario = os.getenv("USUARIO")
password = os.getenv("PASSWORD")
url = os.getenv("PORTAL_URL")
print(f"URL: {url}")
salida = os.getenv("SALIDA")


# Ocultar ventana de Tkinter
#Tk().withdraw()

# Seleccionar archivo de entrada
#ruta_entrada = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
#ruta_salida = salida
#if not ruta_entrada:  # Si el usuario cancela, se detiene el programa
#    print("No se seleccionó ningún archivo.")
#    exit()

#print(f"Archivo seleccionado: {ruta_entrada}")

# Obtener la carpeta donde está el archivo
#carpeta_entrada = os.path.dirname(ruta_entrada)

# Obtener todos los archivos Excel en la misma carpeta
#archivos = glob.glob(os.path.join(carpeta_entrada, "*.xlsx"))
#print("Archivos en la carpeta:", archivos)

#df = pd.read_excel(ruta_entrada, header=None)


# Configurar Selenium con Chrome
url = url
driver = webdriver.Chrome()
driver.get(url)
time.sleep(15)

#funcion para ingresar usuario y contrseña de la pagina
def ingresar_datos( usuario, password):
    campo_usuario = driver.find_element(By.ID, "email")
    print(f"el usuario es : {campo_usuario}")
    campo_usuario.send_keys(usuario)

    campo_contraseña = driver.find_element(By.NAME, "password")
    print(f"el password es : {campo_contraseña}")
    campo_contraseña.send_keys(password)


    boton_login = driver.find_element(By.XPATH, '//input[@value="Iniciar Sesión"]')
    boton_login.click()

ingresar_datos( usuario, password)  

# Esperar a que el menú se cargue y hacer clic en "Facturación"
def ir_a_facturacion():
    try:
        print("Accediendo a sección de facturación...")
        time.sleep(10)  
        # hacer click en factura
        menu_facturacion = driver.find_element(By.XPATH, '//span[contains(text(), "Mis Facturas")]')
        menu_facturacion.click()

        time.sleep(5)
        # hacer click En la parte superior del lado derecho dnde se encuentran los nombres de las plantas 
        parte_superior = driver.find_element(By.CLASS_NAME, "sumistro")
        parte_superior.click()
        print("✅ Click realizado en el suministro (planta) correctamente.: {parte_superior}")
        time.sleep(5)
    except Exception as e:
        print(f"No se pudo acceder a Facturación: {e}")

ir_a_facturacion()

#descargar la factura
def descargar_factura():
    try:
        time.sleep(5)
        factura = driver.find_element(By.XPATH, '//a[contains(text(), "Descargar")]')  # Ajustar
        factura.click()
        print("Factura descargada.")
        time.sleep(3)  # esperar descarga
    except Exception as e:
        print(f"Error al descargar la factura: {e}")

#cargar el excel
def actualizar_excel(ruta_excel, datos):
    df = pd.read_excel(ruta_excel)
    nuevo_df = pd.DataFrame([datos])
    df = pd.concat([df, nuevo_df], ignore_index=True)
    df.to_excel(ruta_excel, index=False)
    print("Dashboard actualizado.")

