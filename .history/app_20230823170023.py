from flask import Flask

# 创建 Flask 应用
app = Flask(__name__)


@app.route('/uploadSoundFile', methods=['POST'])
def getMsg():

    return 'this is a server'


# 启动应用
if __name__ == '__main__':
    app.run()
