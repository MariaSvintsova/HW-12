def save_picture(picture):
    '''return path for uploaded picture'''
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path
