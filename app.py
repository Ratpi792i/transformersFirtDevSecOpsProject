from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Transformers API</h1><p>DevSecOps Project</p>'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return jsonify({"input": data, "result": "prediction"})

@app.route('/models', methods=['GET'])
def models():
    return jsonify({"models": ["bert", "gpt2", "t5"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
