# Результат выполнения тестового задания Django + DRF

## Настройка переменных среды

Для запуска приложения необходимо скопировать пример конфигурации:

```sh
cp .django_env.example .django_env
```

И внести необходимые изменения (параметры подключения к базе, SECRET_KEY) в `.django_env`


## Зависимости

Установка необходимых зависимостей производится посредством: `pip install -r requirements.txt`

Добавление новых зависимостей: 

- Добавляем необходимую зависимость в `requirements.in`
- Выполняем `pip-compile` (из пакета [pip-tools](https://pypi.org/project/pip-tools/)) - эта команда основываясь на `requirements.in` сгенерирует `requirements.txt`
- Выполняем `pip install -r requirements.txt` чтобы установить добавленные зависимости


## Swagger

Документация API (swagger) располагается тут: `http://127.0.0.1:8000/api/v1/schema/swagger-ui/`