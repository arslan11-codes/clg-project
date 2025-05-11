# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello from Cloud Run!'

# if __name__ == '__main__':
#     # IMPORTANT: Cloud Run expects the app to listen on 0.0.0.0:8080
#     app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    team_members = ["Arslan", "Muneer", "Mahima", "Shakshi"]
    return render_template('home.html', team=team_members)

@app.route('/blog')
def blog():
    return render_template('blog.html')  # Blog content will go here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
