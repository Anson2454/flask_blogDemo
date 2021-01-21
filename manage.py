from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskr import create_app, db

app = create_app()
manager = Manager(app)  # 利用 app 进行 Manager 实例化
migrate = Migrate(app, db)  # 利用 app 和 db 进行 Migrate 的实例化；db 中有数据库的相关操作
# 定义了一个 "db" 的命令； flask-migrate 依赖于 flask-script
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()  # 启动程序改为 manager.run()
