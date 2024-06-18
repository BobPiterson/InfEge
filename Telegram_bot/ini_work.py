import configparser

# создать экземпляр
config = configparser.ConfigParser()
# прочитать файл .ini
config.read('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/InfEge/Telegram_bot/bot.ini')
# read values from a section
token = config.get("default", "Token")
print(token)