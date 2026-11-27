from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ

app = Flask(__name__)


# 1. プロジェクトのトップ
@app.route('/')
def index():
    return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
    return render_template('janken_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():
    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    if not name:
        name = "名無しさん"

    # <input type="radio" ... name="hand">
    hand = request.form.get("hand", None)

    # リストの中からランダムに選ぶ
    cpu = random.choice(["rock", "scissor", "paper"])

    # じゃんけん処理
    if hand == cpu:
        result_message = "あいこ"
    else:
        if hand == "rock":
            if cpu == "scissor":
                result_message = "{} の勝ち".format(name)
            else:
                result_message = "{} の負け".format(name)
        elif hand == "scissor":
            if cpu == "paper":
                result_message = "{} の勝ち".format(name)
            else:
                result_message = "{} の負け".format(name)
        elif hand == "paper":
            if cpu == "rock":
                result_message = "{} の勝ち".format(name)
            else:
                result_message = "{} の負け".format(name)
        else:
            result_message = "後出しはダメです。"

    return render_template('janken_play.html', result_message=result_message, name=name, hand=hand, cpu=cpu)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8348, debug=True)