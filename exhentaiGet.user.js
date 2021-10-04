// ==UserScript==
// @name         exhentaiGet
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        *://exhentai.org/*
// @include			*://exhentai.org/g/*
// @include			*://g.e-hentai.org/g/*
// @require      https://code.jquery.com/jquery-3.2.1.slim.min.js
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {

    var txt="<a href=\"https://btsow.one/search/"+ $("h1#gj").text() +"\">"+ $("h1#gj").text() +"</a>";
    $("h1#gj").text("")
    $("h1#gj").append(txt);

    GM_xmlhttpRequest({
        method: "GET",
        url: "http://192.168.0.110/manga.html",
        onload: function (result) {
            let _text = result.responseText;
            $("div.gl1t").each(function () {
                let _div = $(this).children("a").children("div")
                let _name = _div.text()

                _name = _name.replace(/\[.*?\]/g,'');
                _name = _name.replace(/\(.*?\)/g,'');
                _name = _name.replace(/\【.*?\】/g,'');

                _name = _name.split(" + ")[0]

                _name = _name.trim()

                let _index = _text.search(_name)

                if(_text.search(_name)!=-1)
                {
                    _div.attr("style", "color:#FF0")
                }
            });

        },
        onerror: function (e) {
            console.log(e);
        }
    });

    GM_xmlhttpRequest({
        method: "GET",
        url: "http://192.168.0.110/doujinshi.html",
        onload: function (result) {
            let _text = result.responseText;
            $("div.gl1t").each(function () {
                let _div = $(this).children("a").children("div")
                let _name = _div.text()

                _name = _name.replace(/\[.*?\]/g,'');
                _name = _name.replace(/\(.*?\)/g,'');
                _name = _name.replace(/\【.*?\】/g,'');

                _name = _name.split(" + ")[0]

                _name = _name.trim()

                let _index = _text.search(_name)

                if(_text.search(_name)!=-1)
                {
                    _div.attr("style", "color:#F00")
                }
            });

        },
        onerror: function (e) {
            console.log(e);
        }
    });



})();