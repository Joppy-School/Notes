# My internship at the innovationcenter Civon

# Introduction
During my internship at Civon I worked on a few different projects. While working on these projects I was thrown into the deep end and had to learn a lot of new things on my own. This was because I had to automate a machine on my own. Despite me being thrown into the deep end I learned a lot of new things and I want to learn more about these things in the future. I have also did some other things like coding a little robot called Misty, I have also tested a few VR headsets and games. These games are `First Steps`, `Richie's Plank Experience`, `Beat Saber` and `Keep Talking and Nobody Explodes`. These games i have played on multiple different VR headsets. While I was coding misty I found a few different ways of coding her. These options are `Blockly`, `Python web interface` and `Python API`, While coding different small pieces of Misty I added everything into one and now it is the main software that we use to move Misty around.

# Assignment 1: Laser welding machine
The laser welding machine is a machine that uses high energy laser beams to make a piece of metal so hot that it will weld to another piece of metal. This is a very precise task. This means that the operator of the machine needs to have some experience with the machine, on top of that `BeGeDo` has 2 different laser welding machines and only has 1 operator most of the time. This means that one of the 2 machine will be turned off most of the time. So they assigned me to automate one of the 2 machines so that they can use both machines at the same time.

![Laser welding machine](/pictures/Stage/Civon/BeGeDo/laserWeldingMachine.png)


## plan of action
Maybe it is a good begin to explain a little about the machine's history. this machine is the first of it's kind, made by a german company called `CRONITEX`. This company didn't make any documentation about this machine because it was the first kind to ever be made, so they wanted to keep it a secret on how it works. This was quite a challenge to automate this machine because of the lack of documentation. So I thought of a plan to make control the machine which is simulate the differnt parts of the machine and then simulate it.

### The Joystick
The Joystick is simple part of the machine to simulate (I thought). The Joystick has 4 different analog values that it sends to the machine. These values are `X`, `Y`, `Z` and `R`.
Lets start with the simple values:
- `X`: This is the axis that moves the whole platform from left to right.
- `Y`: This is the axis that moves the whole platform from front to back.
- `Z`: This is the axis that moves the whole platform up and down.

Now the more complicated value:
If you want to move along the `R` axis, you have to add a circular expansion block to the machine. This rotational axis can be used to weld circular parts together. This is the only axis that can not be used without the circular expansion block. So I am just going to forget it even exists

You also have to keep in mind that the machine will move faster if you move the joystick further away from the center. This is not a linear function, this is more of a exponential function with an upper limit.

### The Foot pedal
The foot pedal has a lot of different functions which I will completely forget because they are not that important for the automation of the machine. The only thing that is important to the automation is an analog button that is used to start the laser. This button could have been simple, but ofcourse it is an analog value between 0 and 12 volts

### The interface
To make my system a bit simpler I decided to make a small simple interface. This interface will be made from an arduino mega, a few buttons, 3 seven-segment displays and a few small LED's. This interface is to select how many lines you want to weld.

![Interface prototype](/pictures/Stage/Civon/BeGeDo/PCB/Interface_prototype.png)


# Assignment 2: Misty

![Misty](/pictures/Stage/Civon/Misty/Banner2.jpg)


At Civon we have a small Robot called Misty. Misty is a small robot that can be automated

## Blockly

![Blockly](/pictures/Stage/Civon/Misty/Interface/Blockly.png)

The blockly way is a very simple way to program Misty. This is because you can just drag and drop blocks and connect them together. But it is also very limited because if the blocks that you need are not there you can not create them yourself. so if you want to do something that is not in the blockly interface you are basically forced to use one of the other ways to program Misty. This is why I only used this way to program Misty for a mere 15 minutes.

## Python web environment

![Python web environment](/pictures/Stage/Civon/Misty/Interface/Python.png)

The python web environment is a simple way to program Misty if you know basic python and/or are used to text based programming. This is because you can just type in the code that you want to run on Misty and then run it. When you use this way you will run all the code on misty itself. This means that you can not use any external libraries. This is why I only used this way to program Misty for a maximum of hour or 2.

## API
Misty also has a API that you can use which I used to code Misty. This is because I am used to text based programming, I know python and I had a goal of learning how to use the API. This is why I used this way to program Misty for the rest of my internship. This way of programming is a lot more complicated than the other ways because you have to know how to use the API. This is why I had to read a lot of documentation to learn how to use the API. I found out that I really enjoy reading proper documentation that works and is not outdated. This is why I want to learn more about API's in the future.


# Assignment 3: VR

## The VR headsets

### Oculus Quest 1

![Oculus Quest 1](/pictures/Stage/Civon/VR/Glasses/q1.jpg)

The Oculus Quest 1 is the first edition of the Oculus Quest Series. This headset is a standalone headset. This means that you do not need a computer to use this headset. This headset is also the first headset that I have ever used. On top of that it is the headset I used the most over my time at Civon. It is the headset we use the most on wednesday events and saterday events. Currently it is also the headset that i bought for myself when I saw the price of around 100 euro's for a second hand one on `Marktplaats`. This is why I will mostly be talking about my expierence with this headset in the paragraphs about the games. This headset also has a few downsides. The first downside is that it is a on the heavier side for the quality of the screen and such that you get. This weight is only on the front of the headset which will make the headset press into the bottom of your face (underneath your eyes, just a tiny bit above your cheeks). This will make the headset a bit uncomfortable to wear for a long time. The second downside is that the picture quality is not that great. This is because the screen is not that high in resolutions. Even though the screen is not that high in resolution it is still a very good headset to buy if you want to get into VR.
If you have a computer that is capable of running VR games I would recommend buying the Oculus Quest 1 because of the price.

