from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)
app.config['ENV'] = 'develoment'

# create a route docecater
'''
safe
upper
lower
capetlise
title
striptags
trim
'''


@app.route("/")
def hello():
    my_name = "shreshth"
    stuf = "This is bold"

    favorit_pizza = ['pepperoni', 'cheese', 'mushrooms', 41]
    return render_template("index.html", firstname=my_name, stuf=stuf, fav_pizza=favorit_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)


@app.errorhandler(404)
def not_found_error(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


app.run(debug=True)
