import random
import copy
summ=0
rounds=1
mesos=0
value=0

test=[]
for i in range(100):
    test.append([])
    for j in range(5):
        test[i].append(0)

players=[]
playersnumbers=[]
bingo=[]

i=0
for i in range(100):
    players.append(i+1)

i=0
for i in range(100):
    playersnumbers.append([])
    for j in range(5):
        playersnumbers[i].append(0)

i=0
for i in range(80):
    bingo.append(0)

x=0
for x in range(1000):
    for i in range(80):
        bingo[i]=random.randint(0,80)
        while (bingo[i]==0):
            bingo[i]=random.randint(0,80)

    i=0
    j=0
    for i in range(100):
        test=copy.copy(bingo)
        for j in range(5):
            value=random.choice(test)
            test.remove(value)
            playersnumbers[i][j]=value

    i=0
    j=0
    b=0
    pl=0
    find=0

    test=copy.copy(bingo)
    for b in range(80):
        if (find==1):
            break
        choice=random.choice(test)
        test.remove(choice)
        for i in range(100):
            for j in range(5):
                if (choice==playersnumbers[i][j]):
                    pl+=1
                if (pl==5):
                    print '----------\nNikitis (Arithmos Pexti): {0}\nArithmoi: {1}\nGiros: {2}\n----------\n'.format(players[i],playersnumbers[i],rounds)
                    find=1
                    break
            if (find!=1):
                summ+=1
            if (find==1):
                break
    find=0
    rounds+=1

mesos=summ/1000
print 'Mesos: {0}'.format(mesos)
