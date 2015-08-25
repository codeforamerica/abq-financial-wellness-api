from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'This is the api for ABQ Financial Wellness Wizard'

if __name__ == '__main__':
  app.run()
