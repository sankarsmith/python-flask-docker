from flask import Flask,render_template
import socket
import nltk;
from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    text = request.args.get("text")
    try:
        sentences = nltk.sent_tokenize(text)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        return jsonify(sentences)
    except:
        return render_template('error.html')
@app.route("/test")
def indexnew():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
