from image import ImageHandler, ImageProcessor


def menu():
    handler = None
    processor = None

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Загрузить изображение")
        print("2. Масштабировать изображение до 50%")
        print("3. Сохранить изображение с текущей датой")
        print("4. Применить фильтр к изображению")
        print("5. Добавить водяной знак")
        print("6. Показать изображение")
        print("7. Сохранить обработанное изображение")
        print("8. Выйти из программы")

        res = input("\nВыберите пункт из предложенного списка: ")

        if res == "1":
            image_path = input("Введите путь к изображению: ")
            handler = ImageHandler(image_path)
            handler.load_image()

        elif res == "2":
            if handler and handler.image:
                handler.scale_image_50_percent()
            else:
                print("Сначала загрузите изображение!")

        elif res == "3":
            if handler and handler.image:
                output_prefix = input("Введите префикс для сохранения файла: ")
                handler.save_image_with_date(output_prefix)
            else:
                print("Сначала загрузите изображение!")

        elif res == "4":
            if handler and handler.image:
                image_for_processing = handler.get_image_for_processing()
                if image_for_processing:
                    processor = ImageProcessor(image_for_processing)
                    filter_type = input("Введите тип фильтра (BLUR, CONTOUR, DETAIL, SHARPEN, EDGE_ENHANCE, EMBOSS): ").strip().upper()
                    processor.apply_filter(filter_type)
            else:
                print("Сначала загрузите изображение!")

        elif res == "5":
            if processor and processor.image:
                watermark_text = input("Введите текст водяного знака (по умолчанию 'Вариант 5'): ").strip() or "Вариант 5"
                processor.add_watermark(watermark_text)
            else:
                print("Сначала примените фильтр или загрузите изображение для обработки!")

        elif res == "6":
            if processor and processor.image:
                processor.show_image()
            elif handler and handler.image:
                handler.image.show()
            else:
                print("Сначала загрузите изображение или обработайте его!")

        elif res == "7":
            if processor and processor.image:
                save_path = input("Введите путь для сохранения обработанного изображения: ")
                processor.get_image().save(save_path)
                print(f"Изображение сохранено как: {save_path}")
            else:
                print("Сначала обработайте изображение!")

        elif res == "8":
            print("Выход из программы.")
            break

        else:
            print("Неправильный выбор, попробуйте снова.")

if __name__ == "__main__":
    menu()