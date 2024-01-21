import numpy as np
import matplotlib.pyplot as plt
# загружаем класс WordCloud из библиотеки wordcloud
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import string 
from PIL import Image
async def word_cloud(text):
    text = text.lower()
    table = str.maketrans("", "", string.punctuation)
    text = text.translate(table)
    cake_mask = np.array(Image.open('Plan.png'))
    wc = WordCloud(stopwords = STOPWORDS, repeat=True, 
                   mask=cake_mask,
                   width = cake_mask.shape[1],
                   height = cake_mask.shape[1]).generate(text)
    file = "60874022.jpg"
    wc.to_file("60874022.jpg")
    return file 
 