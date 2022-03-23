import os
from PIL import Image
import random

random.seed(version=2) 

def random_gen():
    individual = '-|-|-|-|-'

    part1 = random.randint(0, len(background)-1)
    part2 = random.randint(0, len(border)-1)
    part3 = random.randint(0, len(filler)-1)
    part4 = random.randint(0, len(rhomb)-1)
    part5 = random.randint(0, len(rock)-1)

    if part2==4:
        part3 = '-'
        part4 = '-'

    if part4!=2:
        part4 = '-'

    individual = str(part1) + '|' + str(part2) + '|' + str(part3) + '|' + str(part4) + '|' + str(part5) 
    print(str(i)+'---'+str(len(genesis))+'---'+individual)
    return individual

def is_unique_gen(next_gen):
    try:
        pos = genesis.index(next_gen)
    except:
        pos = -1
    if pos == -1:
        return True
    else:
        return False


def make_png(num, next_gen):
 
    im1 = Image.open(dir_png+background[int(next_gen.split('|')[0])])
    
    void=0
    try:
        im2 = Image.open(dir_png+border[int(next_gen.split('|')[1])])
        im1.paste(im2, (0, 0), mask=im2)
        im2.close()
    except:
        void=0
    
    try:
        im2 = Image.open(dir_png+filler[int(next_gen.split('|')[2])])
        im1.paste(im2, (0, 0), mask=im2)
        im2.close()
    except:
        void=0

    if next_gen.split('|')[1]=='4':
        try:
            im2 = Image.open(dir_png+'20.png')
            im1.paste(im2, (0, 0), mask=im2)
            im2.close()
        except:
            void=0

    try:
        im2 = Image.open(dir_png+rhomb[int(next_gen.split('|')[3])])
        im1.paste(im2, (0, 0), mask=im2)
        im2.close()
    except:
        void=0

    try:
        im2 = Image.open(dir_png+'19.png')
        im1.paste(im2, (0, 0), mask=im2)
        im2.close()
    except:
        void=0

    
    try:
        im2 = Image.open(dir_png+rock[int(next_gen.split('|')[4])])
        im1.paste(im2, (0, 0), mask=im2)
        im2.close()
    except:
        void=0

    im1.save(dir_result+str(num+1)+'.png', format='png')
    im1.close()
    

    return 0


background = ['31.png', '32.png','33.png', '34.png','35.png', '39.png', '36.png','37.png', '38.png','40.png']
border = ['21.png', '22.png', '24.png', '26.png', '18.png']
rock = ['1.png', '2.png','3.png', '25.png', '4.png', '5.png']
filler = ['6.png', '7.png','8.png', '9.png','14.png', '15.png','16.png', '17.png','10.png', '11.png','12.png', '13.png']
rhomb = ['none.png', 'none.png', '23.png', 'none.png']

dir_result = './result/'
dir_png = './png/'

need_items = 1000
genesis = []

#max = 10 * 5 * 6 * 12 * 2 = 7200
#collection of random 1000

print('Compute the enemies')


for i in os.listdir(dir_result):
    os.remove(dir_result+i)


for i in range(need_items):
    next_gen = '0'
    while not is_unique_gen(next_gen) or next_gen == '0':
        next_gen = random_gen()
    genesis.append(next_gen)
    make_png(i, next_gen)


#save log
log = ""     
for x in genesis:
  log += x+'\n'
print(log)
f = open('genesis.log', 'w')
f.write(log)


print('Done')