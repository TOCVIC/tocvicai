from flask import Flask
from flask import render_template

app = Flask(__name__)


# sets app route and renders file
@app.route('/')
def takeCommand():
   return render_template('index.html')


# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/takeCommand")
# def home():
#     return render_template("index.html")
#
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
#
#
#
# #
# if __name__ == "__main__":
# 	app.run(debug=True)
#
#
# # from flask import Flask, render_template
# #
# # app = Flask(__name__)
# #
# # @app.route("/")
# # def home():
# #     return render_template("home.html")
