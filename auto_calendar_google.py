import pyautogui
import time
import pandas

pyautogui.PAUSE = 1.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.click(x=793, y=77)
link = 'https://calendar.google.com/calendar/u/0/r/year'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(2)

tabela = pandas.read_csv('story.csv')

for i in range(0, len(tabela)):
    pyautogui.click(x=90, y=274)
    time.sleep(0.5)
    pyautogui.click(x=72, y=392)
    time.sleep(0.5)
    pyautogui.click(x=880, y=470)
    pyautogui.write(tabela.loc[i, 'titulo'])
    pyautogui.click(x=806, y=595)
    pyautogui.typewrite(tabela.loc[i, 'data'])
    pyautogui.click(x=899, y=559)
    pyautogui.write(tabela.loc[i, 'hora'])
    pyautogui.click(x=824, y=744)
    pyautogui.write('Frase:')
    pyautogui.press('enter')
    pyautogui.write(tabela.loc[i, 'frase'])
    pyautogui.press('enter')
    pyautogui.write('Imagem:')
    pyautogui.press('enter')
    pyautogui.write(tabela.loc[i, 'sugestao'])
    pyautogui.click(x=1164, y=962)
    time.sleep(2)
    # pyautogui.click(x=863, y=75)
    # pyautogui.write(link)
    # time.sleep(1)
