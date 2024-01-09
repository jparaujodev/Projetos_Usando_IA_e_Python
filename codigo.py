import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.8

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press('enter')

pyautogui.moveTo(x=1223, y=439)

pyautogui.click(clicks=2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press('enter')

#pyautogui.moveTo(x=1320, y=79)

#pyautogui.click(clicks=1)

pyautogui.moveTo(x=805, y=411)

pyautogui.click(clicks=2)

pyautogui.write("jparaujo@gmail.com")

pyautogui.press("tab")

pyautogui.write("12345")

pyautogui.press("tab")

pyautogui.press("enter")

pyautogui.press("esc")

#Pega a tabela com o panda e lê
tabela = pandas.read_csv("produtos.csv")

print(tabela)

#utilizamos o for para que ele pegue cada linha da tabela e repita o mesmo processo de cadastramento
for linha in tabela.index:

    pyautogui.moveTo(x=768, y=299)
    pyautogui.click(clicks=1)
    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"]) #or (str(1))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) #or (str(25.95))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"])) #or (str(6.5))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    #enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

