from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = {}

@app.route('/inventory', methods=['POST'])
def add_item():
    item = request.json
    inventory[item['id']] = item
    return jsonify(item), 201

@app.route('/inventory/<item_id>', methods=['GET'])
def get_item(item_id):
    item = inventory.get(item_id, None)
    if item:
        return jsonify(item), 200
    return jsonify({'error': 'Item not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
