import dns.resolver

class DnsCache(object):
    def __init__(self, dnsName):
        self.dnsName = dnsName

    def dns_to_ip(self):
        a = dns.resolver.resolve(self.dnsName, 'A')
        for answer in a.response.answer:
            for item in answer.items:
                print(self.dnsName + "   " + str(item))
        #print(a.response.answer[0].items[0])
