#!/usr/bin/env python
# coding: utf-8

# # Основы питона

# ### Про выполнение команд
# * Shift + Enter - выполнить код в ячейке и перейти на следующую
# * Ctrl + Enter - выполнить и остаться
# 
# ### Немного полезностей и про markdown:
# * перевести ячейку из кода в комментарии можно с помощью 'Esc + m' или просто 'm', если вы не еще не успели сделать ее активной
# * добавить новую ячейку можно аналогичным образом через 'b'
# * Jupyter понимает эти команды и в русской раскладке
# * все это можно сделать и через верхнюю панель, но рано или поздно она начнет вас раздражать
# * можно писать формулы, список горячих клавиш Ctrl+Shift+P (Command+Shift+P для мака)
# * https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
# * для выделения можно использовать решетки или просто **выделить пожирнее**
# 

# ## Целые и дробные числа

# In[ ]:


# тип присваивается автоматически
snake_case_integer = 4


# In[ ]:


print(snake_case_integer)


# In[ ]:


# для вывода в jupyter notebook не обязательно использовать print
snake_case_integer


# In[ ]:


print(snake_case_integer)


# In[ ]:


# как определить тип переменной
type(snake_case_integer)


# In[ ]:


camelCaseFloatNumber = 4.0


# ### Одно из отличий версий питона 2.7 и 3+

# In[ ]:


3 / 2


# In[ ]:


""" многострочные комментарии
во второй версии питона по умолчанию деление целочисленное
в python 2.7 надо писать float(4) / 3 или 4 / 1.0 / 3

еще вариант - импортировать
from __future__ import division
"""
4 / 3


# Остаток от деления

# In[ ]:


5 % 3


# Возведение в степень

# In[ ]:


5 ** 3


# ### Упражнение
# Выведите на экран реверсную запись трехзначного числа. Пример: вместо 361 вывести 163

# In[ ]:


num = 361


# In[ ]:





# In[ ]:





# ### Основные математические функции
# 
# https://docs.python.org/3/library/math.html

# In[ ]:


import math


# In[ ]:


math.factorial(5)


# In[ ]:


5 * 4 * 3 * 2 * 1


# In[ ]:


# используйте автодополнение
math.factorial(5)


# ### Упражнение
# 
# Посчитайте значение выражения:
# $e^{(x-\mu)\pi}$
# 
# Как писать такие формулы
# 
# http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html

# In[ ]:


x = 4
mu = 2


# In[ ]:





# In[ ]:





# ## Строки

# In[ ]:


title = 'сборная России в финале чм'


# In[ ]:


title = 'сборная России в "финале" чм'


# In[ ]:


title


# In[ ]:


# первая буква слова
title[0]


# In[ ]:


# все буквы с индексами 0, 1, 2
title[:3]


# **А в строчке выше буква с индексом 3 не вошла в результат**

# In[ ]:


# последняя буква
title[-1]


# In[ ]:


# количество букв в строке
len(title)


# ### Булевый тип данных

# In[ ]:


True False


# In[ ]:


1 > 4


# In[ ]:


1 < 4


# In[ ]:


logs = 'user_1 \t apple \t 65371 \nuser_2 \t samsung \t 35300 \nuser_3 \t lg \t 43243 \n'
print(logs)


# In[ ]:


'apple' in logs


# In[ ]:


if 'apple' in logs:
    print('В наличии')
else:
    print('Нету')


# ### Упражнение
# Дана строка с периодическим сигналом signal. Известно, что период укладывается в диапазон от 3 до 10 цифр. Вам необходимо написать код, который берет первые n цифр и сравнивает результат со строкой от n+1 до 2n. Тем самым определяя период сигнала.
# 
# Для ускорения проверки вы можете использовать цикл:
# 
# for n in range(3, 11):

# In[ ]:


signal = '10101001101010011010100110101001101010011010100110101001'


# In[ ]:


signal[:3]


# In[ ]:


signal[3:6]


# In[ ]:


signal[:3] == signal[3:6]


# In[ ]:





# In[ ]:





# In[ ]:





# Замена подстроки

# In[ ]:


title


# In[ ]:


title.replace('России', 'РФ')


# In[ ]:


title = title.replace('России', 'РФ')
title


# Удаление символов в начале и конце строки

# In[ ]:


'  123 '.strip()


# In[ ]:


'  123\n'.strip()


# In[ ]:


'  123x'.strip('x')


# ### Вывод формата результата
# 
# https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html

# In[ ]:


pi_estimation = 22/7


# In[ ]:


type(pi_estimation)


# In[ ]:


type(str(pi_estimation))


# In[ ]:


# в этой строке специально ошибка
result = 'Значение 22/7 (' + pi_estimation + ') является приближением числа pi (' + math.pi + ')'


# In[ ]:


result = 'Значение 22/7 (' + str(pi_estimation) + ') является приближением числа pi (' + str(math.pi) + ')'
result


# In[ ]:


from IPython.display import Image
Image('do_not_format_like_this.jpg')


# Устаревший синтаксис форматирования

# In[ ]:


result = 'Значение 22/7 (%d) является приближением числа pi (%d)' % (pi_estimation, math.pi)
result


# Более запоминающийся вариант

# In[ ]:


result = 'Значение 22/7 ({:.4%}) является приближением числа pi ({:.4f})'.format(pi_estimation, math.pi)
result


# In[ ]:


# указание порядка
'{0}{1}{0}'.format('abra', 'cad')


# Вариант в 3.x питоне

# In[ ]:


f'Значение 22/7 ({pi_estimation:.4f}) является приближением числа pi ({math.pi:.4f})'


# ### Упражнение
# 
# Количество показов баннера = 10\*\*6, кликов по баннеру = 525
# 
# Выведите отношение кликов к показам в следующем формате:
# 
# CTR баннера равен 0.052%

# In[ ]:


shows = 10**6
clicks = 525


# In[ ]:





# In[ ]:





# In[ ]:





# ### Перевод числа в строки и наоборот

# In[ ]:


string_num = '3.1415'


# In[ ]:


# для целых чисел есть функция int
float_num = float(string_num)
float_num


# In[ ]:


# из числа в строку - функция str
type(str(float_num))


# In[ ]:


float('3.14')

