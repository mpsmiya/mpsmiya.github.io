#! /usr/local/bin/python
# coding: utf-8

import cgi
import datetime
import jquerymobile_templete_engine

#-------------------------------------------------------------------------------
#タイトルの作成
#-------------------------------------------------------------------------------
def create_Title():
    return(u"13日の金曜日検索")

#-------------------------------------------------------------------------------
#ヘッダの作成
#-------------------------------------------------------------------------------
def create_Header():
    return(u"13日の金曜日検索")

#-------------------------------------------------------------------------------
#コンテンツの作成
#-------------------------------------------------------------------------------
def create_Content():

    #---------------------------------------------------
    #入力フォーム部分の作成
    #---------------------------------------------------
    context_form=u'''
<form method="GET" action="input_find13friday.cgi">
    <div data-role="fieldcontain">
　　　<label for="year">西暦：</label>
  　　　<select name="year" data-native-menu="false">
         <option>選択してください。</option>
         <optgroup label="西暦">
<!-- [S]年項目 -->
%s
<!-- [E]年項目 -->
         </optgroup>
　　　　</select>
      </label>
    </div>
    <div data-role="fieldcontain">
     <input type="submit" value="SUBMIT" />
    </div>
</form>
'''

    #年項目
    context_form_value = ""
    for i in range(datetime.datetime.today().year-10,datetime.datetime.today().year+10):
       context_form_value = context_form_value + u'<option value="%d">%d年</option>\n' % (i,i)

    context_form = context_form % context_form_value

    #---------------------------------------------------
    #コンテンツ部分
    #---------------------------------------------------
    content = ""
    friday13count=0
    year=datetime.datetime.today().year

    #入力値取得チェック
    form = cgi.FieldStorage()
    year_str = form.getvalue('year', '')

    #数値かチェック
    if False == year_str.isdigit():
        #unicode文字が入った場合にデコードする
        content += "<br/>" + "\n"
        content += u"西暦を入力してください。入力値: %s" % year_str.decode('utf-8')
        content += "<br/>" + "\n"
    else:
        year = int(year_str)

    #13日の金曜日を計算
    for month in range(1,13):
        date = datetime.date(year, month, 13)
        if date.weekday() == 4:
            friday13count += 1
            content += u"%4d/%2d/13: 金曜日です" %(year, month)
            content += "<br/>" + "\n"

    #結果の表示
    content += "<br/>" + "\n"
    if 0 == friday13count:
        content += u"%d年には13日の金曜日はありません" % year
    else:
        content += u"%d年には13日の金曜日が %d日あります" % (year, friday13count)

    return(u"{0}<br/>{1}<br/>".format(context_form,content))

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