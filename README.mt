Pet-проект для получения HTML-разметки

▎Что делает скрипт
Этот код использует Selenium WebDriver для извлечения HTML-кода с указанной веб-страницы. Скрипт размещается
на удаленном сервере и управляется через HTTP. Для управления используются GET-запросы в формате:
http://<ваш_сервер_1.1.1.1>:5000/fetch?url=https://example.com/
С помощью амперсанда () можно передавать дополнительные параметры, такие как:
• headless=false — отключение "безголового" режима.
• proxy=proxy_server:port — использование прокси-сервера.
• username=your_username&password=your_password — аутентификация прокси.
Для работы с прокси с аутентификацией используется библиотека selenium-wire, которая требует установки blinker==1.7.0.
Чтобы избежать конфликтов с зависимостями Flask, необходимо установить seleniumbase с нужными зависимостями.

▎Почему проект полезен
Этот проект полезен для разработчиков и исследователей, которые хотят автоматизировать процесс получения HTML-кода
с веб-страниц. Он может быть использован для веб-скрейпинга, анализа данных, тестирования веб-приложений и других задач,
связанных с извлечением информации из интернета.

▎Как пользователи могут приступить к работе с проектом
Чтобы начать работу с ботом, выполните следующие шаги:
1. Клонируйте репозиторий на свой сервер: git clone https://github.com/K-ei092/petParser.git
2. Перейдите в директорию проекта: cd ваш_репозиторий
3. Установите все зависимости, используя команду: pip install -r requirements.txt
4. Запустите сервер: python app.py
5. Используйте API для получения HTML-кода, отправляя GET-запросы.

▎Где пользователи могут получить помощь по проекту
Если у вас возникли вопросы или вам нужна помощь по использованию проекта, вы можете обратиться к разработчику в GitHub
по имени пользователя K-ei092 (https://github.com/K-ei092). Я постараюсь ответить на ваши вопросы как можно быстрее.

▎Кто поддерживает проект и вносит вклад в проект
Проект поддерживается единственным разработчиком. Ваши отзывы и предложения по улучшению проекта всегда приветствуются
и могут быть отправлены через GitHub. Если вы хотите внести свой вклад, пожалуйста, создайте запрос на изменение
(pull request) или откройте проблему (issue) для обсуждения.

▎Лицензия
Лицензий для использования проекта не требуется

Спасибо за интерес к проекту! Надеемся, он будет полезен для вас!