import re
import requests

def test_regex():
    res = requests.get("https://www.csdn.net")
    info = res.content.decode("utf-8")
    #print(info)
    result = re.findall("<img src=\"(.*?)\"", info)
    for item in result:
        print(item)



if __name__ == "__main__":
    test_regex()