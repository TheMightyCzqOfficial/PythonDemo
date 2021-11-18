import jieba
import jieba.posseg as pseg
import jieba.analyse as anls


if __name__ == '__main__':
    # 全模式
    seg_list = jieba.cut("他来到上海交通大学", cut_all=True)
    print("【全模式】：" + "/ ".join(seg_list))

    # 精确模式
    seg_list = jieba.cut("他来到上海交通大学", cut_all=False)
    print("【精确模式】：" + "/ ".join(seg_list))

    # 返回列表
    seg_list = jieba.lcut("他来到上海交通大学", cut_all=True)
    print("【返回列表】：{0}".format(seg_list))

    # 搜索引擎模式
    seg_list = jieba.cut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")
    print("【搜索引擎模式】：" + "/ ".join(seg_list))

    # 返回列表
    seg_list = jieba.lcut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")
    print("【返回列表】：{0}".format(seg_list))

    # 未启用 HMM
    seg_list = jieba.cut("他来到了网易杭研大厦", HMM=False)  # 默认精确模式和启用 HMM
    print("【未启用 HMM】：" + "/ ".join(seg_list))

    # 识别新词
    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认精确模式和启用 HMM
    print("【识别新词】：" + "/ ".join(seg_list))

    # 基于 TF-IDF 算法的关键词提取
    s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
    for x, w in anls.extract_tags(s, topK=20, withWeight=True):
        print('%s %s' % (x, w))

    # TextRank 是另一种关键词提取算法，基于大名鼎鼎的 PageRank
    for x, w in anls.textrank(s, withWeight=True):
        print('%s %s' % (x, w))

    # 标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法
    words = pseg.cut(s)
    for word, flag in words:
        print("{0} {1}".format(word, flag))