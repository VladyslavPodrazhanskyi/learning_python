# Основной алгоритм создания юнит тестов:
# 1) Импорт модуля unittest и тестируемой функции.
# 2) Создание класса, кот. будет тестировать  функцию, кот наследуется от класса
# unittest.TestCase
# 3) В этом классе прописываются методы тестирования, название должно начинаться с test_
# 3.1. Внутри метода создается фикстура (значение функции или экземпляр класса с зад. параметрами
# 3.2. self.assert - проверочный метод, который принимает фикстуру и ожидаемое значение.
# 4. unittest.main() - функция, кот. запускает все тестовые методы, кот. начинаются с test_

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""
    def test_first_last_name(self):
        """Does names like Igor Pogorelko work properly?"""
        formatted_name = get_formatted_name("igor", "pogorelko")
        self.assertEqual(formatted_name, "Igor Pogorelko")

    def test_first_middle_last_name(self):
        """Does names like Elena Anatolievna vasilieva worl properly?"""
        formatted_name = get_formatted_name("Elena", "vasilieva", "Anatolievna")
        self.assertEqual(formatted_name, "Elena Anatolievna Vasilieva")

if __name__ == "__main__":
    unittest.main()   # Любой метод, имя которого начинается с test_ , будет выполняться автоматически при запуске