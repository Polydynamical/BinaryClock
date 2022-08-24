try:
    from tkinter import *
except:
    from Tkinter import *
from datetime import datetime
from math import log

def decimal_to_binary(number):
    arr = []
    tmp = number
    while tmp != 0:
        i = 0.5
        while tmp > 0:
            i *= 2
            i = int(i)
            tmp -= i
        arr.append(int(i))
        tmp += i - 1
    ans = "000000"
    for x in arr:
        posn = 5 - int(log(x, 2))
        ans = ans[:posn] + "1" + ans[posn + 1:]
    return ans

# Window Info
window_width = 1920
window_height = 1080

hours_bin = "000011"
mins_bin = "001011"
secs_bin = "011001"

# Circle Geometry
width = 80
x_spacing = 200
y_spacing = 100

x_start = window_width // 2
y_start = (window_height - 6 * (y_spacing)) // 2

# GUI
window = Tk()
window.geometry(f"{window_width}x{window_height}")
def clock():
    
    # Time Processing
    hours = int(datetime.now().strftime("%H"))
    mins  = int(datetime.now().strftime("%M"))
    secs  = int(datetime.now().strftime("%S"))

    hours_bin = decimal_to_binary(hours)
    mins_bin  = decimal_to_binary(mins)
    secs_bin  = decimal_to_binary(secs)

    # Hours (five circles)
    for i in range(0, 6):
        if i == 0:
            continue
        # 00011
        if int(hours_bin[i]):
            hours_fill = "red"
        else:
            hours_fill = "blue"
        c.create_oval(x_start - x_spacing - width // 2, y_start + y_spacing*i - width // 2, x_start - x_spacing + width // 2, y_start + y_spacing * i + width // 2, fill=hours_fill)

    # Minutes (six circles)
    for i in range(0, 6):
        if int(mins_bin[i]):
            mins_fill = "red"
        else:
            mins_fill = "blue"
        c.create_oval(x_start - width // 2, y_start + y_spacing*i - width // 2, x_start + width // 2, y_start + y_spacing * i + width // 2, fill=mins_fill)

    # Seconds (six circles)
    for i in range(0, 6):
        if int(secs_bin[i]):
            secs_fill = "red"
        else:
            secs_fill = "blue"
        c.create_oval(x_start + x_spacing - width // 2, y_start + y_spacing*i - width // 2, x_start + x_spacing + width // 2, y_start + y_spacing * i + width // 2, fill=secs_fill)
    window.after(1000, clock)

c = Canvas(window, width=window_width, height=window_height)
c.pack()
clock()
window.mainloop()

# self.state = on
# self.state = off
# tk.update()
