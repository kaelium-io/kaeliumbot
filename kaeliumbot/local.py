from bot import bot
from container import Container
import sys


def main() -> int:
    container = Container()
    container.config.from_ini("config.ini")
    bot.token = container.config.bot.token()
    if bot.get_webhook_info().url:
        print("removing webhook...")
        bot.remove_webhook()

    try:
        bot.infinity_polling(restart_on_change=True)
    except KeyboardInterrupt:
        pass

    if len(sys.argv) > 1 and sys.argv[1] == "set-wh":
        print("setting webhook...")
        bot.set_webhook(url=container.config.bot.api_gw_url())
    return 0


if __name__ == "__main__":
    exit(main())
