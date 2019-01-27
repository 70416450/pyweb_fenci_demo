#coding=utf-8
import web
import sys
import redis
import json
import math

sys.path.append("./")
import jieba
import jieba.posseg
import jieba.analyse

urls = (
    '/', 'index',
    '/test', 'test',
)

render = web.template.render('templates/')
web.template.Template.globals['render'] = render

config = web.storage(
            static = '/static',
            resource = '/resource'
            )
web.template.Template.globals['config'] = config

app = web.application(urls, globals())

class test:
    def GET(self):
        ret = '111'

        return ret


class index:
    def GET(self):
        print "111111111"
        return render.index_test('null', 'null', '100', '')


    def POST(self):
        param = web.input()
        print "==============="
        content = param['item_id']

        # tfidf
        result_list = []
        for x, w in jieba.analyse.extract_tags(content, withWeight=True):
            result_list.append(':'.join([x, str(round(w, 3))]))

        res_str = '<br>'.join(result_list)
        print "res_str: ", res_str

        # textrank
        result_textrank_list = []
        print "xxxxx"
        for x, w in jieba.analyse.textrank(content, withWeight=True):
            print "xxx:",x
            print "www:",w
            result_textrank_list.append(':'.join([x, str(round(w, 3))]))

        res_textrank_str = '<br>'.join(result_textrank_list)
        print "res_textrank_str: ", res_textrank_str





        if len(res_str) <= 0 or len(res_textrank_str) <= 0:
            return json.dumps({'block_one':'null', 'block_two':'null'},ensure_ascii=True, encoding='UTF-8')
        else:
            return json.dumps({'block_one':res_textrank_str, \
                    'block_two':res_str},ensure_ascii=True, encoding='UTF-8')






if __name__ == "__main__":
    app.run()
