# BeGeDo B.V. 

BeGeDo is a company that is specialized in the repairing of moulds. 

## Machine
They have a Machine called the `Vario Laser 9000 Compact` which is a laser welding machine. This machine is used to repair moulds. They do this by adding metal to the moulds. By adding metal to the moulds they can decrease the gaps in the moulds. This is important because the gaps in the moulds can cause the plastic to leak out of the moulds. 

## Plan of action
The current plan of action of mine is to create a bunch of small modules around the machine that can communicate with eachother. These modules will be able to communicate with eachother using the serial ports. So I will make a wall plug that will turn 230 volt AC to something more manageable like 5 volt DC. This will be used to give power to the difference modules around the machine.

## Modules
The following modules will be custom made for this project:
- Wall plug (Alias: Hub)
    - ![Wall plug](/pictures/projects/BeGeDo/WallPlugBasicPrinciple.png)
    - This module will be used to turn 230 volt AC to 5 volt DC. This will be used to power the other modules.
    - because it is a central module it will also be used to communicate with the other modules. (This will be done using a raspberry pi, the version is not yet specified)
    - If you were to remove the raspberry pi and connect your own laptop to the plug it would appear as a usb hub with 4 serial ports.
    - This module will consist of the following:
        - A raspberry pi
        - A 230 volt AC connector
        - A usb C port for power and for the raspberry pi to communicate with the other modules
        - A few usb c ports for power and commications to the other modules
        - A few 12 volt DC connectors (POWER ONLY) to provide power to the other modules (This is done so you don't have to boost the 5 volt DC to 12 volt DC)
 
- Footpedal 
    - This module will be inbetween the footpedal and the machine. This will consist of a relay that will switch the footpedal on or bypassed, this means that as soon as we are starting to give custom commands it will switch the relay to a state where the footpedal has no control. It will also simulate the footpedal to give the machine the signal that the footpedal is pressed. This will be done using a custom made circuit board. This board will consist of the following
        - A relay
        - A microcontroller (Arduino) (intergrated on the board)
        - A usb C port for power and communication with the wall plug
        - A 12 volt DC connector (POWER ONLY) to give the 12 volt DC signals to the machine
    - The relay will be used to switch between the footpedals signal and the signal from the microcontroller. 
    - The microcontroller will be used to simulate the footpedal. 
    - The usb C port will be used to communicate with the Hub
    - A button which will stop the simulation of the footpedal and switch to the footpedal itself. This will be used in case of an emergency.

- Joystick
    - This module will be used to control the X, Y and Z axis of the machine. This will be done using a custom made circuit board. This board will consist of the following:
        - A microcontroller (Arduino) (intergrated on the board)
        - A usb C port for power and communication with the wall plug
        - A 12 volt DC connector (POWER ONLY) to give the 12 volt DC signals to the machine
        - A special connector that will connect the joystick to the machine through the board
        - A relay to switch between the joystick and the microcontroller
        - To make an analog signal for the X and Y axis we will use a potentiometer for each axis, to be specific we will use a digital potentiometer. This make the microcontroller able to control the potentiometer. So it can make a variable voltage between 0 and 12 volt DC. This will be used to control the X and Y axis of the machine.
        - A button which will stop all movement of that is provided by the microcontroller and switch to the joystick. This will be used in case of an emergency.
            - This will also automatically turn on when the joystick is moved. This is done so that as soon as someone touches the joystick it will make them be in control of the machine.
            - This will also automatically turn the following modules off:
                - The footpedal

- Display (Alias: Screen, Interface)
    - This module will be used to display the current status of all the modules. This will be done using a custom made circuit board. This board will consist of the following:
        - A microcontroller (Arduino) (intergrated on the board)
        - A usb C port for power and communication with the wall plug
        - A Second usb C port for special communication with an external device (This can be used to debug the system, or to test if everything on the display can be shown correctly)
        - A 12 volt DC connector (POWER ONLY) to give the 12 volt DC signals to the machine
        - A screen to display the current status of all the modules
        - A button which will stop all movement of that is provided by the different modules around the machine. This will be used in case of an emergency. This will turn the following modules off:
              - The footpedal
              - The joystick
        - A RGB led to indicate the current status of the machine
            - Green: Everything is working as it should
            - Yellow: Something is not working as it should, but it is not critical
            - Red: Something is not working as it should, and it is critical
            - Purple: The modules are in recording mode (This means that it will start recording all the movements of the machine for later replay)
            - blue: The modules are in replay mode (This means that it will replay all the movements that were recorded earlier)
        - A buzzer to indicate different states of the machine, look at [`Buzzer number to beeps`](#buzzer-number-to-beeps) for more information

### buzzer number to beeps
Every number will have a different beep pattern. The following beep patterns will be used:
    All beeps will be 0.25 seconds long
    The long beeps will have a pause of 2 seconds between them
    The normal beeps will have a pause of 1 second between them
    The fast beeps will have a pause of 0.5 seconds between them

- 1 The machine will start in 5 seconds: 
    - Normal beep 
    - Normal beep 
    - Normal beep 
    - Normal beep 
    - Normal beep
- 2 The machine got a critical error and will stop: 
    - Fast beep 
    - Fast beep
    - Fast beep
    - Fast beep
    - Fast beep
- 3 The emergency button has been pressed:
    - Long beep
    - Long beep
    - Long beep
    - Long beep
    - Long beep
- 4 The machine is in a communcation error with the hub:
    - Long beep
    - Normal beep
    - Long beep
    - Normal beep
    - Long beep