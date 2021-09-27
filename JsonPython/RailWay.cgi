#! /usr/local/bin/python
# coding: utf-8

import METRO_API
import html_convert

#---------------------------------------------------
#駅名のコンボボックスを作成する
#---------------------------------------------------
def railwaystationcombobox(title,data):

    #路線名のみ抜き出し
    content = ""
    #-------------------------------
    #路線ごとの駅名を抽出します
    #-------------------------------
    list_TOZAI       = []
    list_MARUNOUCHI  = []
    list_NAMBOKU     = []
    list_HIBIYA      = []
    list_FUKUTOSHIN  = []
    list_HANZOUMON   = []
    list_GINZA       = []
    list_YURAKUCHO   = []
    list_CHIYODA     = []
    #-------------------------------
    #ソート処理
    #-------------------------------
    for elements in data:
        key = 'odpt:railway'
        if key in elements:
            if elements[key] is not None:
                #路線名ごとに分ける
                railway = elements[key]
                if railway ==   METRO_API.RAILWAYNAME.TOZAI:
                    list_TOZAI.append(elements)
                elif railway == METRO_API.RAILWAYNAME.MARUNOUCHI:
                    list_MARUNOUCHI.append(elements)
                elif railway == METRO_API.RAILWAYNAME.MARUNOUCHIBRANCH:
                    list_MARUNOUCHI.append(elements)
                elif railway == METRO_API.RAILWAYNAME.NAMBOKU:
                    list_NAMBOKU.append(elements)
                elif railway == METRO_API.RAILWAYNAME.HIBIYA:
                    list_HIBIYA.append(elements)
                elif railway == METRO_API.RAILWAYNAME.FUKUTOSHIN:
                    list_FUKUTOSHIN.append(elements)
                elif railway == METRO_API.RAILWAYNAME.HANZOUMON:
                    list_HANZOUMON.append(elements)
                elif railway == METRO_API.RAILWAYNAME.GINZA:
                    list_GINZA.append(elements)
                elif railway == METRO_API.RAILWAYNAME.YURAKUCHO:
                    list_YURAKUCHO.append(elements)
                elif railway == METRO_API.RAILWAYNAME.CHIYODA:
                    list_CHIYODA.append(elements)
    #-------------------------------
    #駅名コンボボックスの作成
    #-------------------------------
    r_TOZAI         = ''
    r_MARUNOUCHI    = ''
    r_NAMBOKU       = ''
    r_HIBIYA        = ''
    r_FUKUTOSHIN    = ''
    r_HANZOUMON     = ''
    r_GINZA         = ''
    r_YURAKUCHO     = ''
    r_CHIYODA       = ''
    buffstr         = ''

    html =u"""
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>路線と駅と乗換線</title>
        <link rel="stylesheet" type="text/css" href="css/menu.css">
    </head>

    <body>
        %s
    <div>東京メトロの事情により、予告なく本webシステムの提供をとりやめることがあります。</div>
    </body>
</html>
"""

    st=u"""
    <div class="box">
    <hr>
    <h1>路線と駅と乗換線<br>
    (各路線をクリックすると駅の情報が表示されます)</h1>
    <hr>
    <ul class="menu">
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    %s
    </ul>
"""
    #-------------------------------
    #ソート処理
    #-------------------------------
    for i in range(10):
        #ターゲットとなる路線を決める
        listRailWay = list_TOZAI
        if i == 0:
            listRailWay = list_TOZAI
        elif i == 1:
            listRailWay = list_MARUNOUCHI
        elif i == 2:
            listRailWay = list_NAMBOKU
        elif i == 3:
            listRailWay = list_HIBIYA
        elif i == 4:
            listRailWay = list_FUKUTOSHIN
        elif i == 5:
            listRailWay = list_HANZOUMON
        elif i == 6:
            listRailWay = list_GINZA
        elif i == 7:
            listRailWay = list_YURAKUCHO
        elif i == 8:
            listRailWay = list_CHIYODA

        #---------------------------------------
        #路線ごとの駅名を表示する
        #---------------------------------------
        #路線名
        buffstr = u''
        buffstr = buffstr + '<li>' + '\r\n'
        buffstr = buffstr + '<label for="m%d"></label>' %i + '\r\n'
        buffstr = buffstr + '<input type="checkbox" id="m%d">'%i + METRO_API.JapaneseRailWay( listRailWay[0]['odpt:railway']) + '\r\n'
        buffstr = buffstr + '<ul class="submenu">' + '\r\n'

        #各駅名
        for elements in sorted(listRailWay, key=lambda x:x['odpt:stationCode'], reverse=False):
            key = 'odpt:railway'
            if key in elements:
                href = ''
                href = href + '<a href="Station.cgi?station=' + METRO_API.tagclear(elements['owl:sameAs']) + '">'
                href = href + elements['dc:title']
                href = href + '</a>'
                buffstr = buffstr + '<li><p>[%s]  %s</p></li>' %(elements['odpt:stationCode'],href) + '\r\n'
                key='odpt:connectingRailway'
                connect =''
                connectExist = False;
                if key in elements:
                   for item in elements['odpt:connectingRailway']:
                        connectExist = True;
                        connect = connect + '<li><p>&nbsp;&nbsp;&nbsp;----%s</p></li>' %(METRO_API.JapaneseRailWay(item)) + '\r\n';
                if True == connectExist:
                    buffstr = buffstr + connect;

        buffstr = buffstr + '</ul>' + '\r\n'
        buffstr = buffstr + '</li>' + '\r\n'

        #路線にコンボボックスを戻す
        listRailWay = list_TOZAI
        if i == 0:
            r_TOZAI         = buffstr
        elif i == 1:
            r_MARUNOUCHI    = buffstr
        elif i == 2:
            r_NAMBOKU       = buffstr
        elif i == 3:
            r_HIBIYA        = buffstr
        elif i == 4:
            r_FUKUTOSHIN    = buffstr
        elif i == 5:
            r_HANZOUMON     = buffstr
        elif i == 6:
            r_GINZA         = buffstr
        elif i == 7:
            r_YURAKUCHO     = buffstr
        elif i == 8:
            r_CHIYODA       = buffstr
    st=st %(r_TOZAI,r_MARUNOUCHI,r_NAMBOKU,r_HIBIYA,r_FUKUTOSHIN,r_HANZOUMON,r_GINZA,r_YURAKUCHO,r_CHIYODA)

    return (html %(st))

#---------------------------------------------------
#駅名のコンボボックスを作成する
#---------------------------------------------------
def allstationcombobox(title,data):
    #-------------------------------
    #全駅駅名のコンボボックスを作成します
    #-------------------------------
    return stationcombobox(title,data)

#---------------------------------------------------
#駅名のコンボボックスを作成する
#---------------------------------------------------
def getstation():
    #URLを指定する
    url=''
    url = url + 'https://api.tokyometroapp.jp/api/v2/'
    url = url + 'datapoints?rdf:type=odpt:Station'
    url = url + '&'
    url = url + 'acl:'+METRO_API.Metro_api_Const.ACL

    #データ取得
    return METRO_API.getMetroAPI(url)

def main():

    #データ取得
    root = getstation()
    content = ""
    content = content + railwaystationcombobox('',root)
    print "Content-Type: text/html\n"
    print content.encode('utf-8')

if __name__ == '__main__':
    main()