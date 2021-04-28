import time
import struct
from serial_port import serial_connection
serial = serial_connection

class Button:
    def __init__(self, port, buttonstr):
        self.state = False
        self.port = port
        self.buttonstr = buttonstr
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 05 00 01 E1 {} 01 0A'.format(port_str))

    def clicked(self):
        serial.write(self.cmd_data)
        response = serial.read()
        buttonclick="no"
        if len(response) == 9 and  response[5]==0xE1 and response[6]==self.port:
            button_byte=response[3:5]+bytes.fromhex('00 00')
            button_value=struct.unpack('<i', struct.pack('4B', *(button_byte)))[0]
            # print("%x"%button_value)
            if button_value>=0x1f1 and button_value<=0x1ff:
                buttonclick="UP"
            elif button_value>=0x330 and button_value<=0x33f:
                buttonclick = "LEFT"
            elif button_value>=0x2ff and button_value<=0x30f:
                buttonclick = "DOWN"
            elif button_value>=0x2a0 and button_value<=0x2af:
                buttonclick = "RIGHT"
            else:
                buttonclick
        return self.buttonstr==buttonclick

class UltrasonicSensor():
    def __init__(self, port):
        self.port = port
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 04 00 01 D1 {} 0A'.format(port_str))

    def read(self):
        serial.write(self.cmd_data)
        # time.sleep(0.01)
        return_data = serial.read()
        if len(return_data)<11 or return_data[7] != 0xD1 or return_data[8] != self.port:
            return None
        # print(return_data.hex())
        return_data_ultrasonic = return_data[3:7]
        ultrasonic_sensor = struct.unpack('<f', struct.pack('4B', *(return_data_ultrasonic)))[0]
        # print(ultrasonic_sensor)
        return int(ultrasonic_sensor)


class Light:
    def __init__(self, port):
        self.port = port
        self.port_str = '{:02x}'.format(port)

    def lightcontrol(self, which, Red, Green, Blue):  # 0代表全亮，其他值对应灯珠亮，1~4
        #“{:02d}”.format(i)表示将i变为两位十进制数字的字符串，不够两位用0填充。
        which_str = '{:02x}'.format(which)
        Red_str = '{:02x}'.format(Red)
        Green_str = '{:02x}'.format(Green)
        Blue_str = '{:02x}'.format(Blue)
        cmd_servo_data = bytes.fromhex('77 68 08 00 02 3B {} {} {} {} {} 0A'.format(self.port_str, which_str, Red_str \
                                                                                    , Green_str, Blue_str))
        serial.write(cmd_servo_data)

    def lightoff(self):
        cmd_servo_data1 = bytes.fromhex('77 68 08 00 02 3B 02 00 00 00 00 0A')
        cmd_servo_data2 = bytes.fromhex('77 68 08 00 02 3B 03 00 00 00 00 0A')
        cmd_servo_data = cmd_servo_data1 + cmd_servo_data2
        serial.write(cmd_servo_data)


class Motor_rotate:
    def __init__(self, port):
        self.port = port
        self.port_str = '{:02x}'.format(port)

    def motor_rotate(self, speed):
        cmd_servo_data = bytes.fromhex('77 68 06 00 02 0C 02') + bytes.fromhex(self.port_str) + \
                         speed.to_bytes(1, byteorder='big', signed=True) + bytes.fromhex('0A')
        serial.write(cmd_servo_data)


class Test:
    pass

if __name__ == '__main__':
    on_off_button = LimitSwitch(1)
    start_button = Button(1, "UP")
    stop_button = Button(1, "DOWN")
    left_button=Button(1, "LEFT")
    right_button = Button(1, "RIGHT")
    motor=Motor_rotate(1)
    removemotor=Motor_rotate(2)
    servo1=Servo(3)
    ultr_sensor=UltrasonicSensor(4)
    servo2=Servo_pwm(2)
    servo3 = Servo(1)
    magsens=Magneto_sensor(3)
    # removemotor = Motor_rotate(1)
    # mk =SerialAssistant()
    # mk.start_port()
    time.sleep(1)
    while True:
        km=magsens.read()
        print(km)
        # removemotor.motor_rotate(30)
        # time.sleep(0.5)
        # removemotor.motor_rotate(-30)
        # time.sleep(0.5)
    # while True:
        # servo2.servocontrol(70,30)
        # print("aaaaaa")
        # time.sleep(2)
        # servo1.servocontrol(5,100)
        # print("bbbbbb")
        # time.sleep(2)
        # # servo2.servocontrol(56,30)
        # # time.sleep(2)
        # servo2.servocontrol(30,30)
        # print("cccccc")
        # time.sleep(2)
        # servo1.servocontrol(-85,100)
        # print("dddddd")
        # time.sleep(2)
        #
        # servo1.servocontrol(-85, 30)
    # mk.handler()


    # while True:
    #     print()
    #     servo1.servocontrol(-85, 30)
    #     time.sleep(3)
    #     servo1.servocontrol(5, 30)
    #     time.sleep(3)
    # while True:
        # print("start_button={},stop_button={}".format(start_button.clicked(),stop_button.clicked()))
        # print("stop_button=%d" % stop_button.clicked())
        # print("left_button=%d" % left_button.clicked())
        # print("right_button=%d" % right_button.clicked())
        # distance=ultr_sensor.read()
        # print(distance)
        # print(type(distance))

