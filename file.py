import os

# a=os.listdir()
# print(a)
# os.rename('dog.py','hello.py')
# b=os.listdir()
# print(b)

# for i in range(100) :
#     print(os.system('touch a{0}.txt'.format(i[3])))
#     i+=1

# for i in range(100) :
#     print('touch a{0}.txt'.format(i))
#     i+=1

# for i in range(100) :
#     print('touch a' + str(i)[::3])
#     i+=1

os.chdir('report')
for i in range(100) :
    os.system(f'touch report{str(i).zfill(3)}.txt')
    i+=1

files=os.listdir()
for name in files:
    os.rename(name, 'samsung_'+name)

for i in range(100) :
    os.rename('samsung_report{0}.txt'.format(str(i).zfill(3)), 'samsung_report{0}.txt'.format(str(i+950).zfill(3)))
    i+=1

files2=os.listdir()
for name in files2:
    os.rename(name, name.replace('samsung','SSAFY'))

# files3=os.listdir()
# for name in files3:
#     os.system('rm {0}'.format(name))

# for i in range(100) :
#     os.rename('report{0}.txt'.format(str(i).zfill(3)), 'report{0}.txt'.format(str(i+333).zfill(3)))
#     i+=1