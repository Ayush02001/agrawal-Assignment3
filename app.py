from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Hello from ayush agrawal's GCP assignment is done!'

app.run(host='0.0.0.0')
