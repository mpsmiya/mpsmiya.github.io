#! /usr/local/bin/python
# coding: utf-8

import METRO_API
import html_convert

#---------------------------------------------------
#googlemap用のマーカーデータを作成します。
#---------------------------------------------------
def createmapmarker(data):


    content = ""
    content = content + '<script type="text/javascript" charset="utf-8" src="http://js.api.olp.yahooapis.jp/OpenLocalPlatform/V1/jsapi?appid=wfDrojSxg647FUQMeJxwmtc8saR47FHDRCVLqlgiCwENjWAF28V15HNuRn.ExbYfJpERo7s-"></script>'
    content = content + '<script type="text/javascript">'
    content = content + 'window.onload = function(){'
    content = content + 'var ymap = new Y.Map("map",'
    content = content + '{'

    content = content + ' configure : {'
    content = content + 'doubleClickZoom : true,'
    content = content + 'scrollWheelZoom : true,'#スクロールホイール有効
    content = content + 'continuousZoom : true'
    content = content + '}'

    content = content + '}'
    content = content + ');'
    content = content + 'ymap.drawMap(new Y.LatLng(35.68525, 139.763285), 17, Y.LayerSetId.NORMAL);'


    for elements in sorted(data, key=lambda x:x['odpt:stationCode'], reverse=False):
        name_Title = ''
        gio_long = ''
        gio_lat = ''
        railway = ''
        color=""
        #-----------------------------------
        #駅名
        column = ''
        key = 'dc:title'
        if key in elements:
            if elements[key] is not None:
                name_Title = elements[key]
        #-----------------------------------
        #経度
        #-----------------------------------
        column = ''
        key = 'geo:long'
        if key in elements:
            if elements[key] is not None:
                gio_long = elements[key]
        #-----------------------------------
        #緯度
        #-----------------------------------
        column = ''
        key = 'geo:lat'
        if key in elements:
            if elements[key] is not None:
                gio_lat = elements[key]
        #-----------------------------------
        #路線名
        column = ''
        key = 'odpt:railway'
        if key in elements:
            if elements[key] is not None:
                railway = elements[key]
                color = METRO_API.COLOR(railway).replace("#","")
        #-----------------------------------
        #全部そろっていればマーカーリストに追加
        #-----------------------------------
        if '' != name_Title:
            if ''!= gio_long:
                if ''!= gio_lat:
##                    #ラベルを張る
##                    content = content + 'var label = new Y.Label('
##                    content = content + 'new Y.LatLng('
##                    content = content + str(gio_lat)
##                    content = content + ','
##                    content = content + str(gio_long)
##                    content = content + ')'
##                    content = content + ','
##                    content = content + '"' + name_Title + '"'
##                    content = content + ');'
##                    content = content + 'ymap.addFeature(label);'
##                    content = content + '\n'
##                    #マーカー
##                    content = content + 'var marker = new Y.Marker('
##                    content = content + 'new Y.LatLng('
##                    content = content + str(gio_lat)
##                    content = content + ','
##                    content = content + str(gio_long)
##                    content = content + ')'
##                    content = content + ','
##                    content = content +  '{title: "' + name_Title + '"}'
##                    content = content + ');'
##                    content = content + 'ymap.addFeature(marker);'
##                    content = content + '\n'
                    #円を描く
                    content = content + 'var strokeStyle = new Y.Style("'
                    content = content + color + '", 15, 0.7);'
                    content = content + 'var fillStyle   = new Y.Style("'
                    content = content + color + '", null, 0.2);'
                    content = content + 'var circle = new Y.Circle(new Y.LatLng('
                    content = content + str(gio_lat)
                    content = content + ','
                    content = content + str(gio_long)
                    content = content + '), new Y.Size(0.1, 0.1), {'
                    content = content +     'unit:"km",'
                    content = content +     'strokeStyle: strokeStyle,'
                    content = content +     'fillStyle:fillStyle'
                    content = content + '});'
                    content = content + 'ymap.addFeature(circle);'
                    content = content + '\n'
        #-----------------------------------

    #content = content + createmapmarkerExit()

    content = content + '}'
    content = content + '</script>'
    content = content +'\n'

    return content

#---------------------------------------------------
#googlemap用のマーカーデータを作成します。
#---------------------------------------------------
def createmapmarkerExit():
    import serialize

    data=serialize.StationExitDeSerialize()
    #マーカーリストを作成
    content = ""
    for elements in sorted(data, key=lambda x:x['@id'], reverse=False):
        name_Title = ''
        gio_long = ''
        gio_lat = ''
        #-----------------------------------
        #駅名
        column = ''
        key = 'dc:title'
        if key in elements:
            if elements[key] is not None:
                name_Title = elements[key]
        #-----------------------------------
        #経度
        #-----------------------------------
        column = ''
        key = 'geo:long'
        if key in elements:
            if elements[key] is not None:
                gio_long = elements[key]
        #-----------------------------------
        #緯度
        #-----------------------------------
        column = ''
        key = 'geo:lat'
        if key in elements:
            if elements[key] is not None:
                gio_lat = elements[key]
        #-----------------------------------
        #全部そろっていればマーカーリストに追加
        #-----------------------------------
        if '' != name_Title:
            if ''!= gio_long:
                if ''!= gio_lat:
                    content = content + 'var marker = new Y.Marker('
                    content = content + 'new Y.LatLng('
                    content = content + str(gio_lat)
                    content = content + ','
                    content = content + str(gio_long)
                    content = content + ')'
                    content = content + ','
                    content = content +  '{title: "' + name_Title + '"}'
                    content = content + ');'
                    content = content + 'ymap.addFeature(marker);'
                    content = content + '\n'
        #-----------------------------------

    return content
