import jieba
import jieba.posseg as pseg
from collections import Counter
import matplotlib.pyplot as plt
from pyecharts.charts import Pie, Bar, Graph
from wordcloud import WordCloud
import re
import os


# 分词功能
def word_segmentation(text):
    return jieba.lcut(text)


# 词频统计功能
def word_frequency(words):
    return dict(Counter(words))


# 词性分类并保存为txt功能
def save_pos_tagging(text, file_path='pos_tagging.txt'):
    words = pseg.lcut(text)
    pos_dict = {}
    for word, flag in words:
        pos_dict.setdefault(flag, []).append(word)

    with open(file_path, 'w', encoding='utf-8') as f:
        for pos, words_list in pos_dict.items():
            f.write(f"{pos}: {', '.join(words_list)}\n")


# 读取txt文件生成饼状图可视化功能
def generate_pie_chart(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = word_segmentation(text)
    freq = word_frequency(words)
    top_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:top_n]
    labels = [word for word, _ in top_words]
    values = [count for _, count in top_words]

    pie = Pie()
    pie.add("", [list(z) for z in zip(labels, values)])
    pie.render('word_frequency_pie.html')


# 柱状图可视化功能
def generate_bar_chart(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = word_segmentation(text)
    freq = word_frequency(words)
    top_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:top_n]
    labels = [word for word, _ in top_words]
    values = [count for _, count in top_words]

    bar = Bar()
    bar.add_xaxis(labels)
    bar.add_yaxis("词频", values)
    bar.render('word_frequency_bar.html')


# 关系图可视化功能（简单模拟，假设词频高的词之间有关系）
def generate_relation_graph(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = word_segmentation(text)
    freq = word_frequency(words)
    top_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:top_n]

    nodes = [{"name": word, "symbolSize": count} for word, count in top_words]
    links = []
    for i in range(len(top_words)):
        for j in range(i + 1, len(top_words)):
            links.append({"source": top_words[i][0], "target": top_words[j][0]})

    graph = Graph()
    graph.add("", nodes, links)
    graph.render('word_relation_graph.html')


# 词云可视化功能
def generate_word_cloud(text, file_path='wordcloud.png'):
    wordcloud = WordCloud(font_path='simhei.ttf', background_color='white').generate(' '.join(word_segmentation(text)))
    wordcloud.to_file(file_path)


# 建立人工手动自定义词典功能
def add_custom_dict(custom_dict):
    for word, freq, pos in custom_dict:
        jieba.add_word(word, freq=freq, tag=pos)


# 统计人名并保存txt功能（简单基于词性和常见姓氏匹配）
def save_person_names(text, file_path='person_names.txt'):
    words = pseg.lcut(text)
    person_names = []
    common_surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']  # 简单示例，可扩充
    for word, flag in words:
        if flag == 'nr' and word[0] in common_surnames:
            person_names.append(word)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(', '.join(person_names))


# 统计地名并保存txt功能（简单基于词性匹配）
def save_place_names(text, file_path='place_names.txt'):
    words = pseg.lcut(text)
    place_names = [word for word, flag in words if flag == 'ns']
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(', '.join(place_names))


# 统计武器并保存txt功能（简单基于关键词匹配）
def save_weapon_names(text, file_path='weapon_names.txt'):
    weapon_keywords = ['枪', '炮', '刀', '剑', '弓箭']  # 简单示例，可扩充
    words = word_segmentation(text)
    weapon_names = [word for word in words if any(keyword in word for keyword in weapon_keywords)]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(', '.join(weapon_names))


if __name__ == "__main__":
    # 示例文本
    sample_text = "赵先生今天去了北京，在那里他看到了一些人拿着刀剑，感觉很危险。"

    # 分词
    seg_words = word_segmentation(sample_text)
    print("分词结果:", seg_words)

    # 词频统计
    word_freq = word_frequency(seg_words)
    print("词频统计结果:", word_freq)

    # 词性分类保存
    save_pos_tagging(sample_text)

    # 生成饼状图
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(sample_text)
    generate_pie_chart('test.txt')

    # 生成柱状图
    generate_bar_chart('test.txt')

    # 生成关系图
    generate_relation_graph('test.txt')

    # 生成词云
    generate_word_cloud(sample_text)

    # 自定义词典
    custom_dict = [("自定义词", 100, "n")]
    add_custom_dict(custom_dict)

    # 统计人名保存
    save_person_names(sample_text)

    # 统计地名保存
    save_place_names(sample_text)

    # 统计武器保存
    save_weapon_names(sample_text)