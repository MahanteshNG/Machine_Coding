import random

def snake_ladder(currentposition,dice):
    nextposition=currentposition+dice;
    if nextposition in snakes.keys():
        return snakes[nextposition]
    elif nextposition in ladders.keys():
        return ladders[nextposition]
    else:
        return nextposition

#Taking All Inputs
snakes={};
s=int(input());
for i in range(s):
    x,y=map(int,input().split(" "));
    snakes[x]=y;


ladders={};
l=int(input());
for i in range(l):
    x,y=map(int,input().split(" "));
    ladders[x]=y;

players={};
p=int(input());
for i in range(p):
    x=input();
    players[x]=0;


#set max =0 so that when any one player reaches 100 gave should stop
max=0;
while max<100:
    for name,position in players.items():
        dice=random.randint(1,6);
        currentposition=position;
        nextposition=snake_ladder(currentposition,dice);

        if nextposition==100:
            print(name+" wins the game");
            max=100;
        elif nextposition>100:
            players[name]=currentposition;
        else:
            players[name]=nextposition;
            print("%s rolled a %d and moved from %d to %d" %(name,dice,currentposition,nextposition));


#in bash USE cat Sample_Input | SnakeLadder.py cmd to use input ftom the file.
#in cmd use Sample_Input SnakeLadder.py