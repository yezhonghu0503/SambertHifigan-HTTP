from flask import Flask, request, jsonify

# 创建 Flask 应用
app = Flask(__name__)

token = ''


@app.route('/userToken', methods=['POST'])
def userToken():
    token = request.data
    print(token)
    return jsonify({'msg': 'yes'})


@app.route('/uploadSoundFile', methods=['POST'])
def upload_sound_file():
    sound_file = request.files['file']
    # if sound_file:

    return 'this is a server'


# 启动应用
if __name__ == '__main__':
    app.run()
