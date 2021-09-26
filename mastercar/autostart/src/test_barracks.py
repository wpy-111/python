from driver import *
from obstacle import *
driver = Driver()
driver.stop()
time.sleep(0.5)

driver.driver_run(30, 30)
time.sleep(0.6)
driver.driver_run(0, -40)
time.sleep(1)
driver.driver_run(-30, -30)
time.sleep(0.7)
driver.stop()
for i in range(0, 3):
    Lightwork(2, "red")
    time.sleep(0.2)
    Lightwork(2, "off")
    time.sleep(0.1)
driver.driver_run(30, 30)
time.sleep(0.65)
driver.driver_run(0, 40)
time.sleep(0.9)
driver.stop()
