Support application API

Technology Stack

Python
Django
Django Rest Framework
PostgreSQL
Redis
Celery
Docker, docker-compose
Install

install Python 3

Тестовое задание Innowise Приложение “Support”.
Цель:

1) Пользователь пишет тикет и отправляет.
2) Саппорт видит решенные, нерешенные и замороженные тикеты (все по факту), может отвечать на них.
3) Пользователь может просмотреть ответ саппорта, и добавить новое сообщение( саппорт ответить на него).
4) Саппорт может изменять статусы тикетов.

API:
GET     127.0.0.1:8000/api/task/                                                           - список текущих задач
        127.0.0.1:8000/api/task/id_task                                                     - просмотр деталей задачи

POST   127.0.0.1:8000/auth/users                params{'username':'name', 'password':'123'} - создание учетной записи
       127.0.0.1:8000/token/                    params{'username':'name', 'password':'123'} - получение токена
       127.0.0.1:8000/api/task/                 headers{'Authorization': Bearer 'token'}
                                                        params{'text':'text_task'}           - добавление задачи
       127.0.0.1:8000/api/create_answer/         headers{'Authorization': Bearer 'token'}
                                                        params{'task':'id_task',
                                                                'text':'text_answer',
                                                                'parent':'id_answer'}          - добавление ответа

PUT   127.0.0.1:8000/api/task/id_task    headers{'Authorization': Bearer 'token'}
                                                        params{'status':'name_status'} - изменение статуса (только Админ.)
