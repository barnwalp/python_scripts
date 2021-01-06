import psutil
import ctypes


def message_box(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


battery = psutil.sensors_battery()

if battery.percent < 35 and not battery.power_plugged:
    message_box(f'Battery is below 25% capacity', 'Plug your charger', 1)
elif battery.percent > 85 and battery.power_plugged:
    message_box(f'Battery is above 85% capacity', 'UnPlug your charger', 1)

