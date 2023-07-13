import sys

from dotenv import load_dotenv

from kaeliumbot.bot import bot
from kaeliumbot.container import Container


def main() -> int:
    load_dotenv()
    container = Container()
    settings = container.settings()

    bot.token = settings.telegram_bot_token
    if bot.get_webhook_info().url:
        print("removing webhook...")
        bot.remove_webhook()

    try:
        bot.infinity_polling(restart_on_change=True)
    except KeyboardInterrupt:
        pass

    if len(sys.argv) > 1 and sys.argv[1] == "set-wh":
        print("setting webhook...")
        bot.set_webhook(url=settings.api_gateway_url)
    return 0


if __name__ == "__main__":
    exit(main())
