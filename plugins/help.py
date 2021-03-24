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
               text="""<b>Hey There, I'm Telegraph Bot
I can upload photos or videos to telegraph. Made by @munnipopz 😃
Hit help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/munnipopz")
                                    ],[
                                      InlineKeyboardButton(
                                            "Source Code", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Client.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Client.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!
Just send a photo or video less than 5mb file size, I'll upload it to telegraph.
~ @Infinity_BOTs</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Client.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Client.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>
<b>♞ Developer:</b> <a href="https://t.me/munnipopz</a>
<b>♞ Support:</b> <a href="https://t.me/munnipopz">Infinity BOTs Support</a>
<b>♞ Library:</b> <a href="https://t.me/munnipopz">Pyrogram</a>
<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code", url="https://t.me/munnipopz")
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
        reply_markup = InlineKeyboardMarkup(map(4)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help'))

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
            [InlineKeyboardButton(text = '🤓OWNER🤓', url="https://t.me/Mpazaan")]
        ]
    elif(pos==len(tr.HELP_MSG)-2):
        url = "https://t.me/mpazaanbot"
        button = [
            [InlineKeyboardButton(text = '➕️ ADD ME TO YOUR GROUP ➕️', url="t.me/ForceSubscriber_robot?startgroup=true")], [InlineKeyboardButton(text = '😈SUPPORT CHAT😈', url="https://t.me/mpazaanbot")],
            [InlineKeyboardButton(text = '🤖SOURCE CODE🤖', url=url)],
            [InlineKeyboardButton(text = '😆HELP😆', callback_data = f"help+{pos-1}")],
            [InlineKeyboardButton(text = '😂NO OPEN😀', callback_data = f"start+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '😇FIRST😇', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '😈SECOND😈', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
