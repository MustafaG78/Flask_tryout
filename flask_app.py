from flask import Flask

app= Flask(__name__)

if __name__ == "_main_":
    app.run(port=5000,debug=True)

@app.route('/')
def home():
    return '<p>Ik hoop dat ik het opdracht goed heb uitgevoerd!<p>'


