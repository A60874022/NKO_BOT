import mongoengine as me


class Topic(me.Document):
    title = me.StringField(min_length=3,
                           verbose_name='Название статьи (кнопки)')
    description = me.StringField(multiline=True, verbose_name='Текст статьи')
    image = me.FileField(verbose_name='Изображение')
