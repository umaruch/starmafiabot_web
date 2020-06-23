import sys
import app
from config import HOST, PORT

try:
    if sys.argv[1] == "dropdb":
        print(app.drop_db())

    if sys.argv[1] == "start":
        app.app.run(
            host = HOST,
            port = PORT
        )
except IndexError:
    print("Попробуйте снова")