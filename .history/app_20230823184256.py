from flask import Flask, request, jsonify
import os
# 创建 Flask 应用
app = Flask(__name__)

token = ''


@app.route('/userToken', methods=['POST'])
def userToken():
    if eval(request.data)['token']:
        global token
        token = request.data
        print(eval(token)['token'])
        return jsonify({'code': 0})
    return jsonify({'code': 1})


@app.route('/uploadSoundFile', methods=['POST'])
def upload_sound_file():
    sound_file = request.files['file']
    u_path = eval(token)['token']+'/'
    if sound_file and u_path != '/':
        os.makedirs()
        file_path = 'sound_file/' + \
            u_path + sound_file.filename
        sound_file.save(file_path)
        return jsonify({'code': 0})
    return jsonify({'code': 1})


@app.route('/test')
def api_test():
    print(eval(token)['token'])
    return jsonify({'state': 'sussesful'})


# 启动应用
if __name__ == '__main__':
    app.run()
