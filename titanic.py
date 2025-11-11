import pandas
import matplotlib.pyplot
#Импротируем наши библиотеки

dq = pandas.read_parquet('titanic.parquet')
#Конвертируем в csv
dq.to_csv('titanic.csv', index=False) 

#Данные для анализа
Table = dq.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
#Проценты
Table_percentage = Table.div(Table.sum(axis=1), axis=0) * 100
# Меняем порядок столбцов(ниже еще меняем цвета сверху вниз!)
Table_percentage = Table_percentage[[0, 1]]
#Столбчатая диаграмма в процентах
Table_percentage.plot(kind='bar', stacked=True, color=['blue', 'orange'])

#Подписи на нашем графике
matplotlib.pyplot.title('Статистика выживания на Титанике')  
matplotlib.pyplot.legend(['умерло', 'выжило'])
matplotlib.pyplot.xlabel('Класс')
matplotlib.pyplot.ylabel('% людей')

#График
matplotlib.pyplot.show()

