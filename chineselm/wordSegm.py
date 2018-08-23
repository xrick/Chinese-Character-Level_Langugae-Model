import jieba
import logging

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level = logging.INFO)

    jieba.set_dictionary('dict.txt.tw.big')
    
    stopwordset = set()
    with open('stop_words.txt','r',encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    output = open('wiki_seg.txt','w')

    texts_num = 0

    with open('wiki_zh_tw.txt','r') as content :
        for line in content:
            words = jieba.cut(line,cut_all=False)
            for word in words:
                if word not in stopwordset:
                    output.write(word + ' ')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("has processed %d rows' word segment. " % texts_num)

    output.close()

if __name__ == '__main__':
    main()