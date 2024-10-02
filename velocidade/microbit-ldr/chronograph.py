from microbit import sleep, pin0, pin1, display
from utime import ticks_ms, ticks_diff

def main():
    display.show('FJR ')
    while True:
        u0 = pin0.read_analog()
        if u0 < 500:
            t0 = ticks_ms()
            while True:
                u1 = pin1.read_analog()
                if u1 < 500:
                    dt = ticks_diff(ticks_ms(), t0)
                    for i in range(3):
                        display.scroll(str(dt) + '...', delay=70)
                    break

main()

