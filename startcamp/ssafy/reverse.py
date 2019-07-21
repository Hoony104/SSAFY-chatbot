# with open('problem.txt','w', encoding='utf-8') as p:
#     for i in range(4):
#         p.write(f'{i}\n')

with open('problem.txt', 'r', encoding='utf-8') as pr:
    read=pr.readlines()
    print(read)


with open('problem.txt','w', encoding='utf-8') as pd:
    read.reverse()
    print(read.reverse())
    s=''
    for j in read:
        s+=j
    print(s)
    pd.writelines(s)