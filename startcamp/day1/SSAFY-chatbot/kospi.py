import requests
import bs4
# url="https://finance.naver.com/sise/"
# page=requests.get(url).text
# docu=bs4.BeautifulSoup(page,'html.parser')
# kospi=docu.select_one('#KOSPI_now').text
# print('현재코스피지수는: '+kospi)

url="http://www.naver.com"
page=requests.get(url).text
docu=bs4.BeautifulSoup(page,'html.parser')
#kospi=docu.select_one('.box > li:nth-child(1) > span:nth-child(2) > em:nth-child(1)').text
kosdoc=docu.select('html body div#PM_ID_ct.wrap div.header div.section_navbar div.area_hotkeyword.PM_CL_realtimeKeyword_base div.ah_list.PM_CL_realtimeKeyword_list_base ul.ah_l li.ah_item a.ah_a span.ah_k')



# print(type(kosdoc))

# for i in range(len(kosdoc)):
#     kosdoc[i]=str(kosdoc[i])[19:]
#     kosdoc[i]=kosdoc[i][:-7]


# for i in range(10):
#     print("{0}위 검색어 : {1}".format(i+1,kosdoc[i]))

print(kosdoc)