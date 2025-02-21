from flask import Flask, request

app = Flask(__name__)

@app.route('/collect', methods=['POST'])
def collect():
    data = request.json
    print(f"[+] Données reçues : {data}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5999)
