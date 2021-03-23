import logging
from config import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(3)),
        reply_to_message_id=message.message_id
        )

def map(pos):
    if(pos==3):
        button = [
            [InlineKeyboardButton(text = '🗣 FIRST', url="https://t.me/mpazaanbots")]
            [InlineKeyboardButton(text = '🗣 FRIST', url="https://t.me/munnipopz")]
            [InlineKeyboardButton(text = '🗣 FIRST', url="https://t.me/mpazaanbot")]
        ]


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(4)),
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
            [InlineKeyboardButton(text = '🤓OWNER🤓', url="https://t.me/Mpazaan")]
        ]
    elif(pos==len(tr.HELP_MSG)-2):
        url = "https://t.me/mpazaanbot"
        button = [
            [InlineKeyboardButton(text = '😈SUPPORT CHAT😈', url="https://t.me/mpazaabot")],
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
