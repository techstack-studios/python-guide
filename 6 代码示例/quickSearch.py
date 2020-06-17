import webbrowser
import sys
search_from = sys.argv[1]
try:
    query = sys.argv[2]
except:
    pass
if search_from == "baidu":
    webbrowser.open("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=" + query + "&fenlei=256&rsv_pq=fc77d0fd0018a5e9&rsv_t=e443gZ1p46EC1gVlEoNpo0zT65yJopy34lhHz%2FegRrl0W6Lo28eLDbQo0FE&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=714&rsv_sug4=1365")
if search_from == "bingchina":
    webbrowser.open("https://cn.bing.com/search?q=" + query + "&qs=n&form=QBLH&sp=-1&pq=python&sc=9-6&sk=&cvid=4359830E084843B7A6614F3A6AE26348")
if search_from == "binginternational" or search_from == "binginter":
    webbrowser.open("https://cn.bing.com/search?q=" + query + "&go=提交&qs=n&form=QBLHCN&sp=-1&pq=python&sc=8-6&sk=&cvid=5787F8912CB947CAB554B2197BE10513")
if search_from == "sogou":
    webbrowser.open("https://www.sogou.com/web?query=" + query + "&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=856&sst0=1587806010866&lkt=6%2C1587806010011%2C1587806010684&sugsuv=1587806008286071&sugtime=1587806010866")
if search_from == "weather":
    webbrowser.open("http://www.weather.com.cn/weather1d/101010100.shtml#search")
if search_from == "weatherinternational" or search_from == "weatherinter":
    webbrowser.open("weather.com")
