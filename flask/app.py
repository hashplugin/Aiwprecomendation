from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "connected"})




if __name__ == '__main__':
    app.run(debug=True)
