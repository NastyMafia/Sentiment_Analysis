from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Hello WordCloud"
wc = WordCloud().generate(text)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()