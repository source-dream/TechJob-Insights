<<<<<<< HEAD
from app import app, db
from app.models import Job
import json

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
=======
from app import  app

if __name__ == '__main__':
    app.run()
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
