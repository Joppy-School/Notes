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
