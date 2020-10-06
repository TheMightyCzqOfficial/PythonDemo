import dns.resolver

class DnsCache(object):
    def __init__(self):
        # print("init")
        return

    def ips(self, domain):
        # print(domain)
        ip = ""
        try:
            ret = dns.resolver.resolve(domain, "A")
            for answer in ret.response.answer:
                for item in answer.items:
                    # print(item)
                    ip = item
        except:
            print("异常")
        return ip