from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("create_event.html")

@app.route('/create_room', methods=['POST'])
def get_teams_member():
    data="OK"
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
