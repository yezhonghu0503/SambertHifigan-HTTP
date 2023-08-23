from flask import Flask

# 创建 Flask 应用
app = Flask(__name__)

# 定义一个简单的路由
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 启动应用
if __name__ == '__main__':
    app.run()
