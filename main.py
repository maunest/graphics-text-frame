import tkinter as tk


class FramedTextApp:
    def __init__(self, initial_text, width=800, height=600, initial_size=10):
        self.root = tk.Tk()

        # Устанавливаем размер холста и начальные значения
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(expand=True, fill='both')

        self.text = initial_text
        self.font_size = initial_size
        self.draw_frame()

        self.root.bind('<KeyPress>', self.key_press_handler)

    def draw_frame(self):
        # Вычисляем начальные координаты
        frame_width = len(self.text) * self.font_size + 10
        frame_height = 3 * self.font_size
        x = (self.width - frame_width) // 2
        y = (self.height - frame_height) // 2

        # Очищаем холст
        self.canvas.delete("all")

        # Рисуем рамку и текст
        self.canvas.create_rectangle(x, y, x + frame_width, y + frame_height, outline="black")
        self.canvas.create_rectangle(x - frame_width * 0.02, y - frame_height * 0.1, x + frame_width * 1.02,
                                     y + frame_height * 1.1, outline="black")
        self.canvas.create_text(x + frame_width // 2, y + frame_height // 2, text=self.text,
                                font=("Arial", self.font_size))

    def key_press_handler(self, event):
        if event.keysym == 'Escape':
            self.root.quit()
        if event.keysym == 'Right':
            self.font_size *= 2
            self.draw_frame()
        if event.keysym == 'Left' and self.font_size > 1:
            self.font_size //= 2
            self.draw_frame()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    initial_text = "Hello, World!"
    app = FramedTextApp(initial_text)
    app.run()

