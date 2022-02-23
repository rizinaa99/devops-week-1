from flask import Flask
app= Flask(__name__)
@app.route('/')
def Hello():
  return "<h1>Hello, welcome</h1>"