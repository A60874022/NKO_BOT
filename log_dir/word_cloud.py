import string 
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
from collections import Counter


async def word_cloud(text):
    """Функция построения облаков слов"""
    text = text.lower()
    table = str.maketrans("", "", string.punctuation)
    text = text.translate(table)
    word_counts = Counter(text.split(" ")).keys()
    d = " ".join(word_counts)
    cake_mask = np.array(Image.open('Plan.png'))
    wc = WordCloud(mask=cake_mask,
                   max_words=10).generate(d)
    image_colors = ImageColorGenerator(cake_mask)
    wc.recolor(color_func=image_colors)
    file = "60874022.jpg"
    wc.to_file("60874022.jpg")
    return file

 