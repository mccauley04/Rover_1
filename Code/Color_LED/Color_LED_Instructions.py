'''
1. Raspberry Pi Platform - Color LED
2. Test Color_LED - & Different Colors

If Coding with Python -->

We need to input: python ColorLED.py
To end : Ctrl-C and then

chmod 777 initpin.sh
./initpin.sh

---------------------------------------------------------

If coding with C -->
We need to input: gcc ColorLED.c -o ColorLED -lwiringPi
We need to run the compiled code: ./ColorLED

To see the level state changes of the pins type: gpio readall

End processes: ctrl+c

Now, the state of the relevant pin is uncertain at this time, we also need to run a script to initialize all pins:
chmod 777 initpin.sh
./initpin.sh


'''