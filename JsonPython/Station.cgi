#! /usr/local/bin/python
# coding: utf-8

import cgi
import METRO_API
import html_convert

#-------------------------------------------------------------------------------
#駅施設情報をHTML化する
#-------------------------------------------------------------------------------
def stationfacilityconvert(stationName):
    content = ''

    #-------------------------------------------------------
    #データファイルの読み出し
    #-------------------------------------------------------
    url=''
    url = url + 'https://api.tokyometroapp.jp/api/v2/'
    url = url + 'datapoints/?rdf:type=odpt:StationFacility'
    url = url + '&owl:sameAs=odpt.StationFacility:'
    url = url + stationName
    url = url + '&'
    url = url + 'acl:'+METRO_API.Metro_api_Const.ACL

    root = METRO_API.getMetroAPI(url)
    #-------------------------------------------------------
    #駅名のデータを検索
    #-------------------------------------------------------
    for elements in root:
        #-----------------------------------
        #該当駅か確認
        #-----------------------------------
        hit = False
        key = "owl:sameAs"
        if key in elements:
            item = elements[key]
            if item is not None:
                #対象駅であれば
                if METRO_API.tagclear(stationName) == METRO_API.tagclear(item):
                    hit=True

        #-----------------------------------
        #プラットフォームに車両が停車している時の、車両毎の最寄りの施設・出口等の情報を記述
        #-----------------------------------
        if 'odpt:platformInformation' in elements:

            head = ''
            head = head + u"<table>"
            #テーブルデータ列
            head = head + u"<tr>"
            head = head + html_convert.tagconvert(u"路線名称")
            head = head + html_convert.tagconvert(u"方面")
            head = head + html_convert.tagconvert(u"車両番号")
            head = head + html_convert.tagconvert(u"乗換路線")
            head = head + html_convert.tagconvert(u"駅施設")
            head = head + html_convert.tagconvert(u"改札の外には")
            head = head + u"</tr>"+ "\n"

            info = ''

            for item in elements['odpt:platformInformation']:
                key = "owl:sameAs"
                column = ''
                if item is not None:
                     #対象駅であれば
                    if hit == True:
                        info = info + u"<tr>"
                        #-------------------------------------------------------
                        #路線名
                        key = "odpt:railway"
                        column =''
                        if key in item:
                            if item[key] is not None:
                                column = METRO_API.JapaneseRailWay(item[key])
                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
                        #プラットフォームに停車する列車の方面
                        key = "odpt:railDirection"
                        column =''
                        if key in item:
                            if item[key] is not None:
                                column = METRO_API.JapaneseRailDirection(item[key])
                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
##                        #車両編成数
##                        key = "odpt:carComposition"
##                        column =''
##                        if key in item:
##                            if item[key] is not None:
##                                column = str(item[key])
##                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
                        #車両の号車番号
                        key = "odpt:carNumber"
                        column =''
                        if key in item:
                            if item[key] is not None:
                                column = str(item[key]) + u'号車'
                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
                        #最寄りの乗り換え可能な路線と所要時間
                        key = "odpt:transferInformation"
                        column =''
                        if key in item:
                            if item[key] is not None:
                                for detail in item[key]:
                                    if detail is not None:
                                        dKey = ''
                                        #---------------------------------------
                                        #乗り換え可能路線
                                        dKey ="odpt:railway"
                                        if dKey in detail:
                                            column = column + METRO_API.JapaneseRailWay(detail[dKey]) + '<br>'
                                        #---------------------------------------
                                        #乗り換え可能路線の方面
                                        dKey ="odpt:railDirection"
                                        if dKey in detail:
                                            column = column + METRO_API.JapaneseRailDirection(detail[dKey])+ '<br>'
                                        #---------------------------------------
                                        #所要時間（分）
                                        dKey ="odpt:necessaryTime"
                                        if dKey in detail:
                                            column = column + u'移動時間' +str(detail[dKey]) + u'分<br>'
                                        #---------------------------------------
                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
                        #最寄りのバリアフリー施設
                        key = "odpt:barrierfreeFacility"
                        column =''
                        if key in item:
                            if item[key] is not None:
                                for detail in item[key]:
                                    if detail is not None:
                                        #種別
                                        if 'Elevator' in detail:
                                            column = column +"""<img src="img/Elevator.gif" width="40" height="40" alt="rogo">"""
                                        if 'Stairlift' in detail:
                                            column = column +"""<img src="img/Stairlift.gif" width="40" height="40" alt="rogo">"""
                                        if 'Escalator' in detail:
                                            column = column +"""<img src="img/Escalator.gif" width="40" height="40" alt="rogo">"""
                                        if 'Toilet' in detail:
                                            column = column +"""<img src="img/Toilet.gif" width="40" height="40" alt="rogo">"""
                                        if 'AccessibleRoute' in detail:
                                            column = column +"""<img src="img/Toilet.gif" width="40" height="40" alt="rogo">"""
                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
                        #改札外の最寄り施設
                        key = "odpt:surroundingArea"
                        column =''
                        if key in item:
                            if item[key] is not None:
                                for detail in item[key]:
                                    if detail is not None:
                                        column = column + detail + '<br>'
                        info = info + html_convert.tagconvert(column)
                        #-------------------------------------------------------
                        info = info + u"</tr>"
            head = head + info +u"</table>"
            if info != "":
                content = content + head
    #-------------------------------------------------------
    return content
#-------------------------------------------------------------------------------
#メイン処理
#-------------------------------------------------------------------------------
def main():
    #駅名を確認する
    form = cgi.FieldStorage()
    station = form.getvalue('station', 'odpt.Station:TokyoMetro.Tozai.Otemachi')
    #URLを指定する
    url=''
    url = url + 'https://api.tokyometroapp.jp/api/v2/'
    url = url + 'datapoints/?rdf:type=odpt:StationTimetable'
    url = url + '&odpt:station='
    url = url + station
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
    	border: solid 1px;
    	padding: 0.5em;
    }
    </style>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <title>%s</title>
    </head>
    <body>
    %s
    </body>
    </html>
    """

    content = ""
    content = METRO_API.tagclear(station)
    content = content + stationfacilityconvert(METRO_API.getStationName(station))

    print "Content-Type: text/html\n"
    print (html_body %(METRO_API.tagclear(station), content)).encode('utf-8')

if __name__ == '__main__':
    main()