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
  def __init__(self, author, title):
    self.__title = title
    self.__author = author

  def show_comment(self, comment=object):
    print(f"Заголовок коммента: {comment.title}, текст коммента: {comment.text}")

"""
Создание класса "Запись" для приложения "Блог"
"""
class Comment():
  def __init__(self, title, text):
    self.__title = title
    self.__text = text

  """
  Создаем свойство класса @property для поля title: getter,setter,deleter
  """
  @property
  def title(self):
    return self.__title
    
  @title.setter
  def title(self, value):
    self.__title = str(value)

  @title.deleter
  def title(self):
    self.__title = None

  """
  Создаем свойство класса @property для поля text: getter,setter,deleter
  """
  @property
  def text(self):
    return self.__text
    
  @text.setter
  def text(self, value):
    self.__text = str(value)

  @text.deleter
  def text(self):
    self.__text = None

"""
Создание объектов
"""
myRecord = Record('Vehova', 'First record')
myComment = Comment('First comment', 'Very cool!')

myRecord.show_comment(comment=myComment)
