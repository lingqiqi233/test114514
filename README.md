代码在上面文件里

软件222康健

基于 jieba 库的中文文本处理程序文档

一、程序实现的功能

分词：将输入的中文文本分割成单个词语，便于后续处理。

词频统计：统计每个词语在文本中出现的次数，了解文本中词汇的使用频率。

词性分类保存：对文本中的词语进行词性标注，将相同词性的词语归类并保存到文本文件中。

可视化：

饼状图：展示文本中出现频率最高的若干词语及其占比。

柱状图：直观呈现高频词语及其对应的词频。

关系图：简单模拟高频词语之间的关系，以可视化的方式展示词语关联。

词云：以图形化方式展示文本中词语的频率，频率越高的词语在词云中显示越大。

自定义词典：允许用户手动添加自定义词语及其词性和词频，提高分词准确性。

实体统计保存：

人名统计：从文本中识别并统计人名，保存到文本文件。

地名统计：识别并统计文本中的地名，保存结果。

武器统计：识别并统计与武器相关的词语，保存统计结果。

二、设计思想

模块化设计：将各个功能封装成独立的函数，便于代码的维护、扩展和复用。

数据处理流程：首先对输入文本进行分词，基于分词结果进行词频统计、词性分类、实体识别等操作。对于可视化功能，根据统计后的数据生成相应图表。

简单规则匹配：在人名、地名和武器统计功能中，采用简单的规则匹配方式。例如，通过常见姓氏和特定词性识别人名，根据词性识别地名，通过关键词匹配识别武器。

三、用到主要的函数介绍

jieba.lcut()：精确模式分词，将文本分割成词语列表，是整个文本处理流程的基础。

collections.Counter()：用于统计可迭代对象中元素的出现次数，方便进行词频统计。

jieba.posseg.lcut()：在分词的同时进行词性标注，为词性分类和实体识别提供支持。

matplotlib.pyplot：用于生成饼状图和柱状图，通过设置图表属性展示数据。

pyecharts.charts：包含 Pie（饼图）、Bar（柱状图）、Graph（关系图）类，生成交互式可视化图表，以更直观的方式呈现数据。

wordcloud.WordCloud：生成词云图，通过设置字体、背景颜色等参数展示文本中词语的频率分布。

jieba.add_word()：用于添加自定义词语到 jieba 词典中，提高分词对特定领域词汇的处理能力。

四、测试数据

使用示例文本 “赵先生今天去了北京，在那里他看到了一些人拿着刀剑，感觉很危险。” 进行测试。该文本包含人名、地名和武器相关词汇，能有效测试程序各项功能。

五、输出结果

分词结果：展示文本经过 jieba 分词后的词语列表，如 [' 赵先生 ', ' 今天 ', ' 去 ', ' 北京 ', '，', ' 在 ', ' 那里 ', ' 他 ', ' 看到 ', ' 一些 ', ' 人 ', ' 拿着 ', ' 刀剑 ', '，', ' 感觉 ', ' 很 ', ' 危险 ', '。'] 。

词频统计结果：以字典形式呈现每个词语的出现次数，如 {' 赵先生 ': 1, ' 今天 ': 1, ' 去 ': 1, ' 北京 ': 1, ' 在 ': 1, ' 那里 ': 1, ' 他 ': 1, ' 看到 ': 1, ' 一些 ': 1, ' 人 ': 1, ' 拿着 ': 1, ' 刀剑 ': 1, ' 感觉 ': 1, ' 很 ': 1, ' 危险 ': 1}。

词性分类保存：将词语按词性分类保存到pos_tagging.txt文件中，例如nr: 赵先生 、ns: 北京 。

可视化结果：

饼状图：在word_frequency_pie.html文件中展示高频词语的占比情况。

柱状图：在word_frequency_bar.html文件中展示高频词语及其词频的对比。

关系图：在word_relation_graph.html文件中以图形形式展示高频词语间的简单关系。

词云：生成wordcloud.png图片，展示文本中词语的频率分布。

实体统计保存：

人名统计：将识别出的人名保存到person_names.txt文件，内容为 “赵先生”。

地名统计：将识别出的地名保存到place_names.txt文件，内容为 “北京”。

武器统计：将识别出的武器相关词汇保存到weapon_names.txt文件，内容为 “刀剑”。
