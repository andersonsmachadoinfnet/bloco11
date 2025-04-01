from dnsrecon.lib.dnshelper import DnsHelper
from netaddr import IPAddress
from re import match


class Test_Lib_dnshelper:
    def test_get_a(self):
        helper = DnsHelper("example.com")
        registros_a = helper.get_a("ipv4.google.com")
        if registros_a:
            for registro in registros_a:
                print(f"A: {registro}")

    def test_get_mx(self):
        helper = DnsHelper("example.com")
        registros_mx = helper.get_mx()
        if registros_mx:
            for registro in registros_mx:
                print(f"MX: {registro}")

    def test_get_ns(self):
        helper = DnsHelper("example.com")
        registros_ns = helper.get_ns()
        if registros_ns:
            for registro in registros_ns:
                print(f"NS: {registro}")

dns=Test_Lib_dnshelper()
dns.test_get_a()
dns.test_get_mx()
dns.test_get_ns()