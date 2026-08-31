class Twitter:

    def __init__(self):
        #user, followers (who am i following). 
        #set for O(1) access time
        self.following = {}
        self.tweets = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        #post tweet from userid with tweet id
        self.time -= 1

        if userId not in self.tweets: self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #10 most recent tweet IDs. recency
        #either user himself or following
        feed = []
        if userId in self.tweets: #do they have tweets
            for tweet in self.tweets[userId]:
                feed.append(tweet)
        if userId in self.following: #do they have followers
            for follower in self.following[userId]:
                for tweet in self.tweets[follower]:
                    feed.append(tweet)

        heapq.heapify(feed)
        feed = heapq.nsmallest(10, feed)
        res = []
        for num in feed:
            res.append(num[1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        #not following anyone yet
        if followerId not in self.following: self.following[followerId] = set()

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following: return #not following anyone
        if followeeId not in self.following[followerId]: return #not following this person

        self.following[followerId].remove(followeeId)
        
