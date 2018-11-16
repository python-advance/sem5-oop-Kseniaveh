"""
2.1 Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга».
Создание функций для вывода на печать информации, хранящийся в объектах.

2.3. Формирование отчета по практическому заданию и публикация его в портфолио.
Отчет сформирован в портфолио по данным заданиям.
"""

"""
Создание класса "Запись" для приложения "Блог"
"""
class Record():
  def __init__(self, author, title,coms):
    self.__title = title
    self.__author = author
    self.__comments = coms  

  def show_comments(self):
    print(self.__title+'  '+self.__author)
    for com in self.__comments:
      print(f"Заголовок коммента: {com.title}, текст коммента: {com.text}")    

"""
Создание класса "Запись" для приложения "Блог"
"""
class Comment():
  def __init__(self, title, text):
    self.__title = title
    self.__text = text

  """
  Создаем свойство класса @property для поля title: getter
  """
  @property
  def title(self):
    return self.__title

  """
  Создаем свойство класса @property для поля text: getter
  """
  @property
  def text(self):
    return self.__text
    
"""
Создание объектов для класса Comment
"""
myComment = Comment('First comment1', 'Very cool!')
myComment2 = Comment('First comment2', 'Very cool!')
myComment3 = Comment('First comment3', 'Very cool!')

"""
Создание пустого списка для добавления в него объектов класса Comment
"""
lst=[]
lst.append(myComment)
lst.append(myComment2)
lst.append(myComment3)

"""
Создание объектов для класса Record
"""
myRecord = Record('Vehova', 'First record',lst)
myRecord2 = Record('Vehova2', 'First record2',lst)
myRecord3 = Record('Vehova3', 'First record3',lst)

"""
Создание пустого списка для добавления в него объектов класса Record
"""
records=[]
# добавление каждого нового объекта записи в конец списка
records.append(myRecord)
records.append(myRecord2)
records.append(myRecord3)

# отображение записей в списке 
for rec in records:
  rec.show_comments()

# удаление записи из списка
recorddel=records[1];
records.remove(recorddel)
print('------------------------DELETED 1 ELEM------------------------')
for rec in records:
  rec.show_comments()


#myRecord.show_comment(comment=myComment)
#myRecord.show_comments()


