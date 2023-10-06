import unittest
from tkinter import Tk
from unittest.mock import MagicMock
from main import FramedTextApp


class TestFramedTextApp(unittest.TestCase):

    def setUp(self):
        self.app = FramedTextApp("Test Text", width=800, height=600, initial_size=10)
        self.app.root.quit = MagicMock()
        self.event = MagicMock()

    def test_init(self):
        self.assertIsInstance(self.app.root, Tk)
        self.assertEqual(self.app.text, "Test Text")
        self.assertEqual(self.app.font_size, 10)
        self.assertEqual(self.app.width, 800)
        self.assertEqual(self.app.height, 600)

    def test_draw_frame(self):
        # Проверяем, что draw_frame рисует рамку и текст

        # Проверяем, что есть как минимум 3 элемента
        elements = self.app.canvas.find_all()
        self.assertEqual(len(elements), 3)

        # Проверяем, что первый и второй элемент - прямоугольник (рамка)
        self.assertEqual(self.app.canvas.type(elements[0]), "rectangle")
        self.assertEqual(self.app.canvas.type(elements[1]), "rectangle")

        # Проверяем, что третий элемент - текст
        self.assertEqual(self.app.canvas.type(elements[2]), "text")

    def test_key_press_handler_escape(self):
        # Проверяем, что при нажатии Escape приложение завершает работу

        self.event.keysym = 'Escape'
        self.app.key_press_handler(self.event)
        self.app.root.quit.assert_called_once()

    def test_key_press_handler_right(self):
        # Проверяем, что при нажатии Right увеличивается размер шрифта

        self.event.keysym = 'Right'
        initial_font_size = self.app.font_size

        self.app.key_press_handler(self.event)
        self.assertEqual(self.app.font_size, initial_font_size * 2)

    def test_key_press_handler_left(self):
        # Проверяем, что при нажатии Left уменьшается размер шрифта

        self.event.keysym = 'Left'
        initial_font_size = self.app.font_size

        self.app.key_press_handler(self.event)
        self.assertEqual(self.app.font_size, initial_font_size // 2)


if __name__ == '__test_main__':
    unittest.main()
