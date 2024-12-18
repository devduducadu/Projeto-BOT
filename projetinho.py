'''
"por onde eu começo??" MANULMENTE

primeira etapa -> escrever um passo a passo.
passo 1; entra no sistema da empresa.
https://dlp.hashtagtreinamentos.com/python/intensivao/login
passo 2; fazer login.
passo 3; importar a base de dados.
passo 4; cadastrar 1 produto.
passo 5; repetir o processo ate acabar.
'''

import time
import pyautogui
pyautogui.pause = 1

# PASSO1
pyautogui. press("win")
pyautogui.write("google")
time.sleep(2.5)
pyautogui.press ("enter")

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click (x=567, y=382)

# PASSO2
pyautogui.write('duducard495@gmail.com')
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.click (x=672, y=538)


#PASSO3
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)

#PASSO4 
for linha in tabela.index:
   
    pyautogui.click(x=594, y=257) 
    
    código = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = str(tabela.loc[linha, 'categoria'])
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    custo = str(tabela.loc[linha, 'custo'])
    obs = tabela.loc[linha, 'obs']
    
    pyautogui.write(código)
    pyautogui.press('tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(categoria)
    pyautogui.press('tab')
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    pyautogui.write(custo)
    pyautogui.press('tab')
    pyautogui.write('obs')
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    time.sleep(0.5)
    pyautogui.scroll(500) 
    
#PASSO5

if not pandas.isna(obs):
    obs
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.scroll(100)
