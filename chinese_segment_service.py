from flask import Flask, request, jsonify
from LAC import LAC

app = Flask(__name__)


@app.route('/v1/segment', methods=['GET', 'POST'])
def text_segment():
    query = get_query('query')
    if query == '':
        return jsonify({
            'code': 400,
            'msg': 'query is empty',
            'data': ''
        })
    lac = LAC(mode='seg')
    words = lac.run(query)
    return jsonify({
        'code': 200,
        'msg': 'success',
        'data': words
    })


@app.route('/v1/lac', methods=['GET', 'POST'])
def text_lac():
    query = get_query('query')
    if query == '':
        return jsonify({
            'code': 400,
            'msg': 'query is empty',
            'data': ''
        })
    lac = LAC(mode='lac')
    words = lac.run(query)
    return jsonify({
        'code': 200,
        'msg': 'success',
        'data': {
            'words': words[0],
            'tags': words[1]
        }
    })


@app.route('/v1/rank', methods=['GET', 'POST'])
def text_rank():
    query = get_query('query')
    if query == '':
        return jsonify({
            'code': 400,
            'msg': 'query is empty',
            'data': ''
        })
    lac = LAC(mode='rank')
    words = lac.run(query)
    return jsonify({
        'code': 200,
        'msg': 'success',
        'data': words
    })


def get_query(arg_name):
    query = request.args.get(arg_name, '', type=str)
    if query == '':
        query = request.form.get(arg_name, '', type=str)
    if query == '':
        query = request.json.get(arg_name, '', type=str)
    return query


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