#---------------------------------------------------
#HTMLのメインを作成
#---------------------------------------------------
def htmlmain(title,data):
    html =u"""
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>駅を地図に</title>
 <style>
        ul {
            text-align: center;
        }
        .pop_btn > li {
          display: inline-block;
          height: 50px;
          margin: 0;
          position: relative;
          width: 110px;
        }
        .pop_btn > li a {
          background-color: #0B9;
          border: 5px solid #0B9;
          border-radius: 500px;
          color: #FFF;
          display: block;
          font-family: "Arial Black";
          font-size: 17px;
          height: 40px;
          left: 15px;
          line-height: 40px;
          position: absolute;
          text-align: center;
          text-decoration: none;
          top: 0px;
          -webkit-transition: all ease 0.2s;
          -moz-transition: all ease 0.2s;
          -o-transition: all ease 0.2s;
          -ms-transition: all ease 0.2s;
          transition: all ease 0.2s;
          width: 100px;
        }
        .pop_btn > li a:hover {
          background-color: #FFF;
          color: #0B9;
          height: 40px;
          left: 15px;
          line-height: 40px;
          top: 0;
          width: 100px;
        }

        /* 東西線 */
        .pop_btn > li.TOZAI a:hover {
          color: #00a7db;
          background-color: #FFF;
        }
        .pop_btn > li.TOZAI a {
          background-color: #00a7db;
          border: 5px solid #00a7db;
        }
        /* 丸ノ内線 */
        .pop_btn > li.MARUNOUCHI a:hover {
          color: #e60012;
          background-color: #FFF;
        }
        .pop_btn > li.MARUNOUCHI a {
          background-color: #e60012;
          border: 5px solid #e60012;
        }
        /* 南北線 */
        .pop_btn > li.NAMBOKU a:hover {
          color: #00ada9;
          background-color: #FFF;
        }
        .pop_btn > li.NAMBOKU a {
          background-color: #00ada9;
          border: 5px solid #00ada9;
        }
        /* 日比谷 */
        .pop_btn > li.HIBIYA a:hover {
          color: #9caeb7;
          background-color: #FFF;
        }
        .pop_btn > li.HIBIYA a {
          background-color: #9caeb7;
          border: 5px solid #9caeb7;
        }
        /* 副都心線 */
        .pop_btn > li.FUKUTOSHIN a:hover {
          color: #bb641d;
          background-color: #FFF;
        }
        .pop_btn > li.FUKUTOSHIN a {
          background-color: #bb641d;
          border: 5px solid #bb641d;
        }
        /* 半蔵門線 */
        .pop_btn > li.HANZOUMON a:hover {
          color: #9b7cb6;
          background-color: #FFF;
        }
        .pop_btn > li.HANZOUMON a {
          background-color: #9b7cb6;
          border: 5px solid #9b7cb6;
        }
        /* 銀座線 */
        .pop_btn > li.GINZA a:hover {
          color: #f39700;
          background-color: #FFF;
        }
        .pop_btn > li.GINZA a {
          background-color: #f39700;
          border: 5px solid #f39700;
        }
        /* 有楽町線 */
        .pop_btn > li.YURAKUCHO a:hover {
          color: #d7c447;
          background-color: #FFF;
        }
        .pop_btn > li.YURAKUCHO a {
          background-color: #d7c447;
          border: 5px solid #d7c447;
        }
        /* 千代田線 */
        .pop_btn > li.CHIYODA a:hover {
          color: #009944;
          background-color: #FFF;
        }
        .pop_btn > li.CHIYODA a {
          background-color: #009944;
          border: 5px solid #009944;
        }
    </style>

    </head>

    <body>
        <div id="map" style="width:100%%; height:600px"></div>
            %s
　　　　　　<div>駅から半径100mを路線色の円にしています</div>
            <ul class="pop_btn">
                    <li class="TOZAI"><a href="javascript:void(0)">東西線</a></li><br>
                    <li class="MARUNOUCHI"><a href="javascript:void(0)">丸ノ内線</a></li><br>
                    <li class="NAMBOKU"><a href="javascript:void(0)">南北線</a></li><br>
                    <li class="HIBIYA"><a href="javascript:void(0)">日比谷線</a></li><br>
                    <li class="FUKUTOSHIN"><a href="javascript:void(0)">副都心線</a></li><br>
                    <li class="HANZOUMON"><a href="javascript:void(0)">半蔵門線</a></li><br>
                    <li class="GINZA"><a href="javascript:void(0)">銀座線</a></li><br>
                    <li class="YURAKUCHO"><a href="javascript:void(0)">有楽町線</a></li><br>
                    <li class="CHIYODA"><a href="javascript:void(0)">千代田線</a></li><br>
             </ul>
        <!-- Begin Yahoo! JAPAN Web Services Attribution Snippet -->
        <a href="http://developer.yahoo.co.jp/about">
        <img src="http://i.yimg.jp/images/yjdn/yjdn_attbtn1_88_35.gif" width="88" height="35" title="Webサービス by Yahoo! JAPAN" alt="Web Services by Yahoo! JAPAN" border="0" style="margin:15px 15px 15px 15px"></a>
        <!-- End Yahoo! JAPAN Web Services Attribution Snippet -->
　　　　東京メトロの事情により、予告なく本webシステムの提供をとりやめることがあります。
    </body>
</html>
"""

    return (html %(createmapmarker(data)))

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
    content = content + htmlmain('',root)

    print "Content-Type: text/html\n"
    print content.encode('utf-8')

if __name__ == '__main__':
    main()