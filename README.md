# hw04_tests

[![CI](https://github.com/yandex-praktikum/hw04_tests/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw04_tests/actions/workflows/python-app.yml)

#### Юниттесты для проекта yatube.
Проект содержит тесты для:
- моделей приложения posts;
- url-адресов проекта;
- views и шаблонов;

#### Запуск проекта в dev-режиме 
- Установите и активируйте виртуальное окружение: ```python -m venv venv```
- Установите зависимости из файла requirements.txt: ``` pip install -r requirements.txt ``` 
- Создайте миграции и мигрируйте их в БД: ```python manage.py makemigrations```, ```python manage.py migrate```
-  Запустите сервер, выполнив в папке с файлом manage.py команду: ``` python manage.py runserver ``` 

##### Финальная версия проекта yatube: https://github.com/creamsandwch/hw05_final.
