import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from loader.utils import save_picture
from functions import *

new_blueprint = Blueprint('new_blueprint', __name__, template_folder='templates')


@new_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')

@new_blueprint.route('/post', methods=['POST'])
def add_posts_Post_uploaded():
    '''
    user gives picture and content for new post

    checking if user doesn't give content or picture

    checking file for extension

    trying to give a path for uploaded post

    error FileNotFoundError handling

    checking the file for validity

    adding new dictionary with new post in posts.json

    return template of html with new post
    '''
    pict = request.files.get('picture')
    cont = request.form.get('content')

    if not pict or not cont:
        return 'Не добавлены текст или картинка'
    if pict.filename.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
        logging.info('Загруженный файл не картинка')
        return 'Файл неверного расширения'
    try:
        picture_path = '/' + save_picture(pict)

    except FileNotFoundError:
        logging.error('Загруженный файл нe найден')
        return 'Файл не ннайден'
    except JSONDecodeError:
        return 'Не валидный файл, не превращаеться в список'

    post = add_posts({'pic': picture_path, 'content': cont})
    return render_template('post_uploaded.html', post=post)


