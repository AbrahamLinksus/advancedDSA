# viewership trend using arrays 

#KEY TAKEAWAYS: ARRAY MANIPULATION 

class viewershipTrend:
    def __init__(self, arr):
        self.array = arr

    def analyseArray(self):
        totalViews = 0
        maxViews = float('-inf')
        streakCount, prevView = 0, 0
        prevCount = 0
        for viewsPerDay in self.array:
            if maxViews == float('-inf'):
                prevView = viewsPerDay
            else:
                if viewsPerDay >= prevView:
                    streakCount += 1
                    print(prevView, viewsPerDay, "in")
                else:
                    prevCount = streakCount
                    streakCount = 1
                    print(prevView, viewsPerDay, streakCount, "out")
                prevView = viewsPerDay
            
            totalViews += viewsPerDay
            maxViews = max(maxViews, viewsPerDay)
            
            print(prevCount, streakCount)
        print("Total Views: ", totalViews)
        temp = totalViews/len(self.array)
        print(f"Average Views: {temp:.2f}")
        print("Peak Viewing Day:", maxViews)
        print("Longest Rising Streak:", streakCount)
        return
    
findTrend = viewershipTrend([10, 20, 15, 18, 25, 30, 12, 14])
findTrend.analyseArray()