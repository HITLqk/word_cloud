from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
"""
# 准备文本数据
text = "Thank you so much for your speech.In recent years, personality tests such as MBTI have frequently appeared in workplace recruitment. More and more companies have begun to include relevant content in interviews, and even use it in job adjustments and promotions. Is it reasonable to use the MBTI personality test as a rigid assessment standard for corporate recruitment? Thanks you for your question. First of all, we need to make it clear that personality tests have certain reference value in the recruitment process, but they cannot be used as a rigid screening standard. Although they can help us understand certain characteristics of an individual, they cannot fully reflect a person's ability and quality. Over-reliance on personality tests to screen applicants may ignore the applicant's actual ability and experience, causing companies to miss out on outstanding candidates with potential and talent. An excellent team is often composed of individuals with different backgrounds and characteristics, and their complementarity and collaboration drive team development. Therefore, when recruiting, companies should comprehensively consider multiple factors such as the applicants' professional skills, work experience, and growth experience to select outstanding talents that meet their needs."

# 创建WordCloud对象
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 使用matplotlib显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()
"""


with open("text2.txt",encoding="utf-8") as f:
    s = f.read()
print(s)
ls = jieba.lcut(s) # 生成分词列表
ls = [word for word in ls if len(word)>4]
text = ' '.join(ls) # 连接成字符串
stopwords = ["的","是","了"] # 去掉不需要显示的词

wc = WordCloud(font_path="msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color='white',
                         max_words=100,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("中文词云图2.png") # 保存词云文件


