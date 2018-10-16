from flask import Flask, render_template, request
import json
from pprint import pprint


# Flask　オブジェクトのインスタンス化
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("create_event.html")

# 「Room作成」ボタン押下時の処理
@app.route('/create_room', methods=['POST'] )
def create_room():
    pprint(request.data.decode('utf-8'))  # request.data ・・・ templateから送られてくるデータを取得
    #  ~~~~~~~
    #  request.data で取得したデータをもとに、Teams Room を作成する関数を実行
    #  返却値は result(処理が成功したか失敗したか), message(画面に表示するメッセージ), roomid(作成されたteamsのroomid)　←仮
    #  ~~~~~~~
    return json.dumps(dict(result=True, message='正常にルームが作成されました', roomid='xxxxxxxxxxxx'))

# 「送信 & インバイト作成」ボタン押下時の処理
@app.route('/create_event', methods=['POST'] )
def create_event():
    pprint(request.data.decode('utf-8'))
    #  ~~~~~~~
    #  request.data で取得したデータをもとに、DB登録 / URL作成 の関数を実行
    #  返却値は result(処理が成功したか失敗したか), message(画面に表示するメッセージ), URL　←仮
    #  ~~~~~~~
    return json.dumps(dict(result=True, message='イベント入力URLが作成されました', URL='http://sample.com/xxxxxxxxxxxxx'))


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
