class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        events = []
        for i, (arrival, leaving) in enumerate(times):
            events.append((arrival, 'arrive', i))
            events.append((leaving, 'leave', i))
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        available_chairs = []
        heapq.heapify(available_chairs)
        friend_to_chair = {}
        next_available_chair = 0
    
        for time, event_type, friend in events:
            if event_type == 'arrive':
                if available_chairs:
                    chair = heapq.heappop(available_chairs)
                else:
                    chair = next_available_chair
                    next_available_chair += 1
                friend_to_chair[friend] = chair
                if friend == targetFriend:
                    return chair
        
            else:
                chair = friend_to_chair[friend]
                heapq.heappush(available_chairs, chair)

        

