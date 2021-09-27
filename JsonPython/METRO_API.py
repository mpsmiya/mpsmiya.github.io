#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      GOLF
#
# Created:     17/09/2014
# Copyright:   (c) GOLF 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json, urllib2
import time
#-------------------------------------------------------------------------------
#メトロAPI必須項目
#-------------------------------------------------------------------------------
class Metro_api_Const:
    #APIアクセス用のトークン
    ACL='consumerKey=31a056483bad1c37fb9bd58d6784c97008797dddd34c678415d903601402a5f7'
    ##2014-09-19前でのトークン
    ##ACL='consumerKey=4675e3fbd46bc9801d7e63c8c96d758715909ea5fb2c3032547fdce0929c1bfc'
#-------------------------------------------------------------------------------
#メトロAPIデータ取得
#url:       取得するURL
#-------------------------------------------------------------------------------
def getMetroAPI(url):
    #データ取得
    r = urllib2.urlopen(url)
    root = json.loads(r.read())
    r.close()
    time.sleep(0.2)
    return root
#-------------------------------------------------------------------------------
#メトロ路線シンボルカラー
#-------------------------------------------------------------------------------
class RAILWAYCOLOR:
    TOZAI       = "#00a7db"
    MARUNOUCHI  = "#e60012"
    NAMBOKU     = "#00ada9"
    HIBIYA      = "#9caeb7"
    FUKUTOSHIN  = "#bb641d"
    HANZOUMON   = "#9b7cb6"
    GINZA       = "#f39700"
    YURAKUCHO   = "#d7c447"
    CHIYODA     = "#009944"
#-------------------------------------------------------------------------------
#メトロ路線名称
#-------------------------------------------------------------------------------
class RAILWAYNAME:
    TOZAI               = "odpt.Railway:TokyoMetro.Tozai"
    MARUNOUCHI          = "odpt.Railway:TokyoMetro.Marunouchi"
    MARUNOUCHIBRANCH    = "odpt.Railway:TokyoMetro.MarunouchiBranch"
    NAMBOKU             = "odpt.Railway:TokyoMetro.Namboku"
    HIBIYA              = "odpt.Railway:TokyoMetro.Hibiya"
    FUKUTOSHIN          = "odpt.Railway:TokyoMetro.Fukutoshin"
    HANZOUMON           = "odpt.Railway:TokyoMetro.Hanzomon"
    GINZA               = "odpt.Railway:TokyoMetro.Ginza"
    YURAKUCHO           = "odpt.Railway:TokyoMetro.Yurakucho"
    CHIYODA             = "odpt.Railway:TokyoMetro.Chiyoda"
#-------------------------------------------------------------------------------
#タグをクリア
#-------------------------------------------------------------------------------
def tagclear(param):

    #タグをクリア
    org = param
    org = org.replace('odpt.Railway:', '')
    org = org.replace('odpt.Station:', '')
    org = org.replace('odpt:connectingRailway:', '')
    org = org.replace('odpt.StationFacility:', '')
    return org

