# Курс "Знакомство с Django: ORM" 
## Задача "Урок 1. Пишем пульт охраны банка"

<img src="https://dvmn.org/media/lessons/Django_1-st_LVl_003.png" alt="security" width="150"/>

Репозиторий с сайтом для урока «Пишем пульт охранника банка» курса [dvmn.org](https://dvmn.org/modules/)

# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние».
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД,
но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт,
который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Запросите доступ к БД у менеджера вашего банка.  
Для доступа вам понадобятся хост, порт, название базы данных, логин и пароль.  

Создайте в корневой папке файл `.env` и пропишите в нем эти данные следующим образом:

```
HOST=0.0.0.0
PORT=8000
NAME=security_db
USER=user
PASSWORD=qwerty12
```
где:

`HOST` - IP адрес или доменное имя БД

`PORT` - Порт БД

`NAME` - Имя БД

`USER` - Имя пользователя БД

`PASSWORD` - Пароль пользователя БД

При желании, для включения отладочной системы в файле .env дабавляем следующую нажпись:
```
DEBUG=True
```
По умолчанию DEBUG отключен



Python3 должен быть уже установлен. 

Затем установите зависимости:
```
pip install poetry
```


### Как запустить
```
python manage.py runserver 0.0.0.0:8000
```


открываем в браузере адрес сайта: `http://127.0.0.1:8000/`


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

