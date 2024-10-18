import os
import random
import time
import asyncio
from telegram import Bot

# Задаем токен вашего бота
BOT_TOKEN = "your_bot_token"

# Задаем ID вашего канала или его имя с @
CHANNEL_ID = "-12345"

# Указываем путь к папке с изображениями
IMAGE_FOLDER_PATH = "images/"

# Интервал между постами в секундах (например, 3600 секунд — это 1 час)
# POST_INTERVAL = 3600  # Можно указать другое значение

# Создаем объект бота
bot = Bot(token=BOT_TOKEN)


# Создаем объект бота
bot = Bot(token=BOT_TOKEN)


def get_random_image(image_folder):
    """Функция для выбора случайного изображения из папки."""
    files = [
        f
        for f in os.listdir(image_folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".jfif", ".webp", ".mp4"))
    ]
    if not files:
        raise ValueError(
            "Папка пуста или не содержит изображений или видео с нужными расширениями."
        )
    return os.path.join(image_folder, random.choice(files))


async def post_image_to_channel(bot, channel_id, image_path):
    """Функция для публикации изображения в канал."""
    with open(image_path, "rb") as img:
        await bot.send_photo(chat_id=channel_id, photo=img)
    print(f"Изображение {image_path} отправлено в канал.")


async def main():
    """Основной цикл для регулярной отправки изображений."""
    # while True:
    try:
        # Выбираем случайное изображение
        image_to_post = get_random_image(IMAGE_FOLDER_PATH)

        # Отправляем изображение в канал
        await post_image_to_channel(bot, CHANNEL_ID, image_to_post)

        # Ждем перед следующим постом
        # await asyncio.sleep(POST_INTERVAL)

    except Exception as e:
        print(f"Ошибка: {e}")
        # В случае ошибки подождем немного перед следующей попыткой
        # await asyncio.sleep(60)


# Запуск событийного цикла для асинхронного кода
if __name__ == "__main__":
    asyncio.run(main())
