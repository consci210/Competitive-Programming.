
class Twitter:

    def __init__(self):
        self.following = {}   # user id : [id which user follows]
        self.tweets = {}      # user id : [list of tweets by user]
        self.time = 0 
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        user_tweets = self.tweets.get(userId, [])
        if not tweetId in user_tweets:
            user_tweets.append([self.time, tweetId])
            self.tweets[userId] = user_tweets
            self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followed_users = self.following.get(userId, [])
        newsFeed = []
        if followed_users :
            for followed in followed_users:
                if followed in self.tweets:
                    newsFeed.extend(self.tweets[followed])
        if userId in self.tweets :
            newsFeed.extend(self.tweets[userId])
        heapq.heapify(newsFeed)
        tweets = []
        while newsFeed and len(tweets) < 10:
            time, tweet = heapq.heappop(newsFeed)
            tweets.append(tweet)   
        return tweets 
    
    def follow(self, followerId: int, followeeId: int) -> None:
        current = self.following[followerId] if followerId in self.following else []
        if not followeeId in current :
            current.append(followeeId)
        self.following[followerId] = current 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId] = [id for id in self.following[followerId] if id != followeeId]
            

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
