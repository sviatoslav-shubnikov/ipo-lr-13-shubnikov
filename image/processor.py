from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        """Инициализация с изображением для обработки."""
        self.image = image

    def apply_filter(self, filter_type):
        """Применение фильтра к изображению."""
        if self.image:
            filters = {
                'BLUR': ImageFilter.BLUR,
                'CONTOUR': ImageFilter.CONTOUR,
                'DETAIL': ImageFilter.DETAIL,
                'SHARPEN': ImageFilter.SHARPEN,
                'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
                'EMBOSS': ImageFilter.EMBOSS
            }
            if filter_type in filters:
                self.image = self.image.filter(filters[filter_type])
                print(f"Фильтр '{filter_type}' применен.")
            else:
                print(f"Фильтр '{filter_type}' не найден. Доступные фильтры: {list(filters.keys())}")
        else:
            print("Нет изображения для обработки!")

    def add_watermark(self, text="Вариант 5"):
        """Добавление водяного знака в правом нижнем углу изображения."""
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font_size = max(20, min(self.image.size) // 20)
            font = ImageFont.truetype("arial.ttf", font_size)

            text_width, text_height = draw.textsize(text, font)
            position = (self.image.size[0] - text_width - 10, self.image.size[1] - text_height - 10)

            # Добавление полупрозрачного водяного знака
            watermark = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
            watermark_draw = ImageDraw.Draw(watermark)
            watermark_draw.text(position, text, font=font, fill=(255, 255, 255, 128))
            self.image = Image.alpha_composite(self.image.convert("RGBA"), watermark)
            print(f"Водяной знак '{text}' добавлен в правый нижний угол.")
        else:
            print("Нет изображения для обработки!")

    def show_image(self):
        """Отображение изображения."""
        if self.image:
            self.image.show()
        else:
            print("Нет изображения для отображения!")

    def get_image(self):
        """Возврат обработанного изображения."""
        return self.image