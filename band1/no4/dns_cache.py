import dns.resolver

class DnsCache(object):
    def __init__(self):
        print("init")
        return

    def showIp(self, domain):
        try:
            result = dns.resolver.resolve(domain, "A")
            #print(result)
            for ans in result.response.answer:
                for item in ans.items:
                    print(item)
        except:
            print("发生异常")
        #print(result)
        #print("IP: " + domain)