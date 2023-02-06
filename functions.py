import json


def load_posts():
    """Return data from json"""
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts_by_word(word):
    """return list of posts by word"""
    spisok = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            spisok.append(post)
    return spisok


def add_posts(post):
    '''return new(added) post'''
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
