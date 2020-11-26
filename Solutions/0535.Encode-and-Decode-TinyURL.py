"""
535. Encode and Decode TinyURL

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. 
There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""



"""
Convert long url to short url via hashing of the long url use hash function. 
Look up long url from short url in hash table.
"""
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.mapping = defaultdict(str)     # hash_code --> longUrl
        hash_code = hash(longUrl)
        self.mapping[hash_code] = longUrl   # hash(str) returns the hash_code for the str
        shortUrl = "http://tinyurl.com/" + str(hash_code)
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        hash_code = int(shortUrl.split("/")[-1])
        longUrl = self.mapping[hash_code]
        return longUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
