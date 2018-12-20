"""
Вариативная самостоятельная работа
3.1 Разработка прототипа приложения “Регистрация на конференцию” 
на основе фрагмента технического задания с использованием ООП.

Также в данном задании реализованы getter,setter,deleter для полей формы год рождения и email (задание - Инвариантное работа: 2.2)
"""

""" 
Импортируем модуль re для регулярных выражений года рождения, email
"""
import re 

"""
Создаем класс и пустой список для логгера
"""
class Participant():
  logger = []
  
  """
  Описываем конструктор, где в качестве свойства выступает словарь с входящими полями формы 
  """
  def __init__(self, my_dict):

    self.f_name = my_dict["f_name"] 
    self.s_name = my_dict["s_name"]
    self.country = my_dict["country"]
    self.city = my_dict["city"]
    self.affiliation = my_dict["affiliation"]
    self.streetaddress = my_dict["streetaddress"]
    self.email = my_dict["email"]
    self.birthyear = my_dict["birthyear"]
    

  """
  Создаем свойство класса @property для поля года рождения: getter,setter,deleter
  """

  @property
  def birthyear(self):
      return self._birthyear
    
  @birthyear.setter
  def birthyear(self, value):
    pattern_bd = r".*([1-3][0-9]{3})"
    bd_prov = re.compile(pattern_bd) # re.compile -компиляции регулярного выражения
    self.logger.append("Успешно создан паттерн для года рождения")

    if (not (bd_prov.findall(str(value)))):
      raise ValueError('Invalid birthyear')
    else:
      self.logger.append("Год прошел проверки")
      self._birthyear = int(value)

  @birthyear.deleter
  def birthyear(self):
        self._birthyear = None

  """
  Создаем свойство класса @property для поля года рождения: getter,setter,deleter
  """
  @property
  def email(self):
      return self._email
    
  @email.setter
  def email(self, value):
    pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    number_re = re.compile(pattern) # re.compile -компиляции регулярного выражения
    self.logger.append("Успешно создан паттерн для emali")

    if (not (number_re.findall(str(value)))):
      raise ValueError('Invalid email')
    else:
      self.logger.append("Email прошел проверки")
      self._email = value

  @email.deleter
  def email(self):
        self._email = None

  
  """
  Создаем метод для получения данных из формы
  """
  def get_client_info(self):
    self.participant_info = {
      "f_name": self.f_name,
      "s_name": self.s_name,
      "email": self.email,
      "birthyear": self.birthyear,
      "country": self.country,
      "city": self.city,
      "affiliation":self.affiliation,
      "streetaddress": self.streetaddress
    }

    return self.participant_info

  """
  Метод озвращает строковое представление объекта.
  """
  def __str__(self):
    return (self.f_name + " " + self.s_name)

"""
Объявляем переменные для формы
"""
name = input("Введите имя:")
Sname = input("Введите фамилию:")
mail = input("Введите почту:")
year = input("Введите год рождения:")
count = input("Введите страну:")
town = input("Введите город:")
field = input("Введите университет:")
street = input("Введите улицу:")


newduct={"f_name":name,"s_name":Sname,"email":mail, "birthyear":year, "country":count, "city":town, "affiliation":field, "streetaddress":street}

"""
Ввыводим значение полей формы и логгер
"""
get_inf=Participant(newduct)
print(get_inf.get_client_info())

"""
Запись в файл логгеров
"""
with open('fileLog.txt', 'a') as f:
  f.write(str(get_inf.logger))


#get_inf.email='ksenia@gmil.com'
#print(get_inf.email)
#print(get_inf.logger)
