import glob
from pathlib import Path
from utils import load_plugins
import logging
import asyncio
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "AltBots/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\nšššØš­š¬ ššš©š„šØš²šš šš®šššš¬š¬šš®š„š„š² ā”\nMy Master ---> @šš²ššš§")


async def main():
    await X1.run_until_disconnected()
    await X2.run_until_disconnected()
    await X3.run_until_disconnected()
    await X4.run_until_disconnected()
    await X5.run_until_disconnected()
    await X6.run_until_disconnected()
    await X7.run_until_disconnected()
    await X8.run_until_disconnected()
    await X9.run_until_disconnected()
    await X10.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
