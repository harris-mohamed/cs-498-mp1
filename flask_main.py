from flask import Flask, request

app = Flask(__name__)

seed = 0

@app.post('/')
def seedPost():
    global seed
    seed = request.get_json()['seed']


@app.get('/')
def seedGet():
    global seed
    return f"{seed}"

if __name__ == '__main__':
    app.run()
