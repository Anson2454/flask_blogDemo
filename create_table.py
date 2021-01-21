from flaskr import create_app, db
from flaskr.models import *

app = create_app()
# 1. 在 with app.app_context() 中，执行 db.create_all()；
# 2. 调用 LocalStack 获取 Local 中的 app，再去 app 中获取配置
with app.app_context():
    # db.drop_all()
    db.create_all()
