"""
355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""


"""
self.time = 0; self.follows = collections.defaultdict(set) # key is user, val is a set of users that this use follows; 
self.tweets = collections.defaultdict(collections.deque) # key is user, val is a deque of (time, tweetsId). 
题目要求求top 10 recent posted tweetsId, 所以我们需要一个self.time记录时间，然后用heapq来求解top K问题
"""
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.follows = collections.defaultdict(set)     # (id, and the ids he/she follows)
        self.tweets = collections.defaultdict(lambda: collections.deque())  # (id, and tweetsId he/she posts)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.time, tweetId))    
        if len(self.tweets[userId]) > 10:   # pop the least recent post, to save space in a real system
            self.tweets[userId].popleft()   # 这就是为什么用deque的原因
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # we need to find top 10 most recent posts, ie, top 10 smallest self.time
        # top K problem, the first reaction is heapq
        hq = []
        self.follows[userId].add(userId)    
        for user in self.follows[userId]:   # The two for loops are O(Σt_i) - the sum of all tweets posted by user's followers 
            for time, tweet in self.tweets[user]:
                hq.append((-time, tweet))
        
        heapify(hq)

        res = []
        for _ in range(10):     # use a hq, so that the time is O(10logN)
            if len(hq) > 0:
                res.append(heappop(hq)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
