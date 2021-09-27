#! /usr/local/bin/python
# coding: utf-8

import cgi
import datetime
import jquerymobile_templete_engine

#-------------------------------------------------------------------------------
#年号と、開始年を返す
#-------------------------------------------------------------------------------
def japanese_era(year):
    startyear = 0
    eraname = ""
    #ここから近代
    if year >= 1989:
        eraname = u"平成"
        startyear = 1989
    elif year >= 1926:
        eraname = u"昭和"
        startyear = 1926
    elif year >= 1912:
        eraname = u"大正"
        startyear = 1912
    elif year >= 1868:
        eraname = u"明治"
        startyear = 1868

    #ここから江戸時代
    elif year >= 1865:
        eraname = u"慶応"
        startyear = 1865
    elif year >= 1864:
        eraname = u"元治"
        startyear = 1864
    elif year >= 1861:
        eraname = u"文久"
        startyear = 1861
    elif year >= 1860:
        eraname = u"万延"
        startyear = 1860
    elif year >= 1855:
        eraname = u"安政"
        startyear = 1855
    elif year >= 1848:
        eraname = u"嘉永"
        startyear = 1848
    elif year >= 1845:
        eraname = u"弘化"
        startyear = 1845
    elif year >= 1831:
        eraname = u"天保"
        startyear = 1831
    elif year >= 1818:
        eraname = u"文政"
        startyear = 1818
    elif year >= 1804:
        eraname = u"文化"
        startyear = 1804
    elif year >= 1801:
        eraname = u"享和"
        startyear = 1801
    elif year >= 1789:
        eraname = u"寛政"
        startyear = 1789
    elif year >= 1781:
        eraname = u"天明"
        startyear = 1781
    elif year >= 1772:
        eraname = u"安永"
        startyear = 1772
    elif year >= 1764:
        eraname = u"明和"
        startyear = 1764
    elif year >= 1751:
        eraname = u"宝暦"
        startyear = 1751
    elif year >= 1748:
        eraname = u"寛延"
        startyear = 1748
    elif year >= 1744:
        eraname = u"延享"
        startyear = 1744
    elif year >= 1741:
        eraname = u"寛保"
        startyear = 1741
    elif year >= 1736:
        eraname = u"元文"
        startyear = 1736
    return (startyear, eraname)

#-------------------------------------------------------------------------------
#タイトルの作成
#-------------------------------------------------------------------------------
def create_Title():
    return(u"西暦を和暦に")

#-------------------------------------------------------------------------------
#ヘッダの作成
#-------------------------------------------------------------------------------
def create_Header():
    return(u"西暦を和暦に")

#-------------------------------------------------------------------------------
#コンテンツの作成
#-------------------------------------------------------------------------------
def create_Content():

    #---------------------------------------------------
    #入力フォーム
    #---------------------------------------------------
    content_form=u'''
<!--[S] 入力フォームを追加 -->
%s
<!--[E] 入力フォームを追加 -->
'''

    #入力フォーム部分の作成
    content_form_value = u'''
<form method="GET" action="japanese_eraname.cgi">
    <div data-role="fieldcontain">
        <label for="japanese_era_year">年：</label>
        <input id="japanese_era_year" name="year" type="number" placeholder="西暦"/>
    </div>
</form>
    '''

    content_form = content_form % content_form_value

    #---------------------------------------------------
    #年齢早見表パネル
    #---------------------------------------------------
    content_panel = u'''
<div data-role="collapsible">
    <h3>年齢早見表(誕生日が来れば)</h3>
<!--[S] 年齢早見表 -->
%s
<!--[E] 年齢早見表 -->
</div>
'''

    #年齢早見表の作成
    agelist=""
    startyear = 0
    eraname = ''

    for i in range(0, 400):
        year=datetime.datetime.today().year-i
        #年号の取得
        startyear,eraname = japanese_era(year)
        agelist += u'<p>[{0}年({1}{2:3d})] ({3:3d}歳)</p>\n'.format(datetime.datetime.today().year-i, eraname, (year-startyear)+1, i)

    content_panel = content_panel % agelist

    #---------------------------------------------------
    #入力値処理
    #---------------------------------------------------
    content = ""
    year=datetime.datetime.today().year

    #入力値の取得
    form = cgi.FieldStorage()
    year_str = form.getvalue('year', '')

    #入力値の適正をチェック
    if False == year_str.isdigit():
        content += u"西暦を入力してください。入力値: %s" % year_str.decode('utf-8')
        content += "<br/>"
    else:
        year = int(year_str)

    #---------------------------------------------------
    #和暦の計算
    #---------------------------------------------------
    startyear,eraname = japanese_era(year)
    content += (u"%d年は 　: " % year) + u"{0} {1:3d}年".format(eraname, (year-startyear)+1)
    content += "<br/>"
    content +=   u"誕生日が来れば{0:3d}才".format(datetime.datetime.today().year-year)
    content += "<br/>"

    return(u"{0}<br/>{1}<br/>{2}<br/>".format(content_form, content,content_panel))

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