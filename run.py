from app import app, db
from app.models import Job
import json

if __name__ == '__main__':
    # 创建数据库
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, port=6002)
