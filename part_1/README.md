Перед початком роботи переконайтеся, що встановлені наступні компоненти:

- Python 3.x
- Бібліотека pymongo
- Бібліотека mongoengine

## Встановлення та налаштування

1. Склонуйте репозиторій проекту на свій локальний комп'ютер.
2. Встановіть необхідні залежності
3. Переконайтеся, що у вас є файли JSON з відповідними даними про авторів та цитати. Зробіть необхідні зміни у коді, щоб вказати правильний шлях до цих файлів.
4. Запустіть файл `main.py` для заповнення бази даних MongoDB авторами та їх цитатами.

## Використання

Після успішного заповнення бази даних можна виконувати пошук цитат за тегом, за ім'ям автора або набором тегів. Для цього запустіть скрипт finder.py який приймає команди у наступному форматі - команда: значення. 
Приклад:
name: Steve Martin — знайти та повернути список всіх цитат автора Steve Martin;
tag:life — знайти та повернути список цитат для тегу life;
tags:life,live — знайти та повернути список цитат, де є теги life або live (примітка: без пробілів між тегами life, live);
exit — завершити виконання скрипту;

Виведення результатів пошуку відбувается у форматі utf-8