# with open('ssafy.txt','w', encoding='utf-8') as f:
#     for i in range(6):
#         f.write('16시 20m\n')

with open('ssafy.txt', 'r', encoding='utf-8') as r:
    result=r.readlines()
    print(result)