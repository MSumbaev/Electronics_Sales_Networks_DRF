# Electronics_Sales_Networks_DRF

## Описание

___Electronics_Sales_Networks_DRF___ - веб API приложение на основе DRF для реализации сети по продаже электроники.
Платформа работает только с авторизованными пользователями с помощью JWT токена. Управление всеми сущностями реализовано
как через API, так и через стандартный
Django admin. Полный доступ к управлению всеми сущностями есть только у администратора. Настроена документация swagger,
redoc.

Сеть представляет собой иерархическую структуру из 3 уровней:

- Завод;
- Розничная сеть;
- Индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии).

На странице объекта сети в админ-панели реализована:

- ссылка на «Поставщика» (поле supplier_link);
- фильтр по названию города;
- «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

Реализован CRUD для модели Product и NetworkElement. Удалять и обновлять объекты может только автор этого объекта, а
также админ. Присутствует возможность фильтрации NetworkElement по определенной стране.

### Модели:

- Пользователь/User
- Продукт/Product
- Звено сети/NetworkElement

## Используемое ПО

* Linux
* Python
* Django
* DRF
* PostgeSQL

## Как установить и запустить

1. Для работы проекта необходимо чтобы на вашем компьютере были установлены PostgreSQL;
2. Склонируйте себе репозиторий;
3. Установите зависимости с помощью команды: `pip install -r requirements.txt`;
4. Создайте файл .env используя шаблон .env.sample;
5. Создайте базу данных (не забудьте прописать настройки в .env);
6. Примените миграции: `python3 manage.py migrate`
7. Можете загрузить фикстуру с данными администратора и данные моделей:

```
python3 manage.py loaddata e_sales_networks_data.json
```

8. Запустите сервер: `python3 mange.py runserver`

## Пароли и логины:

### Администратор:

* username: admin
* password: admin
