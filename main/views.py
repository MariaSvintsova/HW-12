import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import *


messages_blueprint = Blueprint('messages_blueprint', __name__, template_folder='templates')

@messages_blueprint.route('/')
def main_page():
    return render_template('index.html')

@messages_blueprint.route('/search/')
def search_page():
    """View of search page (search by word)"""
    word = request.args.get('word', '')
    logging.info('Запускаю поиск по слову')
    try:
        posts = search_posts_by_word(word)
    except FileNotFoundError:
        logging.error('Загруженный файл нe найден')
        return 'Файл не найден'
    except JSONDecodeError:
        raise
        # return 'Не валидный файл, не превращаеться в список'
    return render_template('post_list.html', posts=posts, word=word)


