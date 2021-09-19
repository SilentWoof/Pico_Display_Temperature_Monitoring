import machine
import utime
import picodisplay as display

# **--------------------------------------------------**
# Configure Pico Display
# **--------------------------------------------------**
# Pico Display resolution is 240 x 135 pixels
display_width = display.get_width()
display_height = display.get_height()
display_buffer = bytearray(display_width * display_height * 2)
display.init(display_buffer)

# Set the display backlight to 50%
display.set_backlight(0.5)

# set some fixed screen elemanets
def display_legend():
    display.set_pen(0, 0, 0)
    display.rectangle(0, 104, 240, 31)
    display.set_pen(255, 255, 255)
    display.text("-60", 1, 1, 50, 3)
    display.text("m", 50, 8, 25, 2)
    display.text("now", 187, 1, 50, 3)
    display.text(str(core0_loop_n), 105, 1, 100, 2)

# Define taking temperature notification
def taking_temp_note():
    display.set_led(100, 0, 150) # magenta
    utime.sleep(0.1)
    display.set_led(0, 0, 0) # black
    utime.sleep(0.1)

# Define colours for display LED based on temperature range
def led_temp():
    if temperature > t_hot:
        display.set_led(255, 0, 0) # red
    elif temperature < t_cold:
        display.set_led(0, 0, 50) # blue
    else:
        display.set_led(0, 50, 0) # green

# Define display LED off
def led_off():
    display.set_led(0, 0, 0) # black

# **--------------------------------------------------**
# Configure Pico's Onboard temperature sensor
# **--------------------------------------------------**
# reads from Pico's temp sensor and converts it into a more manageable number
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535)

# add a variable to manually adjust the accuracy of the sensor
t_adjust = 1.5

# set the upper and lower temperature limits
t_hot = 25
t_cold = 18

temperatures = []

# **--------------------------------------------------**
# Define Console Print Info for Debugging
# **--------------------------------------------------**
def status_print():
    print("*--------------------------*")
    print("Core 0 Loop #" + str(core0_loop_n))
    print("*--------------------------*")
    print("Sensor reading: " + str(reading))
    print("Temperature: " + str(temperature))
    print("Decimal temperature: " + str(temp_float))
    print("Screen Display: " + str(temp_float) + "c")
    print("*--------------------------*")
    print("\n")

# **--------------------------------------------------**
# Configure Additional Variables
# **--------------------------------------------------**
# Loop counter
core0_loop_n = 0

while True:
    # start counting the loops
    core0_loop_n += 1
    
    # blackout the screen
    display.set_pen(0, 0, 0)
    display.clear()
    
    # taking teperature notification
    taking_temp_note()

    # the following two lines convert the value from the temp sensor into celsius
    reading = (sensor_temp.read_u16() * conversion_factor)
    temp_float = round((27 - (reading - 0.706) / 0.001721) + t_adjust, 1)
    temperature = int(temp_float)

    # drawing the graph on the screen
    # shifts the temperatures history to the left by one sample
    if len(temperatures) > 60:  # 240 pixels screen width / 4 pixels per reading value
        temperatures = temperatures[1::]
    else:
        temperatures.append(temperature)

    i = 0

    for t in temperatures:
        # chooses a pen colour based on the temperature
        display.set_pen(0, 255, 0) # green
        if t > t_hot:
            display.set_pen(255, 0, 0) # red
        elif t < t_cold:
            display.set_pen(0, 0, 255) # blue
    
        # draws the reading as a tall, thin rectangle
        display.rectangle(i, display_height - (t * 3), 4, display_height)

        # the next tall thin rectangle needs to be drawn 4 pixels to the right of the last one
        i += 4

    # draws a black background for the text at the bottom of the screen
    display_legend()
    
    # sets the temperature reading as text in the black box at the bottom of the screen
    display.set_pen(0, 255, 0)
    if t > t_hot:
        display.set_pen(255, 0, 0)
    elif t < t_cold:
        display.set_pen(0, 0, 255)
    display.text(str(temp_float) + "c", 70, 103, 0, 5)
    
    # update the display
    display.update()
    
    # print information to console
    status_print()

    # Toggle LED to Show Thread is running and set the interval between checks
    # LED Flashes with a half second interval so value is number of seconds required x 2.
    for delay in range(60):
        led_temp()
        utime.sleep(0.25)
        led_off()
        utime.sleep(0.25)
