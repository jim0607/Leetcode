"""
393. UTF-8 Validation

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""



"""
这道题考察我们 UTF-8 编码，这种互联网所采用的通用的编码格式的产生是为了解决ASCII只能表示英文字符的局限性，
和统一 Unicode 的实现方式。下面这段摘自维基百科 UTF-8 编码：

对于 UTF-8 编码中的任意字节B，如果B的第一位为0，则B独立的表示一个字符(ASCII 码)；
如果B的第一位为1，第二位为0，则B为一个多字节字符中的一个字节(非 ASCII 字符)；
如果B的前两位为1，第三位为0，则B为两个字节表示的字符中的第一个字节；
如果B的前三位为1，第四位为0，则B为三个字节表示的字符中的第一个字节；
如果B的前四位为1，第五位为0，则B为四个字节表示的字符中的第一个字节；
因此，对 UTF-8 编码中的任意字节，根据第一位，可判断是否为 ASCII 字符；
根据前二位，可判断该字节是否为一个字符编码的第一个字节；
根据前四位（如果前两位均为1），可确定该字节为字符编码的第一个字节，并且可判断对应的字符由几个字节表示；
根据前五位（如果前四位为1），可判断编码是否有错误或数据传输过程中是否有错误。

那么根据上面的描述，我们可以先来判断第一位，如果是0的话，则说明是 ASCII 码，我们直接跳过，
判断方法是只要比二进制数 10000000 小的数第一位肯定是0，
然后我们来处理第一位是1的情况，由于第一位的1只是个标识符，后面连续跟的1的个数才是表示后面的字节的个数，
我们可以统一从第一位开始连续1的个数，然后减去1就是后面的字节的个数，我想的办法是如果该数字大于等于 128，
则表示第一位是1，然后减去 128，如果得到的数大于等于 64，则表示第二位是1，依次类推就可以得到连续的个数 cnt，
我们要注意 10000000 这个数是不合法的，所以当 cnt 为1的时候直接返回 false，还有就是连续1的个数不能超过4个，
当 cnt 大于4时也是不合法的。即便是当 cnt 为 [2, 4] 之间的数，若后面没有跟正确个数的字节，还是非法的，
所以当 cnt > n-i 时还是 false。我们得到了合法的 cnt 的个数，只要验证后面的字节是否是以 10 开头的数即可，
验证方法也很简单，只要这个数在 10000000 ~ 10111111 范围之间，则一定是 10 开头的
"""
"""
C++ version
"""
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int n = data.size();
        for (int i = 0; i < n; ++i) {
            if (data[i] < 0b10000000) {
                continue;
            } else {
                int cnt = 0, val = data[i];
                for (int j = 7; j >= 1; --j) {
                    if (val >= pow(2, j)) ++cnt;
                    else break;
                    val -= pow(2, j);
                }
                if (cnt == 1 || cnt > 4 || cnt > n - i) return false;
                for (int j = i + 1; j < i + cnt; ++j) {
                    if (data[j] > 0b10111111 || data[j] < 0b10000000) return false;
                } 
                i += cnt - 1;
            }
        }
        return true;
    }
};




class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        
        for byte in data:
            if byte >= 128 and byte <= 191:
                if not count:
                    return False
                count -= 1
            else:
                if count:
                    return False
                if byte < 128:
                    continue
                elif byte < 224:
                    count = 1
                elif byte < 240:
                    count = 2
                elif byte < 248:
                    count = 3
                else:
                    return False
                    
        return count == 0
        
        
