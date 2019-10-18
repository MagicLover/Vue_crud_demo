import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Flask web开发',
        'author': '米格尔 格林贝格',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': '流畅的python',
        'author': 'Luciano Ramalho',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'python编程从入门到实践',
        'author': 'Eric Matthes',
        'read': True
    }
]


@app.route('/ping', methods=['GET'])
def ping_pong():
    """测试前后端对接"""
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    """获取书籍列表 添加书籍"""
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


def remove_book(book_id):
    """根据uuid删除书籍"""
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
