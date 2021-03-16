import os

import gd
import nekitdev

HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 80)

app = gd.server.create_app()

gd.server.setup_gd_app_sync(app)

nekitdev.setup_app(app)

try:
    gd.server.run_app_sync(app, host=HOST, port=PORT)

except Exception:
    pass
