#coding=utf-8
import web
import sys
import redis
import json
import math

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


test_dict = {'aaa':'111', 'bbb':'222'}
test2_dict = {'aaa':'444', 'bbb':'555'}


class index:
    def GET(self):
        print "111111111"
        return render.index_test('null', 'null', '100', '')


    def POST(self):
        param = web.input()
        print "==============="
        item_id= param['item_id']
        print item_id
        if item_id not in test_dict:
            return json.dumps({'block_one':'null', 'block_two':'null'},ensure_ascii=True, encoding='UTF-8')
        else:
            print test_dict[item_id]
            print test2_dict[item_id]
            return json.dumps({'block_one':test_dict[item_id], 'block_two':test2_dict[item_id]},ensure_ascii=True, encoding='UTF-8')






if __name__ == "__main__":
    app.run()
