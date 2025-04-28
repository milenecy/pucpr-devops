from flask import Flask, request, jsonify

app = Flask(__name__)

def soma(a, b):
    return a + b

@app.route("/soma")
def somar():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        resultado = soma(a, b)
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
