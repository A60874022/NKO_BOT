import mongoengine as db


class User(db.Document):
    name = db.StringField(max_length=40, required=True)
    password = db.StringField(max_length=60, required=True)
   


class Topic(db.Document):
    
    title = db.StringField(min_length=3,
                           verbose_name='Название статьи (кнопки)')
    description = db.StringField(multiline=True, verbose_name='Текст статьи')
    image = db.FileField(verbose_name='Изображение')