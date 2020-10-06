from pip._vendor.distlib.compat import raw_input

from band2.no4.dns_cache import DnsCache
from band2.no4.rebots_info import RebotsInfo

if __name__ == "__main1__":
    dns = DnsCache()
    while True:
        input = raw_input("请输入要查询的域名：")
        if input == "x":
            break
        else:
            ip = dns.ips(input)
            print(ip)

if __name__ == "__main__":
    rebot = RebotsInfo()
    reb = rebot.getRobots("http://localhost:8080")
    print(reb)
