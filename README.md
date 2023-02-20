# stripe1
Решение тестового задания "Функционал бэкенда на Django + Spripe API"
Тестовое задание находится в файле test_task.md

Пример разворачивания удаленном сервере:
http://89.108.76.227:8000/

Как установить проект
(Разворачивал на vps-серверах с Ubuntu 20.04 LTS и Debian 11)

Клонировать репозиторий и перейти в него командной строкой:
git clone https://github.com/TarumK/stripe1.git
cd stripe1

Создать и активировать виртуальное окружение:

python3 -m venv venv
source venv/bin/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Так как я делал коммиты и пушил вместе с базой данных(она маленькая), то делать миграцию необязательно.
А так при необходимости можно сделать миграцию
Выполнить миграции:

cd stripe1
python3 manage.py migrate

Запустить проект:
python3 manage.py runserver

Стек технологий: Python 3, Django 4.1.7, JS, Stripe API 5.1.1
Автор проекта - Мурат Кябишев

Бонусная часть задания с непрерывным потоком платежей и оплатой подписок пока не решил,
но при наличии дополнительного времени, думаю справлюсь.

Пробовал собрать докер-образ и даже собрал, но он с привязкой к конкретному IP-адресу сервера,
на котором разворачивается. Пока не разобрался, как можно через docker-composer настроить ip-adress хоста,
на котором нужно запустить контейнер.
Адрес докер-образа следующий: https://hub.docker.com/repository/docker/tarumk/stripe_test/general


