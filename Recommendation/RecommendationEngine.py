
import numpy as np
from collections import defaultdict

class RecommendationEngine(object):

    def __init__(self, videos, profiles):
        self.videos = videos
        self.profiles = profiles

    def get_similarity_index(self, userA, userB):
        rates = np.array(self.profiles[userA]) * np.array(self.profiles[userB])
        valid_indices = np.where(rates != 0)
        similarity_index = np.sum(rates) / len(valid_indices[0])
        return similarity_index
        
    def get_recommendations(self, user):
        similarity_scores = []
        video_to_score_map = defaultdict(float)
        
        for other_user in list(self.profiles.keys()):
            similarity_scores.append(self.get_similarity_index(user, other_user))
            
        not_seen_videos = np.where(np.array(self.profiles[user]) == 0)[0]
        for video in not_seen_videos:
            scores = []
            for other_user, similarity_score in zip(list(self.profiles.keys()), similarity_scores):
                other_user_rate = self.profiles[other_user][video]
                if other_user_rate != 0:
                    scores.append(similarity_score * other_user_rate)
            video_to_score_map[self.videos[video]] = sum(scores) / len(scores)
        sorted_video_to_score_map = {k: v for k, v in sorted(video_to_score_map.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_video_to_score_map.keys())
        
obj = RecommendationEngine(["v0", "v1","v2","v3","v4","v5"], {'userA':[0,1,1,0,0,-1], 'userB':[-1,1,1,1,0,1],'userC':[1,1,1,1,-1,-1]})
val = obj.get_similarity_index("userA", "userA")
print(val)
print(obj.get_recommendations("userA"))
