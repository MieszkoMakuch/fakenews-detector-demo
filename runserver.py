from fakenews_detector_demo import app
from fakenews_detector_demo.controllers import article

# update herokou git push heroku master

if __name__ == '__main__':
    app.register_blueprint(article.mod)
    app.run(debug=True, host='127.0.0.1', port=5001)
