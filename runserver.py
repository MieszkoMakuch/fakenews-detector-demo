from newspaperdemo import app
from newspaperdemo.controllers import article

if __name__ == '__main__':
    app.register_blueprint(article.mod)
    app.run(debug=True, host='127.0.0.1', port=5001)
