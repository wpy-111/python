from joystick import JoyStick
from cart import Cart
import time
import cv2
import threading
import json
import config
cart = Cart()
from collections import deque
class SafeQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.queue = deque([])
    self.remaining_space = threading.Semaphore(capacity)
    self.fill_count = threading.Semaphore(0)

  def append(self, item):
    self.remaining_space.acquire()
    self.queue.append(item)
    self.fill_count.release()

  def consume(self):
    self.fill_count.acquire()
    item = self.queue.popleft()
    self.remaining_space.release()
    return item

class DataItem:
    def __init__(self, axis, image):
        self.axis = axis
        self.image = image

queue = SafeQueue(3)

class Logger:

    def __init__(self):
        self.camera = cv2.VideoCapture(config.front_cam)
        self.started = False
        self.stopped_ = False
        self.counter = 0
        self.map = {}
        self.result_dir = "train"

    def start(self):
        self.started = True
        cart.steer(0)
        pass

    def stop(self):
        if self.stopped_:
            return
        self.stopped_ = True
        cart.stop()
        path = "{}/result.json".format(self.result_dir)
        with open(path, 'w') as fp:
            json.dump(self.map.copy(), fp)
        pass

    def log(self, axis):
        if self.started :
            item  = queue.consume()
            axis = item.axis
            image = item.image
            path = "{}/{}.jpg".format(self.result_dir, self.counter)
            self.map[self.counter] = axis
            cv2.imwrite(path, image)
            self.counter = self.counter + 1

    def stopped(self):
        return self.stopped_

js = JoyStick()
logger = Logger()

def joystick_thread():
    print("before open")
    js.open()
    while not logger.stopped():
        # print("loop")
        time, value, type_, number = js.read()
        # print(value)
        if js.type(type_) == "button":
            print("button:{} state: {}".format(number, value))
            if number == 6 and value == 1:
                logger.start()
            if number == 7 and value == 1:
                logger.stop()
        if js.type(type_) == "axis":
            print("axis:{} state: {}".format(number, value))
            if number == 2:
                # handle_axis(time, value)
                js.x_axis = value * 1.0 / 32767

        if logger.started:
            return_value, image = logger.camera.read()
            item = DataItem(js.x_axis, image)
            queue.append(item)
            cart.steer(js.x_axis)


def main():
    t = threading.Thread(target=joystick_thread, args=())
    t.start()

    # logger.start()
    while not logger.stopped():
        # time.sleep(0.01)
        logger.log(js.x_axis)

    t.join()
    cart.stop()

main()
logger.stopped()
logger.camera.release()
cart.stop()
