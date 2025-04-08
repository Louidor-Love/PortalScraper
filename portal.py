import os
import time
import re 
import pandas as pd
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
load_dotenv()
usuario = os.getenv("USUARIO")
password = os.getenv("PASSWORD")
url = os.getenv("PORTAL_URL")