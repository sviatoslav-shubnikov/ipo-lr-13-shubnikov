from PIL import Image
from datetime import datetime

class ImageHandler:
    def __init__(self, image_path):
        """Инициализация с путем к изображению."""
        self.image_path = image_path
        self.image = None

    def load_image(self):
        """Загрузка изображения по указанному пути."""
        self.image = Image.open(self.image_path)
        print(f"Изображение успешно загружено: {self.image_path}")

    def save_image(self, output_path, format=None):
        """Сохранение изображения по указанному пути и формату."""
        if self.image:
            self.image.save(output_path, format=format)
            print(f"Изображение сохранено как: {output_path}")
        else:
            print("Сначала загрузите изображение!")

    def resize_image(self, new_size):
        """Изменение размера изображения."""
        if self.image:
            self.image = self.image.resize(new_size)
            print(f"Размер изображения изменен на: {new_size}")
        else:
            print("Сначала загрузите изображение!")

    def scale_image_50_percent(self):
        """Масштабирование изображения до 50% от исходного размера."""
        if self.image:
            original_size = self.image.size
            new_size = (original_size[0] // 2, original_size[1] // 2)
            self.image = self.image.resize(new_size)
            print(f"Изображение масштабировано до 50%: новый размер {new_size}")
        else:
            print("Сначала загрузите изображение!")

    def save_image_with_date(self, output_path_prefix, format=None):
        """Сохранение изображения с добавлением текущей даты к имени файла."""
        if self.image:
            date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_path = f"{output_path_prefix}_{date_str}.jpg"
            self.image.save(output_path, format=format)
            print(f"Изображение сохранено как: {output_path}")
        else:
            print("Сначала загрузите изображение!")

    def get_image_for_processing(self):
        """Передача изображения для обработки в ImageProcessor."""
        if self.image:
            return self.image.copy()
        else:
            print("Сначала загрузите изображение!")
            return None