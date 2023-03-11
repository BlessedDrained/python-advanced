Исходный файл
```
class Person:
  def __init__(self, name, year_of_birth, address=''):
      self.name = name
      self.yob = year_of_birth
      self.address = address

 def get_age(self):
       now = datetime.datetime.now()
       return self.yob - now.year

 def get_name(self):
       return self.name

 def set_name(self, name):
       self.name = self.name

 def set_address(self, address):
       self.address == address

 def get_address(self):
       return self.address

 def is_homeless(self):
       '''
       returns True if address is not set, false in other case
       '''
       return address is None
```

Найденные ошибки:
* Отсутствие импорта модуля *datetime*
* Некорректные отступы у всех функций, включая инициализатор
* Некорретный отступ содержимого инициализатора
* Некорректный подсчет возраста в get_age():  
~~~
Неверно: self.yob - now.year
Верно: now.year - self.yob
~~~
* Неверное присваивание имени в set_name():  
~~~
Неверно: self.name = self.name
Верно: self.name = name
~~~
* Некорректное присваивание адреса в set_address():
~~~
Неверно: self.address == address
Верно: self.address = address
~~~
  
  
Исправленный код:
~~~
class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        return self.yob - now.year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
       '''
       returns True if address is not set, false in other case
       '''
       return address is None
~~~
