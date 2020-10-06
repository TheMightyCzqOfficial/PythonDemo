from pip._vendor.distlib.compat import raw_input

from band1.no4.dns_cache import DnsCache
from band1.no4.rebots_info import RebotsInfo


if __name__ == '__main1__':
    dns = DnsCache()
    while True:
        info = raw_input("请输入域名：")
        if info == 'x':
            break
        else:
            dns.showIp(info)

if __name__ == '__main__':
    reb = RebotsInfo()
    reb.get_rebots("http://www.mju.edu.cn/rebots.txt")