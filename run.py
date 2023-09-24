from app import app, db
from app.Scraper.scraper import run

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    run()
    app.run()
    