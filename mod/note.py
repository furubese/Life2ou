serch = urllib.parse.quote(word)
    url = "https://www.amazon.co.jp/s?k={}".format(serch)
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        e = ["er", e]
        return e

    soup = BeautifulSoup(html, "html.parser")
    rs_price= soup.select('span.a-offscreen')
    rs_picture= soup.select('img.s-image')

    if not rs_picture:
        e = ["er", "検索に一致する商品はありませんでした"]
        return e

    if len(rs_picture) > vol:
        vol = 1
    elif len(rs_picture) < vol:
        vol = len(rs_picture)
    
