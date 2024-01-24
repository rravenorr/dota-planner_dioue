from app import InitApp
from os import path
import os

# Assuming InitApp is the function that initializes your Flask app
app = InitApp()

# Use the app context to perform database operations
with app.app_context():
    from app.models import db

    # Create the necessary tables
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
