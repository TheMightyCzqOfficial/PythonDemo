from pip._vendor.distlib.compat import raw_input

from course_prev.no4.dnscache import DnsCache
from course_prev.no4.reboot_spider import RebootInfo

if __name__ == '__main1__':
    while True:
        dns = raw_input("请输入域名：")
        if dns == 'x':
            break
        try:
            dnsCache = DnsCache(dns)
            dnsCache.dns_to_ip()
        except :
            print("异常")

if __name__ == '__main__':
    rebot = RebootInfo('http://localhost:8080/')
    rebot.print_info()