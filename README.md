Оглавление
- Задачи:
    - [Задача 1](#задача-1)
    - [Задача 2](#задача-2)
- Код:
    - [Задача 1](task1/app/)
    - [Задача 2](task2/app/)
- Инструкция:
    - [Запуск](#запуск)
    - [Подключение к базе данных](#подключение-к-базе-данных-с-помощью-dbeaver)
    - [Использование postman](#использование-postman-для-использования-api)
    - [Endpoints](#endpoints)
- Документация openapi:
    - YAML:
        - [Задача 1](documentation/openapi_task1.yaml)
        - [Задача 2](documentation/openapi_task2.yaml)
    - JSON:
        - [Задача 1](documentation/openapi_task1.json)
        - [Задача 2](documentation/openapi_task2.json)

***
# Задача 1

1.  С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
2. Реализовать на Python3 веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:

    - В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
    - После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
    - Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
    - Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.
4. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAalchemy,  пользоваться аннотацией типов.

***
# Задача 2

Необходимо реализовать веб-сервис, выполняющий следующие функции:

- Создание пользователя;
- Для каждого пользователя - сохранение аудиозаписи в формате wav, преобразование её в формат mp3 и запись в базу данных и предоставление ссылки для скачивания аудиозаписи.

Детализация задачи:

1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
2. Реализовать веб-сервис со следующими REST методами:

    - Создание пользователя, POST:

        - Принимает на вход запросы с именем пользователя;
        - Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя и UUID токен доступа (в виде строки) для данного пользователя;
        - Возвращает сгенерированные идентификатор пользователя и токен.

    - Добавление аудиозаписи, POST:

        - Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav;
        - Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;
        - Возвращает URL для скачивания записи вида http://host:port/record?id=id_записи&user=id_пользователя.

    - Доступ к аудиозаписи, GET:

        - Предоставляет возможность скачать аудиозапись по ссылке.

3. Для всех сервисов метода должна быть предусмотрена предусмотрена обработка различных ошибок, возникающих при выполнении запроса, с возвращением соответствующего HTTP статуса.
4. Модель данных (таблицы, поля) для каждого из заданий можно выбрать по своему усмотрению.
5. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисами из пп. 2. и 3., их настройке и запуску. А также пример запросов к методам сервиса.
6. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAlchemy,  пользоваться аннотацией типов.

***
## Запуск
Для запуска приложения необходимо:
1. Перейти с помощью терминала в директорию проекта и нужной задачи, например:
```
cd test_Bewise.ai/task2
```
2. Выполнить следующие команды:
    - Linux/Mac:
        ```
        make lin_compose
        make lin_migrate
        ```
    - Windows:
        ```
        make win_compose
        make win_migrate
        ```
3. Используя:
    - Postman:
        - Используя endpoints воспользоваться сервисом
    - Браузер:
        - Перейти на http://localhost:8000/docs#/
        - Использовать endpoints, представленные на странице
4. Для завершения работы:
    - Linux/Mac:
        ```
        make lin_down
        ```
    - Windows:
        ```
        make win_down
        ```
    - Команда остановит контейнеры и удалит контейнер с приложением
    - В случае возникновения ошибки запуска на линуксе попробуйте поменять docker compose на docker-compose
    - Если не работает make, то выполнить следующие действия по порядку:
        - Linux/Mac:
            ```
            sudo docker compose up -d --build
            sudo docker exec task1-app-1 alembic upgrade heads
            ```
        - Windows:
            ```
            docker-compose up -d --build
            docker exec task1-app-1 alembic upgrade heads
            ```

***
## Подключение к базе данных с помощью dbeaver
Откройте приложение DBeaver и выполните действия на фото:
![](images/main_dbeaver.jpg)
***
![](images/choose_dbeaver.jpg)
***
В поле пароль введите postgres
![](images/connect_dbeaver.jpg)

***
## Использование Postman для использования API
![](images/postman.jpg)

***
## Endpoints

|endpoint|Makes|Request body|Path parametres|
|--------|----------|---------------------------|--------|
|**POST** http://localhost:8000/user/| Позволяет создать пользователя| Request body: <br>- username(string)|None|
|**GET** http://localhost:8000/user/| Позволяет получить список пользователей, возвращает список пользователей (id: int, uuid: str, username: str)| None |None|
|**POST** http://localhost:8000/record/| Позволяет добавить аудиозапись ползователю, возвращает ссылку на скачивание добавленной записи (link:str )| Request body: <br>- user_id: int, <br>- record: wav file|None|
|**GET** http://localhost:8000/record/?user_id={user_id}&record_id={uuid}'| Позволяет скачать файл пользователя| None| Path parametres: <br>- user_id: int,<br>- record_id: str|

** После добавления записи POST запросом вам будет возвращена ссылка для скачивания файла