#-------------------------------------------------------------------------------
#駅名を取得する
#-------------------------------------------------------------------------------
def getStationName(param):

    #路線名
    railwayName = param
    railwayName =railwayName.replace('odpt.Station:','')

    if "Tozai." in railwayName:
        railwayName =railwayName.replace('Tozai.','')
    elif "Marunouchi." in railwayName:
        railwayName =railwayName.replace('Marunouchi.','')
    elif "MarunouchiBranch." in railwayName:
        railwayName =railwayName.replace('MarunouchiBranch.','')
    elif "Namboku." in railwayName:
        railwayName =railwayName.replace('Namboku.','')
    elif "Hibiya." in railwayName:
        railwayName =railwayName.replace('Hibiya.','')
    elif "Fukutoshin." in railwayName:
        railwayName =railwayName.replace('Fukutoshin.','')
    elif "Hanzomon." in railwayName:
        railwayName =railwayName.replace('Hanzomon.','')
    elif "Ginza." in railwayName:
        railwayName =railwayName.replace('Ginza.','')
    elif "Yurakucho." in railwayName:
        railwayName =railwayName.replace('Yurakucho.','')
    elif "Chiyoda." in railwayName:
        railwayName =railwayName.replace('Chiyoda.','')
    return railwayName

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
def JapaneseRailWay(param):

    #タグをクリア
    org = tagclear(param)

    #路線名
    railwayName = org
    if org =="TokyoMetro.Tozai":
        railwayName =u"東西線"
    elif org =="TokyoMetro.Marunouchi":
        railwayName =u"丸ノ内線"
    elif org =="TokyoMetro.MarunouchiBranch":
        railwayName =u"丸ノ内（分岐線）線"
    elif org =="TokyoMetro.Namboku":
        railwayName =u"南北線"
    elif org =="TokyoMetro.Hibiya":
        railwayName =u"日比谷線"
    elif org =="TokyoMetro.Fukutoshin":
        railwayName =u"副都心線"
    elif org =="TokyoMetro.Hanzomon":
        railwayName =u"半蔵門線"
    elif org =="TokyoMetro.Ginza":
        railwayName =u"銀座線"
    elif org =="TokyoMetro.Yurakucho":
        railwayName =u"有楽町線"
    elif org =="TokyoMetro.Chiyoda":
        railwayName =u"千代田線"
    elif org =="TokyoMetro.Chiyoda":
        railwayName =u"千代田線"

    #東京メトロ以外の路線
    elif org =="JR-East":
        railwayName =u"JR線"
    elif org =="JR-East.Chuo":
        railwayName =u"JR線.中央線"
    elif org =="JR-East.ChuoKaisoku":
        railwayName =u"JR線.中央線快速"
    elif org =="JR-East.ChuoSobu":
        railwayName =u"JR線.中央・総武線各駅停車"
    elif org =="JR-East.Joban":
        railwayName =u"JR線.常磐線"
    elif org =="JR-East.KeihinTohoku":
        railwayName =u"JR線.京浜東北線"
    elif org =="JR-East.Keiyo":
        railwayName =u"JR線.京葉線"
    elif org =="JR-East.Musashino":
        railwayName =u"JR線.武蔵野線"
    elif org =="JR-East.NaritaExpress":
        railwayName =u"JR線.成田エクスプレス"
    elif org =="JR-East.Saikyo":
        railwayName =u"JR線.埼京線"
    elif org =="JR-East.ShonanShinjuku":
        railwayName =u"JR線.湘南新宿ライン"
    elif org =="JR-East.Sobu":
        railwayName =u"JR線.総武線"
    elif org =="JR-East.Takasaki":
        railwayName =u"JR線.高崎線"
    elif org =="JR-East.Tokaido":
        railwayName =u"JR線.東海道線"
    elif org =="JR-East.Utsunomiya":
        railwayName =u"JR線.宇都宮線"
    elif org =="JR-East.Yamanote":
        railwayName =u"JR線.山手線"
    elif org =="JR-East.Yokosuka":
        railwayName =u"JR線.横須賀線"

    elif org =="Keio.Inokashira":
        railwayName =u"京王線.井の頭線"
    elif org =="Keio.Keio":
        railwayName =u"京王線.京王線"
    elif org =="Keio.New":
        railwayName =u"京王線.京王新線"

    elif org =="Keisei.KeiseiMain":
        railwayName =u"京成線.京成本線"
    elif org =="Keisei.KeiseiOshiage":
        railwayName =u"京成線.押上線"

    elif org =="MIR.TX":
        railwayName =u"つくばエクスプレス線"

    elif org =="Odakyu.Odawara":
        railwayName =u"小田急線.小田原線"

    elif org =="SaitamaRailway.SaitamaRailway":
        railwayName =u"埼玉高速鉄道線"

    elif org =="Seibu.Ikebukuro":
        railwayName =u"西武線.池袋線"
    elif org =="Seibu.SeibuYurakucho":
        railwayName =u"西武線.西武有楽町線"
    elif org =="Seibu.Shinjuku":
        railwayName =u"西武線.新宿線"

    elif org =="TWR.Rinkai":
        railwayName =u"りんかい線"

    elif org =="Tobu.Isesaki":
        railwayName =u"東武線.伊勢崎線"
    elif org =="Tobu.Tojo":
        railwayName =u"東武線.東上線"

    elif org =="Toei.Asakusa":
        railwayName =u"都営線.浅草線"
    elif org =="Toei.Mita":
        railwayName =u"都営線.三田線"
    elif org =="Toei.NipporiToneri":
        railwayName =u"都営線.日暮里・舎人ライナー"
    elif org =="Toei.Oedo":
        railwayName =u"都営線.大江戸線"
    elif org =="Toei.Shinjuku":
        railwayName =u"都営線.新宿線"
    elif org =="Toei.TodenArakawa":
        railwayName =u"都営線.都電荒川線"

    elif org =="Tokyu.DenEnToshi":
        railwayName =u"東急線.田園都市線"
    elif org =="Tokyu.Meguro":
        railwayName =u"東急線.目黒線"
    elif org =="Tokyu.Toyoko":
        railwayName =u"東急線.東横線"

    elif org =="ToyoRapidRailway.ToyoRapidRailway":
        railwayName =u"東葉高速線"

    elif org =="Yurikamome.Yurikamome":
        railwayName =u"ゆりかもめ"

    #色を付加
    color=COLOR(org)

    if color != '':
        railwayName ='<font color="'+ color +'">' + railwayName + '</font>'

    return railwayName

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
def COLOR(param):

    #タグをクリア
    org = tagclear(param)
    #色を付加
    color=''
    if org =="TokyoMetro.Tozai":
        color=RAILWAYCOLOR.TOZAI
    elif org =="TokyoMetro.Marunouchi":
        color=RAILWAYCOLOR.MARUNOUCHI
    elif org =="TokyoMetro.MarunouchiBranch":
        color=RAILWAYCOLOR.MARUNOUCHI
    elif org =="TokyoMetro.Namboku":
        color=RAILWAYCOLOR.NAMBOKU
    elif org =="TokyoMetro.Hibiya":
        color=RAILWAYCOLOR.HIBIYA
    elif org =="TokyoMetro.Fukutoshin":
        color=RAILWAYCOLOR.FUKUTOSHIN
    elif org =="TokyoMetro.Hanzomon":
        color=RAILWAYCOLOR.HANZOUMON
    elif org =="TokyoMetro.Ginza":
        color=RAILWAYCOLOR.GINZA
    elif org =="TokyoMetro.Yurakucho":
        color=RAILWAYCOLOR.YURAKUCHO
    elif org =="TokyoMetro.Chiyoda":
        color=RAILWAYCOLOR.CHIYODA

    return color

