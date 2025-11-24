from datetime import datetime
from loguru import logger
from cryptography.fernet import Fernet
from view import user_menu, answer_with_result
from model import write, read


def controller():
    KEY = Fernet.generate_key()
    cipher = Fernet(KEY)
    logger.info("Контроллер запущен")

    def encrypt(text, cipher):
        return cipher.encrypt(text.encode()).decode()

    def decrypt(text, cipher):
        return cipher.decrypt(text.encode()).decode()

    while True:
        data = read()
        line = user_menu()
        logger.info(f"В переменной line: {line}")

        result = None

        if line[1] == 1:
            result = encrypt(line[0], cipher)
            answer_with_result(result)
        elif line[1] == 2:
            try:
                result = decrypt(line[0], cipher)
                answer_with_result(result)
            except Exception as e:
                logger.error(f"Ошибка при расшифровке: {e}")
                answer_with_result("Ошибка расшифровки")
        elif line[1] == 3:
            break
        else:
            logger.error("Пользователь выбрал не 1 и не 2!")

        if result is not None:
            data.update({f"{datetime.now()}": result})
            write(data)
