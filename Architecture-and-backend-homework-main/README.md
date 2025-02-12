# Домашнее задание к уроку "Архитектура и серверная часть" 
## Цель

Научиться работать с линтером и форматтером `ruff`, применяя его к реальному проекту для улучшения качества кода.

## Задание

1. **Описание:**

В этом задании вы будете работать с реальным, но уже неиспользуемым, коммерческим проектом. В нем предварительно были удалены или заменены "чувствительные" данные (например токены, юзернеймы, пароли). Код проекта очень сильно далек от идеала (на самом деле он прямо ужасен и является наглядным примером того, как писать код не надо) и содержит множество проблем, которые могут быть выявлены и частично исправлены с помощью линтера и форматтера Ruff. Ваша задача — изучить код, разобраться с документацией [ruff](https://docs.astral.sh/ruff/), настроить его конфигурацию и применить линтер и форматтер к проекту.

2. **Инструкция:**

    * Склонируйте репозиторий проекта к себе на компьютер.
    * Установите менеджер пакетов `uv` (если у вас его нет): `curl -LsSf https://astral.sh/uv/install.sh | sh` для MacOS и Linux (подробнее о `uv` [здесь](https://docs.astral.sh/uv/))
    * Установите зависимости проекта: `uv sync` 
    * Установите `ruff`: `uv add ruff` (будет хорошо, если вы найдете способ добавить ruff в dev зависимости).
    * Изучите документацию `ruff`, обращая внимание на разделы о конфигурации, правилах, исправлениях и форматировании.
    * Создайте свою конфигурацию `ruff` используя `pyproject.toml`, который уже представлен в проекте.
    * Экспериментируйте с различными настройками `ruff`. Вы можете настроить его как очень строго (чтобы выявить максимальное количество проблем), так и более мягко (сосредоточившись на базовом форматировании и наиболее критичных ошибках).
    * Запустите `ruff` для анализа и форматирования кода:
        * `uv run ruff check` — для анализа кода и выявления проблем.
        * `uv run ruff format` — для форматирования.
    * Создайте свой публичный репозиторий и закоммитьте туда изменения, включая обновленный `pyproject.toml` и исправленный код.

P.S. Обратите внимание, что вам не нужно запускать сам код проекта (flask). Вы работаете только с кодом и его качеством.

3. **Что вам нужно прислать на проверку:**

    * Ссылка на ваш GitHub репозиторий с выполненным заданием.  Репозиторий должен содержать:
    * Исходный код проекта после применения Ruff и ваших ручных изменений.
    * Обновленный `pyproject.toml`, который содержит вашу конфигурацию `ruff`.
    * (Опционально) краткое описание в `README.md`, какие настройки вы использовали и почему, а также какие проблемы вы решили с помощью `ruff`.

## Благодарность

Большое спасибо за выполнение задания! Если у вас возникли вопросы или трудности, не стесняйтесь обращаться к вашему ментору. Вы также можете подписаться на мой телеграм-канал [Записки экспата-программиста](https://t.me/ExpatDevDiary) или написать мне лично в [тг](https://t.me/samoylovartem) - я всегда рад пообщаться про Python и программирование в целом. 
