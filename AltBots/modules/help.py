from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f"β ππ½π€π©π¨ πππ‘π₯ πππ£πͺ β\n\nΒ» **α΄ΚΙͺα΄α΄ α΄Ι΄ Κα΄Κα΄α΄‘ Κα΄α΄α΄α΄Ι΄κ± κ°α΄Κ Κα΄Κα΄**\nΒ» **α΄α΄α΄ α΄Κα΄α΄α΄Κ: @PyXen**"


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  "https://te.legra.ph/file/07d39b85c6cea32f15259.jpg",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("β’ κ±α΄α΄α΄ β’", data="spam"),
            Button.inline("β’ Κα΄Ιͺα΄ β’", data="raid"),
           ],
           [
            Button.inline("β’ α΄xα΄Κα΄ β’", data="extra"),
           ],
           [    
            Button.url("β’ α΄Κα΄Ι΄Ι΄α΄Κ β’", "https://t.me/TheAltron"),
            Button.url("β’ sα΄α΄α΄α΄Κα΄ β’", "https://t.me/AltronChats")
           ],
           ],
           )


extra_msg = f"""
**Β» α΄xα΄Κα΄ α΄α΄α΄α΄α΄Ι΄α΄κ±:**

π¨ππ²πΏππΌπ: α΄κ±α΄ΚΚα΄α΄ α΄α΄α΄κ±
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

ππ°π΅πΌ: α΄α΄ α΄α΄α΄Ιͺα΄ α΄ α΄α΄Κα΄ α΄Ι΄ α΄Ι΄Κ α΄κ±α΄Κ
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

ππ²π?ππ²: α΄α΄ Κα΄α΄α΄ α΄ Ι’Κα΄α΄α΄/α΄Κα΄Ι΄Ι΄α΄Κ
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**Β© @PyXen**
"""

                 
raid_msg = f"""
**Β» Κα΄Ιͺα΄ α΄α΄α΄α΄α΄Ι΄α΄κ±:**

π₯π?πΆπ±: α΄α΄α΄Ιͺα΄ α΄α΄α΄κ± Κα΄Ιͺα΄ α΄Ι΄ α΄Ι΄Κ ΙͺΙ΄α΄Ιͺα΄ Ιͺα΄α΄α΄Κ α΄κ±α΄Κ κ°α΄Κ Ι’Ιͺα΄ α΄Ι΄ Κα΄Ι΄Ι’α΄.
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

π₯π²π½πΉππ₯π?πΆπ±: α΄α΄α΄Ιͺα΄ α΄α΄α΄κ± Κα΄α΄ΚΚ Κα΄Ιͺα΄ α΄Ι΄ α΄Κα΄ α΄κ±α΄Κ!!
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

ππ₯π²π½πΉππ₯π?πΆπ±: α΄α΄α΄α΄α΄Ιͺα΄ α΄α΄α΄κ± Κα΄α΄ΚΚ Κα΄Ιͺα΄ α΄Ι΄ α΄Κα΄ α΄κ±α΄Κ!!
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

ππππ’π: Κα΄α΄ α΄ Κα΄Ιͺα΄ α΄Ι΄ α΄Κα΄ α΄κ±α΄Κ!!
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

ππππ’π: κ±Κα΄Κα΄ΚΙͺ Κα΄Ιͺα΄ α΄Ι΄ α΄Κα΄ α΄κ±α΄Κ!!
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

ππππ’π: α΄Κα΄α΄ Κα΄Ιͺα΄ α΄Ι΄ α΄Κα΄ α΄κ±α΄Κ!!
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**Β© @PyXen**
"""

spam_msg = f"""
**Β» κ±α΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄κ±:**

π¦π½π?πΊ: κ±α΄α΄α΄κ± α΄ α΄α΄κ±κ±α΄Ι’α΄.
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

π£πΌπΏπ»π¦π½π?πΊ: α΄α΄Κα΄α΄Ι’Κα΄α΄ΚΚ κ±α΄α΄α΄.
  1) {hl}pspam <count>

ππ?π»π΄: κ±α΄α΄α΄κ± Κα΄Ι΄Ι’ΙͺΙ΄Ι’ α΄α΄κ±κ±α΄Ι’α΄ κ°α΄Κ Ι’Ιͺα΄ α΄Ι΄ α΄α΄α΄Ι΄α΄α΄Κ.
  1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)


** Β© @PyXen**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("β’ κ±α΄α΄α΄ β’", data="spam"),
            Button.inline("β’ Κα΄Ιͺα΄ β’", data="raid"),
           ],
           [
            Button.inline("β’ α΄xα΄Κα΄ β’", data="extra"),
           ],
           [
            Button.url("β’ α΄Κα΄Ι΄Ι΄α΄Κ β’", "https://t.me/TheAltron"),
            Button.url("β’ sα΄α΄α΄α΄Κα΄ β’", "https://t.me/AltronChats")
           ],
           ],
        )           
   else:
        await event.answer("Make Your Own Altron Bots !! @PyXen", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(spam_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            ) 
   else:
        await event.answer("Make Your Own Altron Bots !! @PyXen", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )  
     else:
        await event.answer("Make Your Own Altron Bots !! @PyXen", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
   else:
        await event.answer("Make Your Own Altron Bots !! @PyXen", cache_time=0, alert=True)
