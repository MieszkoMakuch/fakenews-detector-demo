from flask import Flask, request, render_template, redirect, url_for

# from fakenews_detector.url_utils import format_url
# from fakenews_detector.main import check_news
from fakenews_detector_demo.article_analyzer import analyze_article

app = Flask(__name__)

# Debug logging
import logging
import sys

# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try:
    log.info('Logging to console')
except:
    _, ex, _ = sys.exc_info()
    log.error(ex.message)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles/show')
def show_article():
    url_to_clean = request.args.get('url_to_clean')
    if not url_to_clean:
        return redirect(url_for('index'))

    # Fake news
    article = analyze_article(url_to_clean, log)
    return render_template('article/index.html', article=article, url=url_to_clean)
