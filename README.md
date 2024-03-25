<h2 alingn='center'>DevSearch</h2>

### Описание проекта:
    Для разработчиков
    Возможность добавления блога.
    Регистрация и авторизация пользователей.
    
## Разработка



##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python3 -m venv venv
    
##### 3) Активировать виртуальное окружение

    venv\Scripts\activate.bat - Windows

    venv/bin/activate - Linux

##### 4) Устанавливить зависимости:

    pip3 install -r requirements.txt
    
##### 5) Выполнить команду для выполнения makemigrations

    python3 manage.py makemigrations

##### 6) Выполнить команду для выполнения миграций

    python3 manage.py migrate

##### 7) Создать суперпользователя

    python3 manage.py createsuperuser
    
##### 8) Запустить сервер

    python3 manage.py runserver
