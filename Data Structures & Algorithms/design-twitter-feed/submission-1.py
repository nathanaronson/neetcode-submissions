class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # user -> users
        self.tweets = defaultdict(list) # user -> (time, tweetId)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees_posts = []

        for followeeId in self.following[userId] | {userId}:
            num_tweets = len(self.tweets[followeeId])
            if num_tweets > 0:
                time, tweetId = self.tweets[followeeId][num_tweets - 1]
                nextIdx = num_tweets - 2
                heapq.heappush_max(followees_posts, (time, tweetId, followeeId, nextIdx))
        
        res = []

        while len(res) < 10 and followees_posts:
            _, tweetId, followeeId, nextIdx = heapq.heappop_max(followees_posts)
            res.append(tweetId)

            if nextIdx >= 0:
                next_time, next_tweetId = self.tweets[followeeId][nextIdx]
                heapq.heappush_max(followees_posts, (next_time, next_tweetId, followeeId, nextIdx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
