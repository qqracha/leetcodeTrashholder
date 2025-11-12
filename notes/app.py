from flask import Flask, request, jsonify, abort

app = Flask(__name__)
items = []
_id = 1

@app.route('/items', methods=['GET','POST','OPTIONS'])
def items_root():
    global _id
    if request.method == 'GET':
        return jsonify(items)
    if request.method == 'POST':
        data = request.get_json()
        data['id'] = _id
        _id += 1
        items.append(data)
        return jsonify(data), 201
    return '', 204

@app.route('/items/<int:item_id>', methods=['GET','PUT','PATCH','DELETE'])
def item(item_id):
    it = next((x for x in items if x['id']==item_id), None)
    if not it:
        abort(404)
    if request.method == 'GET':
        return jsonify(it)
    if request.method == 'PUT':
        data = request.get_json()
        data['id'] = item_id
        idx = items.index(it)
        items[idx] = data
        return jsonify(data)
    if request.method == 'PATCH':
        data = request.get_json()
        it.update(data)
        return jsonify(it)
    if request.method == 'DELETE':
        items.remove(it)
        return '', 204

if __name__ == '__main__':
    app.run(port=3000)
