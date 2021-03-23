import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")        
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(1575148105)
	SUDO_USERS = list(set(SUDO_USERS))
        
class Messages():
      HELP_MSG = [
        ".",

        "[🔔](https://i.imgur.com/SmqQApH.jpg) **FORCE SUBSCRIBE :**\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "[⚙](https://i.imgur.com/ItAdRVF.jpg) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.",
        
        "[⚙](https://i.imgur.com/LnOEiTK.jpg) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[👨‍💻](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) **DEVELOPED BY @AmineSoukara**"
      ]

      START_IMG = "https://telegra.ph/file/dd451b9d186d65a2187d5.jpg"

      START_MSG = "**Hey! [👋](https://i.imgur.com/SmqQApH.jpg) [{}](tg://user?id={})**\n\n● I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help"

      else:
             first_name = update.effective_user.first_name
             update.effective_message.reply_photo(START_IMG,PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name), OWNER_ID),reply_markup=InlineKeyboardMarkup(
                                                 [[InlineKeyboardButton(text="Help",url="t.me/{}?start=help".format(bot.username)),InlineKeyboardButton(text=" 👥 channel.",url="https://t.me/Mothirajinn_bot")],  
                                                 [InlineKeyboardButton(text="Creater",url="https://t.me/Mothirajinn_bot"),InlineKeyboardButton(text="Mai Source",url="https://t.me/Mothirajinn_bot")]]),disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

