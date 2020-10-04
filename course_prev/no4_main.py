from pip._vendor.distlib.compat import raw_input

from course_prev.no4.dnscache import DnsCache

if __name__ == '__main__':
    while True:
        dns = raw_input("请输入域名：")
        if dns == 'x':
            break
        try:
            dnsCache = DnsCache(dns)
            dnsCache.dns_to_ip()
        except :
            print("异常")
