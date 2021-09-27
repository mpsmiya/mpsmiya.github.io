#! /usr/local/bin/python
# coding: utf-8

import json, urllib2
import METRO_API
import html_convert

#URLを指定する
url=''
url = url + 'https://api.tokyometroapp.jp/api/v2/'
url = url + 'datapoints?rdf:type=odpt:TrainInformation'
url = url + '&'
url = url + 'acl:'+METRO_API.Metro_api_Const.ACL

#データ取得
root = METRO_API.getMetroAPI(url)

#htmlを出力
html_body = u"""
<html>
<style>
div {
        text-align: center;
}
table {
	border-collapse: collapse;
        align="center"
}
td {
        text-align: center;
	border: solid 1px;
	padding: 0.5em;
}
</style>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>運行情報</title>
</head>
<body>
%s
</body>
</html>
"""


#路線名のみ抜き出し
content = ""
content = content + u"<div>" + "\n"
content = content + u'<table align="center">' + "\n"
tag_sTD="<td>"
tag_eTD="</td>"

content = content + u"<tr>"
content = content + html_convert.tagconvert(u"路線名称")
content = content + html_convert.tagconvert(u"更新時刻")
content = content + html_convert.tagconvert(u"運行情報")
content = content + u"</tr>"+ "\n"

for elements in root:

    content = content + u"<tr>"
    keyList = elements.keys()

    keyName = ''
    column =''
    #-------------------------------------------------------
    #路線名称
    keyName='odpt:railway'
    column =''
    if elements.has_key(keyName):
        if elements[keyName] is not None:
            column = column + METRO_API.JapaneseRailWay(elements[keyName])
    content = content + html_convert.tagconvert(column)  
    #-------------------------------------------------------
    #発生時刻
    keyName='odpt:timeOfOrigin'
    column =''
    if elements.has_key(keyName):
        if elements[keyName] is not None:
            column = elements[keyName]
    content = content + html_convert.tagconvert(column)
    #-------------------------------------------------------
    #運行情報テキスト
    keyName='odpt:trainInformationText'
    column =''
    if elements.has_key(keyName):
        if elements[keyName] is not None:
            column = elements[keyName]
    content = content + html_convert.tagconvert(column)
    #-------------------------------------------------------
    content = content + u"</tr>" + "\n"

content = content + u"</table>"+ "\n"
content = content + u"</div>"+ "\n"
content = content + u"<div>東京メトロの事情により、予告なく本webシステムの提供をとりやめることがあります。</div>"

print "Content-type: text/html\n"
print (html_body % content).encode('utf-8')