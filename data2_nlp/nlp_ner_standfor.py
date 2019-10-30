from stanfordcorenlp import StanfordCoreNLP

# 命名实体识别ner 中文中的应用，一定记得下载中文jar包，并标志lang=‘zh’
nlp = StanfordCoreNLP(
    r'C:\Users\lwang.leiwang\.m2\repository\edu\stanford\nlp\stanford-corenlp\3.9.2\stanford-corenlp-3.9.2.jar',
    lang='zh')
sentence = '清华大学位于北京。'
print(nlp.word_tokenize(sentence))
print(nlp.pos_tag(sentence))
print(nlp.ner(sentence))
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))
