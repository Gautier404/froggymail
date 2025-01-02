## A playground to start experimenting with my thermal printer functionality

import serial
import time

bytedelay = 0.00057346
dot_feed_s = 0.0021
dot_print_s = 0.03
line_spacing = 6

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=3000)

def write_char(char: str) -> None:
    resume = time.monotonic() + bytedelay
    while time.monotonic() < resume:
        pass
    uart.write(bytes(char, "ascii"))
    if char == "\n":
        resume = time.monotonic() + + line_spacing*dot_feed_s
        while time.monotonic() < resume:
            pass
    
def write(text: str) -> None:
    for char in text:
        write_char(char)

write("1/1/2025 Testing out my new thermal printer I bought for cheap off of ebay")
write_char("\n") 
write_char("\n")
write("This")
write_char("\n")
write_char("\n")
write("is")
write_char("\n")
write_char("\n")
write("a")
write_char("\n")
write_char("\n")
write("test")
write_char("\n")
write_char("\n")
write("Thank you! :)")
write_char("\n")
write_char("\n")
write_char("\n")

