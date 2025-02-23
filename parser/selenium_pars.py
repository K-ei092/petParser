import random
import logging
import time
import os

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

from parser.user_agent import user_agent_pc


logger = logging.getLogger(__name__)

# установка драйвера
executable_path = ChromeDriverManager().install()


class HtmlGetter:

    # конструктор вебдрайвера
    def __init__(self, headless: str = 'true', proxy: str | bool = False, proxy_auth: dict | bool = False):

        ua = random.choice(user_agent_pc)

        current_dir = os.getcwd()
        folder_name = 'seleniumwire_storage'
        storage_dir = os.path.join(current_dir, folder_name)
        options_sw = {
            'request_storage_base_dir': storage_dir,
            'request_storage': 'memory',
            'request_storage_max_size': 200                               # 'log_level': None
        }
        chrome_service_path = ChromiumService(executable_path=executable_path)

        option = webdriver.ChromeOptions()
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_argument('log-level=3')
        option.add_argument('--window-size=1300,750')
        option.set_capability("pageLoadStrategy", "eager")                # не ждать полной загрузки страницы

        if headless == 'true':
            option.add_argument('--headless=new')                         # включение фонового режима

        if proxy_auth:
            options_sw['proxy'] = proxy_auth                              # добавляем настройки прокси с аутентификацией
        elif proxy:
            option.add_argument('--proxy-server=%s' % proxy)  # добавляем настройки прокси

        # option.add_argument(f'user-agent={ua}')

        self.driver = webdriver.Chrome(
            service=chrome_service_path,
            options=option,
            seleniumwire_options=options_sw
        )

        stealth(
            self.driver,
            user_agent=ua,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        # self.driver.implicitly_wait(10)

    def get_html(self, url) -> str:

        with self.driver as WD:
            WD.get(url)
            time.sleep(1)
            WD.execute_script("document.body.style.zoom='100%'")
            html = WD.page_source
            time.sleep(10)

            if html:
                return html
            raise ConnectionError(f'Site response - {html}')

    # закрытие драйвера
    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def __del__(self):
        pass


def main():

    getter = HtmlGetter(headless='false')
    # html = getter.get_html('https://codepen.io/pen?layout=%EF%BB%BF')
    html = getter.get_html('https://antcpt.com/score_detector/')
    getter.close_driver()
    print(html)


if __name__ == '__main__':
    main()
