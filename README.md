# Тестовое задание для тестировщика
1. Переключитесь на ветку add-page-with_form. 
2. Откройте страницу index.html в браузере. 
3. Найдите на странице элемент с id=important, значение ```data-value``` этого элемента введите в поле ввода на странице из пункта 2 и нажмите кнопку ```submit```.
4. Найдите значение хедера ```secret``` в ответе от сервера. 
5. Найдите значение data-value элемента с ```id=special``` на странице.
6. Сделайте POST запрос с помощью утилиты Postman. Вам нужно отправить запрос на адрес ```http://qatest.etprf.ru/api/stage2```
параметр ```secret```, найденный на шаге 4 передается в строке запроса (query string), в теле запроса передается JSON с полем ```special``` со значением ```data-value```, найденным на шаге 5
7. Ответ, полученный от сервера является результатом выполненной проверки, направьте нам результат.

Для запуска проекта скопируйте проект в рабочую директорию https://github.com/Timur2807/Testing.git. 
Настройте виртуальное окружение для этого откройте командную строку(CMD) 
Передите в рабочую директорию сd (worddir)
Далее пишем команду python -m venv venv .
Этой командой вы создаете виртуальное окружение.
Нужно активировать виртуальное окружение
venv\Scripts\activate
После нужно установить все зависимости.
pip install -r requirements.txt
Как только установятся все зависимости можно приступать к запуску скрипта.
Пишем команду python get_value.py
