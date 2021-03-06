import jieba

txt = open('D:\\Edge浏览器下载\\沉默的羔羊.txt', encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) >= 2:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print("{:^10}：{:>5}".format(word, count))
