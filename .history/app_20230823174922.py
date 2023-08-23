from flask import Flask, request, jsonify

# 创建 Flask 应用
app = Flask(__name__)

token = ''


@app.route('/userToken', methods=['POST'])
def userToken():
    if eval(request.data)['token']:
        global token
        token = request.data
        print(eval(token)['token'])
        return jsonify({'tokenState': 'Yes'})
    return jsonify({'tokenState': 'No'})


@app.route('/uploadSoundFile', methods=['POST'])
def upload_sound_file():
    sound_file = request.files['file']
    # if sound_file:

    return 'this is a server'


@app.route('/test')
def api_test():
    print(eval(token)['token'])
    return jsonify({'state': 'sussesful'})


# 启动应用
if __name__ == '__main__':
    app.run()
