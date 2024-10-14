from flask import Flask


msg =  f"""muhahahaaa
"""

msg = msg.replace("\n","<br />")

app = Flask(__name__)
@app.route('/')
def main():
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1379)
