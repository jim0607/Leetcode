"""
642. Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""



"""
与1268很像，只不过输入input_str是流数据，需要不断更新hotness.
In TrieNode, there should be self.child, self.is_end, self.sentence, self.hotness.
In Trie, there should be a method to insert a sentence into the trie; there should also be 
a method to search for all the possible autocomplete words of a given input string;
这个search mehtod分三步，第一步是遍历找到需要search的input_str在trie中所在的node, 第二步是从这个node出发，
找到其所有能到达的endNode, 显然是backtrack来做，第三步是对所有能达到的endNode.hotness排个序，取前三作为输出。
"""

class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        self.sentence = ""
        self.hotness = 0
        
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, sentence, hotness):       # we should also insert the hotness so that we can use later
        """
        insert the sentence with it's appear time into the trie
        """
        curr = self.root
        for ch in sentence:
            curr = curr.child[ch]
        curr.is_end = True
        curr.sentence = sentence
        curr.hotness = curr.hotness - hotness     # use negative to make sure descending order of hotness, - hotness is to 处理流动输入的input_str, 因为如果输入了很多次"i love u", 那么就需要insert很多次，那么hotness自然就很高
        
    def search(self, input_str):
        res = []
        curr = self.root
        for ch in input_str:
            if ch not in curr.child:
                return res
            curr = curr.child[ch]
            
        self.backtrack(curr, res)

        return [sentence[1] for sentence in sorted(res)[:3]]
    
    def backtrack(self, curr, res):
        if curr.is_end:
            res.append((curr.hotness, curr.sentence))      # append the hotness so that we can sort later
            # return        注意这里不能return 因为收到health之后，如果return了就搜不到healthy了
        
        for next in curr.child.values():     # 注意这里的next node is the value of the dictionary cuz it's a trieNode
            self.backtrack(next, res)
        

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.input_str = ""     # 注意这里必须用全局变量，不然每次query input一个ch的时候input_str都会清空，这样不符合题意，题目要求处理流动的string
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])

    def input(self, ch: str) -> List[str]:
        if ch != "#":
            self.input_str += ch
            return self.trie.search(self.input_str)
        else:
            self.trie.insert(self.input_str, 1)     # if ch=="#", then we have finished typing one sentence, there is no need to search for the auto-complete string. But we need to insert the sentence into trie to update the trie
            self.input_str = ""




"""
Another solution that somehow dones't work, but don't know why
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.sentences = collections.defaultdict(int)

        
class Trie:
    
    def __init__(self, sentences, times):
        self.root = TrieNode()
        for i, sentence in enumerate(sentences):
            self._insert(sentence, times[i])
               
    def _insert(self, sentence, time):
        curr = self.root
        for ch in sentence:
            curr = curr.child[ch]
            curr.sentences[sentence] += time
        
    def search(self, sentence): # Return a list of sentences that start with the sentence
        curr = self.root
        for ch in sentence:
            if ch not in curr.child:
                return collections.defaultdict(int)
            curr = curr.child[ch]
        return curr.sentences
        
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.stc = ""
        self.map = collections.defaultdict(int)
        for i in range(len(sentences)):
            self.map[sentences[i]] = times[i]
            
        self.trie = Trie(sentences, times)

    def input(self, ch: str) -> List[str]:
        if ch.isalpha() or ch == " ":
            self.stc += ch
            res = [(sentence, time) for sentence, time in self.trie.search(self.stc).items()]
            res.sort(key = lambda x: (-x[1], x[0]))
            return [sentence for sentence, _ in res[:3]]
            
        elif ch == "#":
            self.map[self.stc] += 1
            self.trie._insert(self.stc, self.map[self.stc])     
            self.stc = ""
            return []
            

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
