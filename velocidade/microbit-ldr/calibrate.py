from microbit import sleep, pin0, pin1, display, button_a

def calibrate(pin_number):
    pin = [pin0, pin1][pin_number]
    display.scroll('Block LDR ' + str(pin_number))
    sample_size = 10
    values = []
    for i in range(sample_size):
        sleep(100)
        values.append(pin.read_analog())
    values.sort()
    median = values[len(values)//2]
    display.scroll('Median: ' + str(median))
    return median

def main():
    display.show('FJR ')
    while True:
        if button_a.get_presses():
            median = calibrate(1)

main()

