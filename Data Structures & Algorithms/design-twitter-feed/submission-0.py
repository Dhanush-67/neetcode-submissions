class Twitter:

    def __init__(self):
        self.follower_map = {}
        self.tweet_stack = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_stack.append([userId,tweetId])
        self.follower_map.setdefault(userId,set()).add(userId)

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        count = 0
        for tweet_index in range(len(self.tweet_stack)-1,-1,-1):
            if count >= 10:
                break
            if userId in self.follower_map and self.tweet_stack[tweet_index][0] in self.follower_map[userId]:
                feed.append(self.tweet_stack[tweet_index][1])
                count += 1
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map.setdefault(followerId,set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_map and followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)