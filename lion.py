from collections import Counter
import docx
import matplotlib.pyplot
import pandas
#Импортируем наши библиотеки

#Открываем документ Word
doc = docx.Document('lion.docx') 
#Собираем весь текст в строку
text = ' '.join([pl.text for pl in doc.paragraphs])

#Cписок знаков препинания для удаления из текста
znak_prep = '.,!?;:"()'
for vz in znak_prep:
    #Теперь удаляем каждый знак препинания из текста
    text = text.replace(vz, '')

#Разбиваем наш текст на слова
num_of_words = text.split() 
#Считаем сколько раз встречается каждое слово в тексте
schitaem_slova = Counter(num_of_words) 
#Общее количество слов в тексте
vsego_slov = len(num_of_words)

spisok_slov = [(slovo, kolvo, (kolvo / vsego_slov) * 100) for slovo, kolvo in schitaem_slova.items()]
pandas.DataFrame(spisok_slov, columns=['Слово', 'Количество', 'Частота (%)']).to_excel('num_of_words.xlsx', index=False) 

russ_bukvi = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' 
#Отбираем только русские буквы
bukvi = [qwe for qwe in text if qwe in russ_bukvi] 
schitaem_bukvi = Counter(bukvi)

 #Создаем столбчатую диаграмму
matplotlib.pyplot.bar(schitaem_bukvi.keys(), schitaem_bukvi.values())
 #Подпись для  OY
matplotlib.pyplot.ylabel('Количество')
#Подпись для OX
matplotlib.pyplot.xlabel('Буквы')
#График
matplotlib.pyplot.show() 

for ck, kolvo in schitaem_bukvi.items():
    #Печатаем статистику
    print(f"{ck}: {kolvo}") 
