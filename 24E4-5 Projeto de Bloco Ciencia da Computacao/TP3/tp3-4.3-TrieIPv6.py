class TrieNode:
    def __init__(self):
        self.children = {}  
        self.is_end_of_prefix = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def ip_to_int(self, ip):
        segments = ip.split(':')
        ip_int = 0
        for segment in segments:
            ip_int = (ip_int << 16) + int(segment, 16)
        return ip_int
    
    def insert(self, prefix):
        ip, prefix_len = prefix.split('/')
        prefix_len = int(prefix_len)
        ip_int = self.ip_to_int(ip)

        node = self.root
        for i in range(prefix_len):
            bit = (ip_int >> (127 - i)) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

        node.is_end_of_prefix = True
    
    def longest_prefix_match(self, ip):
        ip_int = self.ip_to_int(ip)
        node = self.root
        longest_match = None
        
        for i in range(128): 
            bit = (ip_int >> (127 - i)) & 1

            if bit in node.children:
                node = node.children[bit]
                if node.is_end_of_prefix:
                    longest_match = ip_int >> (i + 1) << (i + 1)  
            else:
                break

        if longest_match is not None:
            longest_prefix = self.int_to_ip(longest_match)
            return longest_prefix
        else:
            return None  
    
    def int_to_ip(self, ip_int):
        segments = []
        for i in range(8):
            segments.append(f"{(ip_int >> (112 - 16 * i)) & 0xFFFF:04x}")
        return ":".join(segments)


trie = Trie()
trie.insert("2001:db8::/32")
trie.insert("2001:db8:1234::/48")

ip = "2001:db8:1234:5678::1"
lpm = trie.longest_prefix_match(ip)
print(f"O maior prefixo que corresponde ao IP {ip} é: {lpm}")
