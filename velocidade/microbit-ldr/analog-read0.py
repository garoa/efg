from microbit import sleep, pin0, pin1, display, button_a

def calibrate(pin_number, debug=):
    pin = [pin0, pin1][pin_number]
    arrow = '<>'[pin_number]
    arrow = arrow * 2
    sample_size = 10
    values = []
    for i in range(sample_size):
        sleep(10)
        values.append(pin.read_analog())
    values.sort()
    median = values[len(values)//2]
    display.scroll(arrow + str(median) + arrow, delay=70)
    sleep(1000)
    return median

def main():
    display.show('FJR ')
    while True:
        median = calibrate(0)
        median = calibrate(1)

main()

