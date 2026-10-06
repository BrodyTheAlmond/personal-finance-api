import os
from app.__init__ import create_app

# FLASK_ENV in your .env controls which config is loaded
app = create_app(os.environ.get("FLASK_ENV", "development"))

if __name__ == "__main__":
    app.run()