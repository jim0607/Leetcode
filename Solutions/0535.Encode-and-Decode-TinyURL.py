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
Convert long url to short url via hashing. 
Look up long url from short url in hash table.
"""
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.mapping = collections.defaultdict(str)  # short_url --> long_url
        key = str(hash(longUrl))    # hash(str) returns the hash_code for the str
        self.mapping[key] = longUrl
        shortUrl = "http://tinyurl.com/" + key
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mapping[shortUrl.split("/")[-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
