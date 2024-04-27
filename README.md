Projeto pessoal para a criação de arquivos em Excel sobrre a Série B do Campeonato Brasileiro

Para usá-lo, você precisa:

1) Instalar o WebDriver Chrome referente à versão do seu Google Chrome (o que utilizei foi a versão 124.0)
2) Gostar de futebol e estatística :)

Site onde estou usando o WebScrapping: https://fbref.com/pt/comps/38/Serie-B-Estatisticas

Bibliotecas Python utilizadas no código:
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import sys

A junção de todas elas denotam um uso eficiente de recursos, ajudando à evitar bugs e pegando os dados da maneira mais precisa possível. 
O projeto segue em andamento, onde desejo automatizar a raspagem de dados e demonstrá-lo visualmente. 

