class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def ip_to_int(self, ip):
        octets = ip.split('.')
        return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    
    def insert(self, prefix):
        ip, prefix_len = prefix.split('/')
        prefix_len = int(prefix_len)
        ip_int = self.ip_to_int(ip)

        node = self.root
        for i in range(prefix_len):
            bit = (ip_int >> (31 - i)) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

        node.is_end_of_prefix = True
    
    def longest_prefix_match(self, ip):
        ip_int = self.ip_to_int(ip)
        node = self.root
        longest_match = None
        
        for i in range(32): 
            bit = (ip_int >> (31 - i)) & 1

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
        return f"{(ip_int >> 24) & 255}.{(ip_int >> 16) & 255}.{(ip_int >> 8) & 255}.{ip_int & 255}"


trie = Trie()
trie.insert("192.168.0.0/16")
trie.insert("192.168.1.0/24")
trie.insert("10.0.0.0/8")

ip = "192.168.1.100"
lpm = trie.longest_prefix_match(ip)
print(f"O maior prefixo que corresponde ao IP {ip} é: {lpm}")
