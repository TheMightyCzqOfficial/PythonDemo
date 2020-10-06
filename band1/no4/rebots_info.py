import urllib.robotparser

class RebotsInfo(object):
    def __init__(self):
        return

    def get_rebots(self, rebotsName):
        rb = urllib.robotparser.RobotFileParser()
        rb.set_url(rebotsName)
        rebots = rb.read()
        print(rebots)
        return rebots