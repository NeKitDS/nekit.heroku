import os

import gd
import gdbot
import nekit_site

# get credentials
BOT_TOKEN = os.getenv("BOT_TOKEN")
GD_USER = os.getenv("GD_USER")
GD_PASSWORD = os.getenv("GD_PASSWORD")

# create a loop
LOOP = gd.utils.acquire_loop()

# attach bot running task
LOOP.create_task(gdbot.run_bot(BOT_TOKEN, GD_USER, GD_PASSWORD, LOOP))

# attach site running task
LOOP.create_task(nekit_site.run_async())

try:
    LOOP.run_forever()

finally:
    gd.utils.shutdown_loop(LOOP)
