import requests
from bs4 import BeautifulSoup

# Шаг 1: Читаем HTML-контент из файла index.html
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Шаг 2: Парсим HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Находим элемент с id "important" и получаем его data-value
important_value = soup.find(id='important')['data-value']
print(f'Значение important: {important_value}')

# Шаг 3: Отправляем запрос на сервер stage1
response = requests.get('http://qatest.etprf.ru/api/stage1', params={'important': important_value})

# Проверяем, был ли запрос успешным
if response.status_code == 200:
    # Извлекаем заголовок secret из ответа
    secret_header = response.headers.get('secret')
    print(f'Заголовок Secret: {secret_header}')

    # Предполагаем, что ответ содержит JSON-данные
    result = response.json()

    # Извлекаем data-value из элемента с id "special"
    special_value = result.get('special')
    print(f'Значение special: {special_value}')

    # Отправляем запрос на сервер stage2
    url_stage2 = 'http://qatest.etprf.ru/api/stage2'
    headers = {'Content-Type': 'application/json'}
    json_data = {'special': special_value}

    # Отправляем POST-запрос с параметром secret в строке запроса
    response_stage2 = requests.post(url_stage2, params={'secret': secret_header}, json=json_data)

    # Проверяем, был ли запрос успешным
    if response_stage2.status_code == 200:
        try:
            json_response = response_stage2.json()
            print('Запрос на stage2 выполнен успешно!')
            print(f'Ответ от stage2: {json_response}')
        except ValueError:
            print('Ошибка декодирования JSON. Ответ сервера не является корректным JSON:')
            print(response_stage2.text)  # Выводим текст ответа для диагностики
    else:
        print(f'Ошибка при запросе на stage2: {response_stage2.status_code} - {response_stage2.text}')
else:
    print(f'Ошибка при запросе на stage1: {response.status_code} - {response.text}')
