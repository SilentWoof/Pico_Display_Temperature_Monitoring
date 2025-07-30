# 🌡️ Pico Display Temperature Monitor

A real-time temperature monitoring project for Raspberry Pi Pico with Pimoroni's Pico Display. This script reads from the onboard temperature sensor, displays readings graphically on the Pico Display, and uses color-coded LED indicators based on temperature thresholds.

## 📦 Features

- Real-time temperature tracking and display
- Color-coded graph bars (green, red, blue)
- LED notification system
- Console debug output
- Adjustable accuracy and threshold settings

## 🛠️ Requirements

- Raspberry Pi Pico
- Pimoroni Pico Display
- MicroPython and required libraries:
  - `machine`
  - `utime`
  - `picodisplay`

## 🚀 Getting Started

1. Copy the `temp-mon.py` script to your Pico.
2. Run the script with MicroPython.
3. Watch the display light up with your ambient temperature readings in real time!

## ⚙️ Configuration

You can tweak the following variables in the script:

```python
t_hot = 25       # Temperature threshold for 'hot' (in Celsius)
t_cold = 18      # Temperature threshold for 'cold'
t_adjust = 1.5   # Manual sensor calibration value

## 📈 Display Legend

- 🔴 **Red bar**: Hot (above `t_hot`)
- 🔵 **Blue bar**: Cold (below `t_cold`)
- 🟢 **Green bar**: Normal range

## 👨‍💻 Debug Output

The script prints sensor readings, temperature values, and loop count to the console for troubleshooting and performance tracking.

---

[SilentWoof](https://github.com/SilentWoof)  
Original script: [`temp-mon.py`](https://github.com/SilentWoof/Pico_Display_Temperature_Monitoring/blob/main/temp-mon.py)

