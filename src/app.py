from flask import Flask,render_template
import socket
import nltk;
# nltk.download()
from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize
from flask import jsonify
from flask import request
import onetimepass as otp

app = Flask(__name__)

@app.route("/")
def index():
    text = request.args.get("text")
    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return jsonify(sentences)

@app.route("/download")
def download():
    print('Downloading')
    nltk.download()
    # sentences = nltk.sent_tokenize(text)
    # sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # sentences = [nltk.pos_tag(sent) for sent in sentences]
    return jsonify('Downlaoded')

@app.route("/2fa")
def download():
    key = request.args.get("key")
    my_token = otp.get_totp(key)
    # sentences = nltk.sent_tokenize(text)
    # sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # sentences = [nltk.pos_tag(sent) for sent in sentences]
    return jsonify(my_token)
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
