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

class SerieB:

    def iniciar(self):
        self.pasta = self.interface()
        self.criar_df(self.pasta)

    def interface(self):
        interface = None
        root = tk.Tk()
        root.title("Brasileirão Série B - Estatísticas em Excel")
        root.geometry("500x250")
        root.configure(bg="#1e1e1e")

        def on_close():
            print("A janela foi fechada. O programa será encerrado.")
            sys.exit()

        def select():
            directory = filedialog.askdirectory()
            if directory:
                print("Diretório selecionado:", directory)
                root.destroy()
                return directory
            else:
                print("Nenhum diretório selecionado. O programa será encerrado.")
                sys.exit()
        return select()

        label = ttk.Label(root, text="Selecione um diretório", background="#1e1e1e", foreground="white", font=("Helvetica", 16))
        label.pack(pady=20)

        button = ttk.Button(root, text="Selecionar", command=select)
        button.pack(pady=10)

        root.protocol("WM_DELETE_WINDOW", on_close)

        root.mainloop()

        if __name__ == "__main__":
            selected_directory = directory
            print("Diretório selecionado:", selected_directory)

    def criar_df(self, diretorio):
        if __name__ == "__main__":
            ##Configuracao do Webdriver
            chrome_driver_path = r"C:\Users\MSI\Desktop\Chrome Driver\chromedriver.exe"
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome()

            #Site
            driver.get(r"https://fbref.com/pt/comps/38/Serie-B-Estatisticas")
            wait = WebDriverWait(driver, 10)
            element = wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "a")))
            df = pd.DataFrame()

            #Glossario
            classi = '//*[@id="switcher_results2024381"]'
            stats = '//*[@id="div_stats_squads_standard_for"]'
            defend = '//*[@id="switcher_stats_squads_keeper"]'
            chutes = '//*[@id="switcher_stats_squads_shooting"]'
            tempo = '//*[@id="switcher_stats_squads_playing_time"]'
            cartoes = '//*[@id="switcher_stats_squads_misc"]'

            #Classificacao
            classificacao = driver.find_element(By.XPATH, classi)
            html = classificacao.get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table), header=None)[0]
            print(f"Tabela criada no local {diretorio}")
            df.to_excel(fr"{diretorio}\Serie B - Classificacao.xlsx")

            #Estatistica
            estatistica = driver.find_element(By.XPATH, stats)
            html2 = estatistica.get_attribute('innerHTML')
            soup2 = BeautifulSoup(html2, 'html.parser')
            table2 = soup2.find('table')
            df2 = pd.read_html(str(table2), header=None)[0]
            print(f"Tabela criada no local {diretorio}")
            df2.to_excel(fr"{diretorio}\Serie B - Estatistica.xlsx")

            #Defesas
            defesas = driver.find_element(By.XPATH, defend)
            html3 = defesas.get_attribute('innerHTML')
            soup3 = BeautifulSoup(html3, 'html.parser')
            table3 = soup3.find('table')
            df3 = pd.read_html(str(table3), header=None)[0]
            print(f"Tabela criada no local {diretorio}")
            df3.to_excel(fr"{diretorio}\Serie B - Defesas.xlsx")

            #Chutes
            chute = driver.find_element(By.XPATH, chutes)
            html4 = chute.get_attribute('innerHTML')
            soup4 = BeautifulSoup(html4, 'html.parser')
            table4 = soup4.find('table')
            df4 = pd.read_html(str(table4), header=None)[0]
            print(f"Tabela criada no local {diretorio}")
            df4.to_excel(fr"{diretorio}\Serie B - Chutes.xlsx")

            #Tempo
            tempojogo = driver.find_element(By.XPATH, tempo)
            html5 = tempojogo.get_attribute('innerHTML')
            soup5 = BeautifulSoup(html5, 'html.parser')
            table5 = soup5.find('table')
            df5 = pd.read_html(str(table5), header=None)[0]
            print(f"Tabela criada no local {diretorio}")
            df5.to_excel(fr"{diretorio}\Serie B - Tempo.xlsx")

            #Cartoes
            card = driver.find_element(By.XPATH, cartoes)
            html6 = card.get_attribute('innerHTML')
            soup6 = BeautifulSoup(html6, 'html.parser')
            table6 = soup6.find('table')
            df6 = pd.read_html(str(table6), header=None)[0]
            print(f"Tabela criada no local {diretorio}")
            df6.to_excel(fr"{diretorio}\Serie B - Cartoes.xlsx")

            # fechar
            time.sleep(1)
            print(f"Todos os arquivos salvos no diretório: {diretorio}")
            driver.quit()

start = SerieB()
start.iniciar()
