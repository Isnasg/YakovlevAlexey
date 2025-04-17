import unittest
from flask_testing import TestCase
from Lab2/Zad7 import app, storage


class FinanceAppTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Очищаем хранилище перед каждым тестом
        storage.clear()
        # Добавляем тестовые данные
        storage.update({
            2023: {
                5: {
                    15: 1000,
                    16: 2000
                },
                6: {
                    1: 1500,
                    2: 2500
                }
            },
            2024: {
                1: {
                    10: 3000
                }
            }
        })

    def test_add_expense_valid(self):
        with self.client:
            response = self.client.post('/add/20230520/5000')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Добавлена трата 5000 руб. за 20.5.2023", response.data)
            self.assertEqual(storage[2023][5][20], 5000)

    def test_add_expense_invalid_date_format(self):
        with self.client:
            response = self.client.post('/add/2023abc20/5000')
            self.assertEqual(response.status_code, 400)
            self.assertIn(b"Дата должна быть в формате YYYYMMDD", response.data)

    def test_add_expense_invalid_date_values(self):
        with self.client:
            response = self.client.post('/add/20231320/5000')
            self.assertEqual(response.status_code, 400)
            self.assertIn(b"Месяц должен быть от 1 до 12", response.data)

    def test_calculate_year_valid(self):
        response = self.client.get('/calculate/2023')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Суммарные траты за 2023 год: 7000 руб.", response.data)

    def test_calculate_year_no_data(self):
        response = self.client.get('/calculate/2025')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Нет данных за 2025 год", response.data)
        self.assertIn(b'"total": 0', response.data)

    def test_calculate_month_valid(self):
        response = self.client.get('/calculate/2023/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Суммарные траты за 5.2023: 3000 руб.", response.data)

    def test_calculate_month_no_data(self):
        response = self.client.get('/calculate/2023/3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Нет данных за 3.2023", response.data)
        self.assertIn(b'"total": 0', response.data)

    def test_add_negative_amount(self):
        response = self.client.post('/add/20230520/-100')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Сумма должна быть положительной", response.data)


if __name__ == '__main__':
    unittest.main()