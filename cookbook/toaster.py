#https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen
import plyer.platforms.win.notification
from plyer import notification
import time

notification.notify("Alert", "Va faire une promenade")
time.sleep(30)
notification.notify("Alert", "Va faire une promenade")
