# Рассчитать время утс верхней кульминации для светил из списка обджект.
# создать графический интерфейс для программы

import astropy.io.fits as pyfits
import astropy
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *

# заранее сделаем два списка: один с названиями,
# второй с прямым восх

file = open("C:/Users/3512/Downloads/Telegram Desktop/objects.dat","r")#открыли файл
all_text = file.readlines() #взяли всё из файла, поделили по строкам. один список - одна строка
print(all_text)

name = []
alpha = []
for line in all_text: #line у нас будет просто каждой строчкой из файла или же каждым элементом из all_text
    name.append(line.split(f'\t')[0])  #смотрим где строка делится табом, вычленяем объекты с нулевым индексом,
    # выгружаем их в изначально пустой список name
    # иначе говоря:
    # m = line.split(f'\t')[0]
    # name.append(m)
    alpha.append(line.split(f"\t")[1]) #вычленяем объекты в строках с индексом 1
alpha[0] = 'alpha' #переименовали чтобы называлось красиво

def click():
    lbl2 = Label(text='Ниже список объектов с соотв α')
    lbl2.grid(column=1, row=3)

    for i in range (0, len(name)):
        lbl3 = Label(text=f'{name[i]}')
        lbl3.grid(column = 1, row = 4+i)
        lbl4 = Label(text=f'{alpha[i]}')
        lbl4.grid(column = 2, row = 4+i)


window = tk.Tk()
window.title("Время UTC для верхней кульминации")
window.geometry('800x800')

lbl1 = Label(text='Введите путь к файлу')
lbl1.grid(column = 1, row = 1)

entr1 = Entry(width = 60)
entr1.grid(column = 2, row = 1)
entr1.insert(0, 'C:/Users/3512/Downloads/Telegram Desktop/objects.dat')

btn = Button(window, text="Принять", command=click)
btn.grid(column = 1, row = 2)


window.mainloop()