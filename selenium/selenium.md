# Selenium

## Driver

```
browser.title

browser.page_source

browser.current_url
```

## Remote

### driver.py
```
import abc
import time

import urllib3
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BaseDriverFactory(abc.ABC):
    @abc.abstractmethod
    def get_webdriver(self) -> WebDriver: ...


class ChromeDriverFactory(BaseDriverFactory):
    host = 'chrome'
    port = '4444'

    @classmethod
    def get_webdriver(cls):
        options = webdriver.ChromeOptions()
        return webdriver.Remote(
            f"http://{cls.host}:{cls.port}",
            options=options,
        )


def get_driver() -> WebDriver:
    while True:
        try:
            driver = ChromeDriverFactory.get_webdriver()
        except urllib3.exceptions.MaxRetryError:
            time.sleep(.1)
        else:
            return driver
```

### docker-compose.yml
```
version: '3.8'
services:
  selenium_learning:
    build: .
    image: 'selenium_learning:1'
    container_name: 'selenium_learning'
    command: >
      sh -c "cd src &&
             poetry run python3 run.py"
    networks:
      - backend
    restart: unless-stopped
    depends_on:
      - chrome

  chrome:
    image: selenium/standalone-chrome:latest
    networks:
      - backend
    ports:
      - '4444:4444'
      - '7900:7900'
    privileged: true
    shm_size: 2g

```

## Quit | Close

```
driver.quit() - quit browser

driver.close() - close window
```

## Elem

```
elem.send_keys()

elem.send_keys(Keys.RETURN | Keys.ENTER)

elem.clear()

elem.submit()

elem.click()
```

## History

```
elem.back()

elem.forward()
```

## Cookie

```
driver.add_cookie({'name': 'any', 'value': 'any'})

driver.get_cookies()
```

## Location

```
XPATH, CSS_SELECTOR
```

## Drag and Drop

```
from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```

## Waits

```
# explicit - wait elem 10 seconds then time error
WebdriverWait(driver, 10).until(ec.<method>())

# implicit - wait 10 seconds
driver.implicitly_wait(10)
```

## Page Design Pattern

```
# all opearations in page
page = MainPage(self.driver)
```

## Functional Tests

```
SetUp and TearDown - DRY friends

SetUp and TearDown for each function not class
```