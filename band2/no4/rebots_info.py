import urllib.robotparser


class RebotsInfo(object):
    def __init__(self):
        return

    def getRobots(self, urlHead):
        url = urlHead + "/rebots.txt"
        pars = urllib.robotparser.RobotFileParser()
        pars.set_url(url)
        print(url)
        pars.read();
        userAgent = 'band2spider'
        oaUrl = "http://localhost:8080/oa/oa.jsp"
        # pars.
        if pars.can_fetch(userAgent, oaUrl):
            print("可以访问")
        else:
            print("不可以访问")
        print(pars)
        return "hello"