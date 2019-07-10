import webbrowser
url = 'https://search.daum.net/search?q='
keyword = list(input().split(","))
print(keyword)
for i in keyword:
    webbrowser.open_new_tab(url+i)