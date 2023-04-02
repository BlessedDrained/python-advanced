from flask import Flask, request, jsonify


app = Flask(__name__)
logs = []

@app.route('/logs', methods=['POST'])
def add_log():
    log_data = request.form.to_dict()
    logs.append(log_data)
    return '', 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

if __name__ == '__main__':
    app.run()