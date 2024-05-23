import re


text = """Blow the dice for me, woo
Put your pretty-ass lips together
Blow it real nice for me (blow it real nice for me)
Yeah, I'm tryna hit a lick
And slide to the dealership in the mornin' (why?)
Poppa need a brand new foreign
Uh, hot hand, they not gon' believe me
But check the recordin'
Ooh, just touched down (down), up a few thou' (thou')
Big booty hoes with me in the penthouse (baow)
Bar full of liquor (liquor), cash for the strippers (strippers)
It gon' get weird tonight, so no pictures (nah)
Pretty motherfucker with some money to blow
I'm 'bout to buy Las Vegas after this roll
I'm 'bout to buy Las Vegas after this roll
Come on, seven, seven, seven, let's go (ooh-wee)
Yes Lawd (ah)
(Don't touch the money, baby)
(Don't touch the money, baby, oh) woo
Ayy, now we makin' money, now we makin' money
Now we makin' money (one, two, three)
Spin the wheel for me (hoo)
Blackjack, baccarat
Dealer where you at? Deal for me
(Dealer where you at, where you at?)
Woo, give me the chips, give me the chips
Give it some magic, go all in (why?)
I can see the champagne fallin'
I got bills to pay, but bills can wait
Ah, fuck it, we ballin'
Stacks on stacks (stacks), racks on racks (racks)
Moonwalk to the money like I'm Mike Jack' (ow)
Yes, I'm faded (ayy), pupil's dilated
But the man in the mirror sayin', "Gon' get your paper" (get it)
Pretty motherfucker with some money to blow
I'm 'bout to buy Las Vegas after this roll
I'm 'bout to buy Las Vegas after this roll
Come on, seven, seven, seven, let's go (oh)
Oh my God
Silk Sonic
This the big one, uh
You gotta trust your gut (you gotta trust your gut, uh)
Can you feel it? (I can feel it)
Ooh (ooh), this the big one (big money)
You gotta trust your gut (you gotta trust your gut now, now)
Can you feel it? (I can feel it)
Pretty motherfucker with some money to blow
I'm 'bout to buy Las Vegas after this roll
I'm 'bout to buy Las Vegas after this roll
Come on, seven (seven), seven (seven), seven, (woo) let's go
Ah-ha
(I told ya, I told ya, I told ya)
Seven (seven), seven (seven), seven, let's go
(Woo, ooh) they can't deal with me, I swear to God"""

# 특수문자 제거
new_text = re.sub(r'[^\w\s]', '', text)

# 줄단위로 split
text_split = new_text.splitlines()

# 줄단위로 split해서 나온 list의 총 갯수: 54
split_count = len(text_split)

# 띄어쓰기 단위로 split
map = []
for i in range(split_count):
    map.append(text_split[i].split(' '))


# worker 5대가 있다고 가정하여 mapping(for문 하나가 worker 하나임)
map_1 = []
for i in range(0, 10):
    map_count = len(map[i])
    for n in range(map_count):
        map_1.append((map[i][n], 1))

map_2 = []
for i in range(10, 20):
    map_count = len(map[i])
    for n in range(map_count):
        map_2.append((map[i][n], 1))

map_3 = []
for i in range(20, 30):
    map_count = len(map[i])
    for n in range(map_count):
        map_3.append((map[i][n], 1))

map_4 = []
for i in range(30, 40):
    map_count = len(map[i])
    for n in range(map_count):
        map_4.append((map[i][n], 1))


map_5 = []
for i in range(40, 54):
    map_count = len(map[i])
    for n in range(map_count):
        map_5.append((map[i][n], 1))

# 분할해서 작업한 것을 하나로 합침
map_all = map_1 + map_2 + map_3 + map_4 + map_5

# reduce
reduce = {}
for i in map_all:
    if i[0] not in reduce.keys():
        reduce[i[0]] = 1
    else:
        reduce[i[0]] += 1
print(reduce)

# 참고 https://langho.tistory.com/7