def JapaneseRailDirection(param):
    jpn_RailDirection = ''
    raildirectonNo = 0

    #-----------------------------------------------
    #方面1
    #-----------------------------------------------
    if 'odpt.RailDirection:TokyoMetro.Asakusa' in param:
        jpn_RailDirection=u'浅草方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Ikebukuro' in param:
        jpn_RailDirection=u'池袋方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.NakanoSakaue' in param:
        jpn_RailDirection=u'中野坂上方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.KitaSenju' in param:
        jpn_RailDirection=u'北千住方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Nakano' in param:
        jpn_RailDirection=u'中野方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Ayase' in param:
        jpn_RailDirection=u'綾瀬方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.KitaAyase' in param:
        jpn_RailDirection=u'北綾瀬方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Wakoshi' in param:
        jpn_RailDirection=u'和光市方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Shibuya' in param:
        jpn_RailDirection=u'渋谷方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Meguro' in param:
        jpn_RailDirection=u'目黒方面'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Wakoshi' in param:
        jpn_RailDirection=u'和光市方面'
        raildirectonNo = 1

    #-----------------------------------------------
    #方面2
    #-----------------------------------------------
    if 'odpt.RailDirection:TokyoMetro.Shibuya' in param:
        jpn_RailDirection=u'渋谷方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Ogikubo' in param:
        jpn_RailDirection=u'荻窪方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Honancho' in param:
        jpn_RailDirection=u'方南町方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.NakaMeguro' in param:
        jpn_RailDirection=u'中目黒方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.NishiFunabashi' in param:
        jpn_RailDirection=u'西船橋方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.YoyogiUehara' in param:
        jpn_RailDirection=u'代々木上原方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Ayase' in param:
        jpn_RailDirection=u'綾瀬方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.ShinKiba' in param:
        jpn_RailDirection=u'新木場方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Oshiage' in param:
        jpn_RailDirection=u'押上方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.AkabaneIwabuchi' in param:
        jpn_RailDirection=u'赤羽岩淵方面'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Shibuya' in param:
        jpn_RailDirection=u'渋谷方面'
        raildirectonNo = 2

    #-----------------------------------------------
    #返却値
    #-----------------------------------------------
    if '' == jpn_RailDirection:
        jpn_RailDirection = param
    return jpn_RailDirection

