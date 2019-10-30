
from snownlp import SnowNLP

s = SnowNLP(u'都闭嘴')

key =s.words # [u'这个', u'东西', u'真心',
# u'很', u'赞']

pos =s.tags # [(u'这个', u'r'), (u'东西', u'n'),
# (u'真心', u'd'), (u'很', u'd'),
# (u'赞', u'Vg')]

sentiment=s.sentiments

print(sentiment)