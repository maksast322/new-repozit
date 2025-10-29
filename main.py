from loguru import logger

from view import user_menu


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)
    user_menu()
    logger.info("Пользовательское меню выставленно")

    if __name__ == "__main__":
        main()
