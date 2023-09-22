import os

class Config:
    # 其他配置参数...
    
    # SQLite数据库连接URI，示例为SQLite数据库文件
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')