#! /usr/local/bin/python
# coding: utf-8

def encodeHtml(title, header, context, footer):
    html_body = u'''

<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="UTF-8" />

        <title>
<!-- [S]タイトル -->
%s
<!-- [S]タイトル -->
        </title>
        <!-- jQuery Mobileの動作に必要なスタイル・ライブラリのインポート-->
        <!-- jQuery Mobileの標準のスタイルシート-->
        <!-- Contents Derivery NetWork-->
        <link rel="stylesheet"
            href="http://code.jquery.com/mobile/1.4.0/jquery.mobile-1.4.0.min.css" />
        <!-- jQuery 本体-->
        <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
        <!-- jQuery Mobile本体-->
        <script src="http://code.jquery.com/mobile/1.4.0/jquery.mobile-1.4.0.min.js">
        </script>
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scaable=yes,maximum-scale=1.5,minimum-scale=1.0">

　　　　<!-- Google -->
　　　　<script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

            ga('create', 'UA-59914580-1', 'auto');
            ga('send', 'pageview');
        </script>

    </head>

    <body>
        <!-- ページ領域-->
        <div data-role="page">
            <div data-role="header" data-position="fixed">
                <h1>
<!-- [S]ヘッダ部分 -->
%s
<!-- [E]ヘッダ部分 -->
                </h1>
                <a href="index.html" data-icon="home"a>Home</a>
            </div>
            <div data-role="content">
<!--[S] コンテンツ部分 -->
%s
<!--[E] コンテンツ部分 -->
            </div>

            <div data-role="footer" data-position="fixed">
                <h2>
<!--[S] フッターは日付時刻 -->
%s JM
<!--[E] フッターは日付時刻 -->
                </h2>
            </div>
        </div>
  </body>
</html>
'''

    return (html_body % (title, header, context, footer)).encode('utf-8')