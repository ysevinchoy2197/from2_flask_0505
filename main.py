#2-misol
from flask import Flask

app = Flask(__name__)

@app.route('/name')
def show_name():
    return f"Ismim Kamal"


@app.route('/age')
def show_age():
    return f"Yoshim 25 da"


@app.route('/city')
def show_city():
    return f"Toshkentda yashayman"