def JapaneseRailWay_From_RailDirection(param):
    jpn_RailWay = ''
    #-----------------------------------------------
    #方面1
    #-----------------------------------------------
    if 'odpt.RailDirection:TokyoMetro.Asakusa' in param:
        jpn_RailDirection=u'銀座線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Ikebukuro' in param:
        jpn_RailDirection=u'丸の内線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.NakanoSakaue' in param:
        jpn_RailDirection=u'丸ノ内線(分岐線)'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.KitaSenju' in param:
        jpn_RailDirection=u'日比谷線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Nakano' in param:
        jpn_RailDirection=u'東西線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Ayase' in param:
        jpn_RailDirection=u'千代田線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.KitaAyase' in param:
        jpn_RailDirection=u'千代田線(支線)'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Wakoshi' in param:
        jpn_RailDirection=u'有楽町線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Shibuya' in param:
        jpn_RailDirection=u'半蔵門線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Meguro' in param:
        jpn_RailDirection=u'南北線'
        raildirectonNo = 1
    if 'odpt.RailDirection:TokyoMetro.Wakoshi' in param:
        jpn_RailDirection=u'副都心線'
        raildirectonNo = 1

    #-----------------------------------------------
    #方面2
    #-----------------------------------------------
    if 'odpt.RailDirection:TokyoMetro.Shibuya' in param:
        jpn_RailDirection=u'銀座線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Ogikubo' in param:
        jpn_RailDirection=u'丸の内線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Honancho' in param:
        jpn_RailDirection=u'丸ノ内線(分岐線)'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.NakaMeguro' in param:
        jpn_RailDirection=u'日比谷線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.NishiFunabashi' in param:
        jpn_RailDirection=u'東西線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.YoyogiUehara' in param:
        jpn_RailDirection=u'千代田線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Ayase' in param:
        jpn_RailDirection=u'千代田線(支線)'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.ShinKiba' in param:
        jpn_RailDirection=u'有楽町線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Oshiage' in param:
        jpn_RailDirection=u'半蔵門線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.AkabaneIwabuchi' in param:
        jpn_RailDirection=u'南北線'
        raildirectonNo = 2
    if 'odpt.RailDirection:TokyoMetro.Shibuya' in param:
        jpn_RailDirection=u'渋谷方面'
        raildirectonNo = 2

    #-----------------------------------------------
    #返却値
    #-----------------------------------------------
    if '' == jpn_RailDirection:
        jpn_RailDirection = param
    return jpn_RailDirection

def JapanesetTrainType(param):
    traintype = ''

    #-----------------------------------------------
    #列車種別
    #-----------------------------------------------
    if 'Local' in param:
        traintype = u'各停'
    if 'Express' in param:
        traintype = u'急行'
    if 'Rapid' in param:
        traintype = u'快速'
    if 'LimitedExpress' in param:
        traintype = u'特急'
    #-----------------------------------------------
    #返却値
    #-----------------------------------------------
    if '' == traintype:
        traintype = param
    return traintype