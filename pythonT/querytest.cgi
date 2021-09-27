#! /usr/local/bin/python
# coding: utf-8

import cgi
import datetime
import jquerymobile_templete_engine

#-------------------------------------------------------------------------------
#タイトルの作成
#-------------------------------------------------------------------------------
def create_Title():
    return(u"入力を受け取ってみる")

#-------------------------------------------------------------------------------
#ヘッダの作成
#-------------------------------------------------------------------------------
def create_Header():
    return(u"入力を受け取ってみる")

#-------------------------------------------------------------------------------
#コンテンツの作成
#-------------------------------------------------------------------------------
def create_Content():

    #---------------------------------------------------
    #入力フォーム
    #---------------------------------------------------
    formarea = u"""
<form method="GET" action="querytest.cgi">
    <div data-role="fieldcontain">
        <input id="querytest_foo" name="foo" placeholder="入力して"/>
    </div>
</form>
"""
    #---------------------------------------------------
    #入力値処理
    #---------------------------------------------------
    content = u'''
<!--[S] 受け取ったパラメータ -->
入力は : %s
<!--[E] 受け取ったパラメータ -->
'''
    #受け取ったクエリ
    form = cgi.FieldStorage()
    #fooがないとエラーになっちゃうよ
    #param = form['foo'].value
    param = form.getvalue('foo','Not applicable')


    content = content % param.decode('utf-8')

    return(u"{0}{1}".format(formarea,content))

#-------------------------------------------------------------------------------
#フッタの作成
#-------------------------------------------------------------------------------
def create_Footer():
    now = datetime.datetime.now()
    strfooter = "%4d/%02d/%02d %02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)

    return (strfooter)

if __name__ == '__main__':

    #要素の作成
    str_Title   = create_Title()
    str_Header  = create_Header()
    str_Context = create_Content()
    str_Footer  = create_Footer()

    #HTMLファイルの書き出し
    print "Content-type: text/html¥n"
    print (jquerymobile_templete_engine.encodeHtml(str_Title, str_Header, str_Context, str_Footer))