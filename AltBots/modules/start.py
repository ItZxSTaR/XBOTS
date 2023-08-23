from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒", data="help_back")
    ],
    [
      Button.url("𝐍𝐄𝐓𝐖𝐎𝐑𝐊", "https://t.me/THE_WEBNET_NETWORK"),
      Button.url("𝐆𝐑𝐎𝐔𝐏", "https://t.me/WEB_NET_CHATMASTI")
      Button.url("𝐂𝐎𝐍𝐓𝐀𝐂𝐓", "https://t.me/WEBNET_CONTACT_BOT")
      Button.url("𝐅𝐄𝐃𝐄𝐑𝐀𝐓𝐈𝐎𝐍", "https://t.me/WEBNET_FED")
    ],
    [
        Button.url("𝐑𝐄𝐏𝐎", "https://github.com/DARKRAVANREPO/DARKRAVANWBNSPAM")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [DARK RAVAN](https://t.me/Dark_Ravan_01)**\n\n"
        TEXT += f"» **POWERED BY​ : [@WEBNET_NETWORK](https://t.me/THE_WEBNET_NETWORK)**\n\n"
        TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/05cc2603544685a5f6592.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
