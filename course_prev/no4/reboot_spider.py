import requests
import urllib.robotparser

class RebootInfo(object):
    def __init__(self, domain):
        self.domain = domain
        return

    def print_info(self):
        url = self.domain + "rebots.txt"
        rbt = urllib.robotparser.RobotFileParser()
        rbt.set_url(url);
        rbt.read();
        print(rbt)
        userAgent = "Baiduspider"
        url = "http://localhost:8080/oa/oa.jsp"
        if rbt.can_fetch(userAgent, url):
            resp = requests.get(url)
            data = resp.content;
            fb = open("oa.html","wb")
            fb.write(data)
            fb.close()

        return