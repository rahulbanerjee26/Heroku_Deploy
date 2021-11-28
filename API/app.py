from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Testing Automatic Deploy'

if __name__ == '__main__':
    app.run(debug=True)

# https://github.com/timanovsky/subdir-heroku-buildpack
# PROJECT_PATH