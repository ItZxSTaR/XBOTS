import sys
import logging
import importlib
from pathlib import Path
from config import SUDO_USERS


def load_plugins(plugin_name):
    path = Path(f"AltronX/modules/{plugin_name}.py")
    name = "AltronX.modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["AltronX.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)

async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)
