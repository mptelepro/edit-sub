import logging
from config import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await client.send_message(
               chat_id=message.chat.id,
               text="""<b>```HEY There, I'M FORCE SUB BOT 😃```
`PLEASE CLICK` /help</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "➕️ ADD ME ➕️", url="t.me/Jin_Jin_robot?startgroup=true"),
                                        InlineKeyboardButton(
                                            "CHANNEL", url="https://t.me/mpazaanbots")
                                    ],[
                                      InlineKeyboardButton(
                                            "GROUP", url="https://t.me/mpazaanbot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️PLAY', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)+1):
        url = "https://github.com/DamienSoukara/FSub-Heroku"
        button = [
            [InlineKeyboardButton(text = '🗣 Support Chat', url="https://t.me/munnipopz")],
            [InlineKeyboardButton(text = '🤖 Source Code', url=url)],
            [InlineKeyboardButton(text = '◀️BACK', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️BACK', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️PLAY', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