### Oculus Quest 2

![Oculus Quest 2](/pictures/Stage/Civon/VR/Glasses/q2.webp)

The Oculus Quest 2 is such a big improvement over the Oculus Quest 1. The Oculus Quest 2 has a such a bigger improvement in picture quality, When you combine the 2 screens you get about a 4K screen. For the price of around 200 euro's and a battery life of 4 hours if you use it as an standalone headset, it is a good choice if you have a bit more money to burn. If you have the budget for a Quest 2 then buy this one over the Quest 1. The biggest positive that I know of this headset is that when walking you don't need to create a Gardian (a virtual wall that you can not walk through). This is mostly a software update that is not available on the Quest 1. This means that you can do some chores while wearing the headset to watch some video's. When you look at price to quality ratio this is a very good headset to buy if you have the budget for it.

### Oculus Quest 3

![Oculus Quest 3](/pictures/Stage/Civon/VR/Glasses/q3.png)

The Quest 3 is the newest headset in the Oculus Quest series. This headset is a lot more expensive than the Quest 2. The Quest 3 is a lot more powerful than the Quest 2. The Quest 1 and 2 have black white camera's through which you look when you are not in the Gardian. While the Quest 3 has color camera's. This is an even bigger improvement to the Quest series. The Quest 3 can also be used to do chores while watching video's. It is a lot more comfortable to wear than the other Quests if you also have the external battery pack. This is because the battery pack is on the back of the headset. This means that the weight is more evenly distributed over your head. For the base price of 550 euro's, it is a amazing headset for the different functions it has. This headset has some mixed reality functions that was not available on the Quest 1, The Quest 2 has some of these functions but not all of them. This is why I would recommend this headset if you have the budget for it and you want to play mixed reality games.

## The games

### First Steps

![First Steps](/pictures/Stage/Civon/VR/Games/FirstSteps/Banner.jpg)

First Steps is a simple game that you finish in about 10 to 20 minutes. In this game you learn a lot about the different functions of the Oculus Quest. This game is automaticly added to your library. if you are new to VR, this is a must. 

![First Steps Hands](/pictures/Stage/Civon/VR/Games/FirstSteps/Hands.jpg)

As you can see in the picture above here you will learn how to use your virtual hands. This is a essenstial part of VR. This is because you will use your hands to interact with everything around you. You can learn from trial and Error or you can learn from this game. This game will teach you how to grab things, how to throw things, how to use the menu and how to use the Gardian. This is why I would recommend this game to everyone who is new to VR.

### Richie's Plank Experience
Richie's Plank Experience is not really a game but more of an experience like the name suggests. In this experience you will be standing on a plank that is an unspecified height. This plank is on top of a skyscraper. There are 2 different ground levels that you can choose from. The first one is the normal ground floor like you can see under here

![Richie's Plank Experience](/pictures/Stage/Civon/VR/Games/RPE/GroundLevel.jpg)

Or you can go for the mixed reality ground level. This is a elevator that is inside your actual playing room. This means that you can walk around in your room and you will see the elevator in the game move with you. This is a very cool experience to have. This is why I would recommend this game to everyone who has money to spend on a VR games. This game costs around 20 euro's. This is a bit expensive for a game that you will only play for a few minutes. But it is better to buy this game if you want to show these functions to friends and family.

![Richie's Plank Experience](/pictures/Stage/Civon/VR/Games/RPE/GroundLevelPassthrough.png)


### Beat Saber

![Beat Saber](/pictures/Stage/Civon/VR/Games/BeatSaber/Banner.jpg)

Beat Saber is a game where you have to hit blocks with your sabers. This game is a very fun game to play. You can play this game for hours and hours. If you like to play games like `Music Notes` and `Guitar Hero` then this is a game for you. Even if you don't realise it you will excerise a lot while playing this game. This is because you will be moving your arms a lot. This is why I would recommend this game to everyone who likes to play games like `Music Notes` and `Guitar Hero`. You have to hit the blocks with the right color with the right saber, which gives you better hand-eye coordination.

### Keep Talking and Nobody Explodes

![Keep Talking and Nobody Explodes](/pictures/Stage/Civon/VR/Games/KTANE/Banner.jpg)

Keep Talking and Nobody Explodes is a game where you have to defuse a bomb. This game is a very fun game to play. If you like to play games like puzzle games then this is a game for you. Sadly you are required to have a second person to play this game with. This is because you need a manual to defuse the bomb. This manual is not in the game. This is why I would recommend this game to everyone who like to play puzzle games. This game will also give you a better time management skill and prioritizing skill, you have to defuse the bomb in a certain amount of time. This means that you have to prioritize the different modules on the bomb. This game is amazing to play with friends and family.

# conclusion
I learned a lot during my internship. I learned how a laserwelding machine works. I learned different properties of different VR headsets. I learned how to use the API of Misty. I really enjoyed my time at Civon. I learned a lot and I am planning to learn a lot more about it.