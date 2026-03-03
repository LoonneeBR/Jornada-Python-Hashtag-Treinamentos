
import pyautogui
import time
import pandas


pyautogui.PAUSE = 0.5

#variaveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
id = "guilherme.treinamentos@hashtag.com"
senha = "1234bacate"
tabela = pandas.read_csv("produtos.csv")

# Passo 1: Abrir Site do sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Realizar Login no Sistema
pyautogui.click(x=532, y=380)
pyautogui.write(id)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
# Passo 3: Abrir base de dados

print(tabela)

# Passo 4: Cadastrar Produto
for linha in tabela.index:
    pyautogui.click(x=430, y=255)

    #codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)
# Passo 5: Repetir passo 3 até cadatrar todos produtos


