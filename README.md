## Текущий семестр

## Описание из прошлого семестра
Выбран тип модели Zero-Shot Image Classification. Модель - openai/clip-vit-large-patch14. В скрипте [clip.py](https://github.com/nasheshin01/URFU_ML_PI/blob/master/SheshinProject/choosed_model/clip.py) представлен пример запуска данной модели.

Было разработано web-приложение на основе библиотеки streamlit. Данное приложение организует работу с ранее выбранной моделью для классификации изображений на произвольных классах.

Код состоит из:
1. Обертка для модели - [clip_classifier.py](https://github.com/nasheshin01/URFU_ML_PI/blob/master/SheshinProject/clip_classifier.py)
2. Скрипт конструирующий само web-приложение - [streamlit_page.py](https://github.com/nasheshin01/URFU_ML_PI/blob/master/SheshinProject/streamlit_page.py)

Приложение:
- Запускается приложение с помощью команды - ```streamlit run streamlit_page.py```
- Скриншоты работы приложения можно найти в папке [screenshots - app1.png, app2.png, app3.png](https://github.com/nasheshin01/URFU_ML_PI/blob/master/SheshinProject/screenshots)

Было реализовано API для классификатора изображений CLIP.
Запросы:
- GET запрос на основную страницу, выдающий описание использования возможных запросов
- GET запрос ```/docs``` - документация API
- POST запрос ```/predict``` - запрос для классификации изображения по выбранным классам. Пример тела запроса:
  ```
  {
      "image_url": "http://images.cocodataset.org/val2017/000000039769.jpg",
      "labels": ["cats", "dogs", "cows"]
  }
  ```
Установка и запуск:
1. Перейти в каталог [SheshinProject](https://github.com/nasheshin01/URFU_ML_PI/blob/master/SheshinProject)
2. Установка зависимостей приложения через команду ```pip install -r .\requirements.txt```
3. Запуск сервера запросов через команду ```uvicorn.exe api_logic:app```

Присутствуют тесты для API.

В файле [test_api.py](SheshinProject\test_api.py) было создано два теста:

- Тест корневой страницы API - test_root
- Тест работы модели через API - test_predict

На этом скриншоте видно прохождение тестов:
![Alt text](SheshinProject/screenshots/image.png)
