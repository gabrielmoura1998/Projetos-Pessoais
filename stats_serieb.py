import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import sys
from tkinter import ttk

class SerieB:

    def __init__(self):
        self.chrome_driver_path = ""
        self.pasta_destino = ""

    def iniciar(self):
        self.interface_inicial()

    def interface_inicial(self):
        root = tk.Tk()
        root.title("Estatísticas do Brasileirão Série B")
        root.geometry("400x200")
        root.configure(bg="#1e1e1e")

        def on_close():
            print("A janela foi fechada. O programa será encerrado.")
            sys.exit()

        def iniciar_programa():
            root.destroy()
            self.interface_selecao()

        style = ttk.Style()
        style.configure('Azure.TButton', background='#2980b9', foreground='blue', font=('Helvetica', 12, 'bold'),
                        borderwidth=0, highlightthickness=0, relief='flat', width=20, anchor='center')

        label_titulo = tk.Label(root, text="Estatísticas do Brasileirão Série B", background="#1e1e1e", foreground="white", font=("Helvetica", 16))
        label_titulo.pack(pady=20)

        button_iniciar = ttk.Button(root, text="INICIAR", command=iniciar_programa, style='Azure.TButton')
        button_iniciar.pack(pady=20)

        root.protocol("WM_DELETE_WINDOW", on_close)

        root.mainloop()

    def interface_selecao(self):
        root = tk.Tk()
        root.title("Estatísticas do Brasileirão Série B")
        root.geometry("1000x500")
        root.configure(bg="#1e1e1e")


        def on_close():
            print("A janela foi fechada. O programa será encerrado.")
            sys.exit()

        def selecionar_driver():
            driver_path = filedialog.askopenfilename(title="Selecione o Chrome Driver")
            if driver_path:
                print("Chrome Driver selecionado:", driver_path)
                self.chrome_driver_path = driver_path
            else:
                print("Nenhum Chrome Driver selecionado. O programa será encerrado.")
                sys.exit()

        def selecionar_pasta():
            pasta = filedialog.askdirectory(title="Selecione a Pasta")
            if pasta:
                print("Pasta selecionada:", pasta)
                self.pasta_destino = pasta
            else:
                print("Nenhuma pasta selecionada. O programa será encerrado.")
                sys.exit()

        style = ttk.Style()
        style.configure('Azure.TButton', background='#2980b9', foreground='blue', font=('Helvetica', 12, 'bold'),
                        borderwidth=0, highlightthickness=0, relief='flat', width=20, anchor='center')

        label = tk.Label(root, text="Você precisa selecionar o Chrome Driver e a pasta de destino! ", background="#1e1e1e", foreground="white", font=("Helvetica", 16))
        label.pack(pady=40)

        label = tk.Label(root, text="Caso não tenha o Chrome Driver, procure em: https://developer.chrome.com/docs/chromedriver?hl=pt-br", background="#1e1e1e", foreground="white", font=("Helvetica", 16))
        label.pack(pady=20)

        label = tk.Label(root, text="Obs: baixe a versão do Google Chrome que você usa, geralmente na versão 124 ou superior!", background="#1e1e1e", foreground="white", font=("Helvetica", 16))
        label.pack(pady=20)

        button_driver = tk.Button(root, text="Selecione o Chrome Driver", command=selecionar_driver, font=("Helvetica", 12, "bold"))
        button_driver.pack(pady=10)
        button_driver.configure(width=30)

        button_pasta = tk.Button(root, text="Selecione a Pasta de destino", command=selecionar_pasta, font=("Helvetica", 12, "bold"))
        button_pasta.pack(pady=10)
        button_pasta.configure(width=30)

        button_iniciar = ttk.Button(root, text="INICIAR", command=root.destroy, style='Azure.TButton')
        button_iniciar.pack(side=tk.BOTTOM, pady=20)

        root.protocol("WM_DELETE_WINDOW", on_close)

        root.mainloop()

        if self.chrome_driver_path and self.pasta_destino:
            self.criar_df()

    def criar_df(self):
        chrome_driver_path = self.chrome_driver_path
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()

        # Site
        driver.get(r"https://fbref.com/pt/comps/38/Serie-B-Estatisticas")
        wait = WebDriverWait(driver, 10)
        element = wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "a")))
        df = pd.DataFrame()

        # Glossario
        classi = '//*[@id="switcher_results2024381"]'
        stats = '//*[@id="div_stats_squads_standard_for"]'
        defend = '//*[@id="switcher_stats_squads_keeper"]'
        chutes = '//*[@id="switcher_stats_squads_shooting"]'
        tempo = '//*[@id="switcher_stats_squads_playing_time"]'
        cartoes = '//*[@id="switcher_stats_squads_misc"]'

        # Classificacao
        classificacao = driver.find_element(By.XPATH, classi)
        html = classificacao.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table), header=None)[0]
        print(f"Tabela criada no local {self.pasta_destino}")
        df.to_excel(fr"{self.pasta_destino}\Serie B - Classificacao.xlsx")

        # Estatistica
        estatistica = driver.find_element(By.XPATH, stats)
        html2 = estatistica.get_attribute('innerHTML')
        soup2 = BeautifulSoup(html2, 'html.parser')
        table2 = soup2.find('table')
        df2 = pd.read_html(str(table2), header=None)[0]
        print(f"Tabela criada no local {self.pasta_destino}")
        df2.to_excel(fr"{self.pasta_destino}\Serie B - Estatistica.xlsx")

        # Defesas
        defesas = driver.find_element(By.XPATH, defend)
        html3 = defesas.get_attribute('innerHTML')
        soup3 = BeautifulSoup(html3, 'html.parser')
        table3 = soup3.find('table')
        df3 = pd.read_html(str(table3), header=None)[0]
        print(f"Tabela criada no local {self.pasta_destino}")
        df3.to_excel(fr"{self.pasta_destino}\Serie B - Defesas.xlsx")

        # Chutes
        chute = driver.find_element(By.XPATH, chutes)
        html4 = chute.get_attribute('innerHTML')
        soup4 = BeautifulSoup(html4, 'html.parser')
        table4 = soup4.find('table')
        df4 = pd.read_html(str(table4), header=None)[0]
        print(f"Tabela criada no local {self.pasta_destino}")
        df4.to_excel(fr"{self.pasta_destino}\Serie B - Chutes.xlsx")

        # Tempo
        tempojogo = driver.find_element(By.XPATH, tempo)
        html5 = tempojogo.get_attribute('innerHTML')
        soup5 = BeautifulSoup(html5, 'html.parser')
        table5 = soup5.find('table')
        df5 = pd.read_html(str(table5), header=None)[0]
        print(f"Tabela criada no local {self.pasta_destino}")
        df5.to_excel(fr"{self.pasta_destino}\Serie B - Tempo.xlsx")

        # Cartoes
        card = driver.find_element(By.XPATH, cartoes)
        html6 = card.get_attribute('innerHTML')
        soup6 = BeautifulSoup(html6, 'html.parser')
        table6 = soup6.find('table')
        df6 = pd.read_html(str(table6), header=None)[0]
        print(f"Tabela criada no local {self.pasta_destino}")
        df6.to_excel(fr"{self.pasta_destino}\Serie B - Cartoes.xlsx")

        # fechar
        time.sleep(1)
        print(f"Todos os arquivos salvos no diretório: {self.pasta_destino}")
        driver.quit()


start = SerieB()
start.iniciar()
