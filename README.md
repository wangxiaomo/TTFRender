## TTFRender Module ##

TTFRender Module 是中文 WebFont && WebFont Loader 的解决方案。WebFont 作为 css3 中比较好的技术被国外广为应用，配合 google webfont loader 方案能很好的实现页面字体动态加载，并且脱离了终端字体库的限制。

WebFont 纵然很好，但是目前没有较好的中文解决方案。一是 google 等其他 WebFont 厂商没有支持。二来是因为中文字库太大，影响 UE。

TTFRender 就是为了解决这一问题而出现的。我们只需要提供特定字体和需要支持的字列表，然后便可以生成符合应用的字符，有效的节省了带宽与时间，并提升了 UE。

#### How To Use ####

1.导出字体

    #-*- coding: utf-8 -*-
    
    from TTFRender import generate
    
    token_list = ["一","三","测","A","B","C","D","E"]
    ttf_file = "new_kai.ttf"
    
    generate(token_list, "kai", ttf_file)

这样就生成了符合应用的字体，之后便可以通过 WebFont && WebFont Loader 引入。

2.使用 font-face 引用。

    @font-face {
        font-family: "FontName",
        src: url("new_kai.ttf"),
    }

3.在 HTML 中使用。

    p { font-family: FontName; }

这样便可以在页面中使用你想要使用的字体了。不过这里有两个问题需要特别注意下：
    
  * 浏览器兼容性
  font-face 是 css3 重新引入的(css2引入。css2.1废弃).在 [CSS3 Support][CSS3 Support] 上可以看到 css3 font-face 对各浏览器的支持。虽然在上面的 url 中显示 IE9 以上才支持
  font-face。但是在 IE6,IE7,IE8 中也有自己的实现，也就是说我们也可以在旧版 IE 中使用 font-face。IE唯一存在的兼容性问题是字体文件需要使用 EOT 格式。FF,Chrome,Opera,Safari 既可以使用
  TTF，也可以使用 OTF 字体。需要注意的是 ios4.1 以前的设备需要使用 SVG 字体。

  * 尽管通过上面的代码对中文字体进行了很大程度的缩小。但是字体文件依然很大，对 UE 影响依然很严重。

#### Alternative Use ####

1.中文字体文件过大？
中文字体过大严重影响 UE。这时候我们可以使用 [WebFont Loader][WebFont Loader] 来控制在不同载入状态下的字体显示。

    <html>
      <head>
        <script type="text/javascript">
          WebFontConfig = {
          google: { families: [ 'Tangerine', 'Cantarell' ] }
        };
        (function() {
          var wf = document.createElement('script');
          wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
              '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
          wf.type = 'text/javascript';
          wf.async = 'true';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(wf, s);
        })();
        </script>
        <style type="text/css">
        .wf-loading p {
          font-family: serif
        }
        .wf-inactive p {
          font-family: serif
        }
        .wf-active p {
          font-family: 'Tangerine', serif
        }
        .wf-loading h1 {
          font-family: serif;
          font-weight: 400;
          font-size: 16px
        }
        .wf-inactive h1 {
          font-family: serif;
          font-weight: 400;
          font-size: 16px
        }
        .wf-active h1 {
          font-family: 'Cantarell', serif;
          font-weight: 400;
          font-size: 16px
        }
        </style>
      </head>
      <body>
      <h1>This is using Cantarell</h1>
      <p>This is using Tangerine!</p>
      </body>
    </html>

2.大字体使用 WebFont Loader 仍然很慢？
这时候我们可以把大字体分割成多个小字体文件。然后让WebFont Loader加载.

#### API ####

* TTFRender/__init__.py
导出模块功能。

* TTFRender/helper.py 
模块 Helper Functions.

    * _unicode
    返回 string 的 unicode 值。

    * get_ttf_file
    根据字体返回指定的字体文件。

    * get_token_list
    返回字列表

* TTFRender/parser.py
TTFRender Core Module.


[CSS3 Support]:  http://www.w3schools.com/cssref/css3_browsersupport.asp
[WebFont Loader]: https://developers.google.com/webfonts/docs/webfont_loader
