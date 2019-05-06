import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
from googletrans import Translator
translator = Translator()
with open('tmp1','r') as f:
    for line in f:
        # print translator.translate('co-founder', dest='zh-CN',src='en')
        a=translator.translate(line, dest='zh-CN',src='en')
        print line.strip(),getattr(a,"text")