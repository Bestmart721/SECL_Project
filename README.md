# SECL_Project
project Secl Group
My project django 1.8
login admin
password admin
Homework 5
В этом задании Вам нужно создать проект управления сетью магазинов.
В нем должно быть несколько приложений -- места, контактные лица, магазины и склады. (4 шт.)
В местах должны быть сущности страны и города. Страна и город должны иметь название, а также в городе должна быть указана страна.
В контактных лицах должны быть сущности контактных лиц, которые имеют имя, фамилию, пол, дату рождения и мейл. Один мейл не может быть в разных контактных лиц.
В магазинах должны быть сущности типа магазина и самого магазина. Тип магазина имеет только название (может иметь значение одежда, еда, стройматериалы, супермаркет, и т.д.). Магазин имеет тип магазина, название, владельца, продавцов, склады, город, адрес и сайт. Магазин может иметь только одного владельца, но может иметь много продавцов и складов. Магазин может не иметь сайт.
В складах должна быть сущность склада. Склад имеет название, город и адрес.

Все модели нужно добавить в админку и заполнить ее данными (по не менее 10 записей на каждую модель).

Как результат -- нужно выслать архив с файлами рабочего проекта.

Дополнительно прошу почитать об реляционных базах данных и о связях между таблицами (один-к-одному, один-ко-многим, многие-ко-многим).
Куда отправлять и как оформлять тему письма вы уже должны знать ;)

P.S.:

На уроке я пропустил OneToOneField -- связь один-к-одному.
По сути -- это тот же ForeignKey, только с атрибутом unique=True (индекс уникальных значений)
