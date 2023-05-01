# Бекенд приложения

### Запуск приложения

Для запуска проекта требуется docker и docker-compose

```bash
  docker-compose up --build
```

В случае, если показывается ошибка о permission denied entrypoint.sh, требуется выполнить команду(Mac / Linux)
```bash
  chmod +x ./project/entrypoint.sh
```

Для доступа к шелу джанго, есть два пути:
- установить все необходимые зависимости и запускать через `python3 manage.py shell`
- запускать проект через докер и дополнительно в другой консоли запустить шел внутри контейнера

1. Узнать id контейнера `sem4univer_backend_web`
```bash
> docker container list
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS         PORTS                                                                                  NAMES
7bf761ddf202   sem4univer_backend_celery        "/usr/src/app/entryp…"   1 second ago     Up 1 second                                                                                           sem4univer_backend_celery_1
48ac4e881e2b   sem4univer_backend_web           "/usr/src/app/entryp…"   1 second ago     Up 1 second    0.0.0.0:1337->8000/tcp, :::1337->8000/tcp                                              sem4univer_backend_web_1
d108af6eb4b5   sem4univer_backend_celery-beat   "/usr/src/app/entryp…"   2 seconds ago    Up 1 second                                                                                           sem4univer_backend_celery-beat_1
1088ceef532d   mailhog/mailhog                  "MailHog"                18 minutes ago   Up 1 second    0.0.0.0:1025->1025/tcp, :::1025->1025/tcp, 0.0.0.0:8025->8025/tcp, :::8025->8025/tcp   sem4univer_backend_smtp-server_1
987bd90e5052   redis:alpine                     "docker-entrypoint.s…"   18 minutes ago   Up 2 seconds   6379/tcp                                                                               sem4univer_backend_redis_1
```

2. Запустить шелл внутри контейнера
```bash

  docker exec -it 48ac4e881e2b python3 manage.py shell
```