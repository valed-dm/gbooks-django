# gbooks-django

В рамках ДЗ №10 создан отдельный репозиторий для Django проекта.
Активированы следующие GitHub Actions:
- Pylint
- Django CI

Pylint обнаружил около 400 несоответствий кода.
Для разрешения этих ошибок выполнены следующие действия:

- создан файл `.pylintrc`, куда были добавлены исключения для:
    - docstrings: C0114, C0115, C0116.
    - файла `manage.py`: C0415 import outside toplevel.
    - файла `api/tests/tests_views`: `E1101 instance of 'Book' has no '_meta' member`
    (первая ошибка `Class 'Book' has no 'objects' member (no-member)` 
    устранена установкой модуля django-pylint).
    - количества атрибутов класса `Book` из `api/schemas/book.py`: макс(7), факт(9).

Найдены 2 ошибки SOLID:

- R0904: too-many-public-methods (commit 82409bc5)
  - `library/tests/test_models.py` изменен для соответствия Single-responsibility principle (S of SOLID)
- W0221 argument-differ error (commit 28d2f2ef)
  - `api/tests/tests_api.py` изменен для соответствия Liskov Substitution Principle (L of SOLID)

Другие исправленные недостатки кода:

- удалены неиспользованные импорты, аргументы
- добавлен параметр timeout в request
- elif после return
- переименованы односимвольные переменные, использованные для упрощения восприятия кода при разработке
- исправлены ошибки при написании dataclasses: созданы поля для изменяемого словаря (`field(default_factory=lambda: [])`); 
  коммиты 731c23e5, 04009050
- устранен продублированный фрагмент кода `R0801: Similar lines in 2 files` коммит c3bbbf08, 
  создан новый файл `library/crud/save_book.py`
- pylint: R1721: unnecessary-comprehension list(book.categories) used instead коммит 0531cc0d
- мелкие ошибки при использовании f-strings.

Настройка Django CI с прохождением тестов прошла быстрее, все тесты Django успешно выполняются.

Необходима дополнительная настройка переменных окружения, которые я передал напрямую в yml-файлах:

 <https://www.paigeniedringhaus.com/blog/use-secret-environment-variables-in-git-hub-actions>

Аккаунт на <https://www.travis-ci.com/> не активировал (нужна valid credit card).
Создал аккаунт на <https://www.harness.io/> для общего знакомства с сервисом DevOps.