# формат запроса
# http://<ваш_сервер>:5000/fetch?url=https://example.com&proxy=proxy_server:port&username=your_username&password=your_password&headless=false
# http://127.0.0.1:5000/fetch?url=https://antcpt.com/score_detector&headless=false

import logging
from datetime import datetime
from pathlib import Path

from flask import Flask, request, jsonify

from parser.selenium_pars import HtmlGetter

from utils.proxy_auth import make_proxy_auth


# Инициализируем логгер
logger = logging.getLogger(__name__)
log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
Path(log_name).parent.mkdir(parents=True, exist_ok=True)

# Конфигурируем логирование
logging.basicConfig(
    level=logging.WARNING,                                             # настройка - DEBUG, production - WARNING
    filename=log_name,                                                # добавляем логи в файл
    filemode='w',                                                     # режим записи (a - добавить, w - переписать)
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

# Выводим в консоль информацию о начале запуска бота
logger.info('Starting app')

app = Flask(__name__)


@app.route('/fetch', methods=['GET'])
def fetch():

    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    proxy = request.args.get('proxy', False)
    username = request.args.get('username', False)
    password = request.args.get('passwords', False)
    headless = request.args.get('headless', 'true')

    if username and password and proxy:
        chrome = HtmlGetter(headless, proxy_auth=make_proxy_auth(login=username, password=password, proxy=proxy))
    elif proxy:
        chrome = HtmlGetter(headless, proxy=proxy)
    else:
        chrome = HtmlGetter(headless)

    html = 'Ответа не получено'

    try:
        html = chrome.get_html(url)
    except ConnectionError as conn_er:
        html = conn_er
    except Exception as ex:
        logger.error(ex)
    finally:
        chrome.close_driver()

    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)                             # Запускаем сервер на всех интерфейсах на порту 5000
