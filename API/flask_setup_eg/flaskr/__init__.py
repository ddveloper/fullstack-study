from flask import Flask, jsonify, request
from models import setup_db, Question
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app) # CORS(app, resources={r"*/api/*": {origins: '*'}})
  
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    # @app.route('/')
    # # @cross_origin
    # def hello():
    #     return jsonify({'message': 'Hello API'})

    @app.route('/questions')
    def get_questions():
        page = request.args.get('page', 1, type=int)
        start = (page-1) * 10
        end = start + 10
        questions = Question.query.all()
        formatted_questions = [question.format() for question in questions]

        return jsonify({
            'success': True,
            'questions': formatted_questions[start:end],
            'total_questions': len(questions)
        })

    return app


# Default port:
if __name__ == '__main__':
    app = create_app()
    app.run()