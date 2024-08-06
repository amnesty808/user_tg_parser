# User Tg Parser

Этот Python-скрипт находит всех участников писавших в указанный чат, так же выводит участников писавших определенные слова(по фильтру) и запсывает их в `user_info.txt` и `user_info_filter.txt`.

## Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/amnesty808/mirror-checker.git
    cd user_tg_parser
    ```

2. Установите зависимости:
    ```bash
    pip install pyrogram
    ```
    
3. Подставить свои данные:
    ```python
    api_id = #you_id_id
    api_hash = #"you_hash_api"
    link = #"tg_linl"
    filter_words = ["word1", "word2", "word3", ...]
    ```
    
4. Запустите скрипт:
    ```bash
    python userTGbot.py
    ```
