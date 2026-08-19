class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a list of prerequisites for each course
        preMap = {}

        for course in range(numCourses):
            preMap[course] = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            preMap[course].append(prerequisite)

        # Keeps track of courses we're currently visiting in DFS
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []: #no prereq
                return True
            
            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq): #check the prereqs to the prereqs
                #if that prereq of prereq is something we already visited, then its false
                    return False

            #mark
            visiting.remove(course) #valid course!
            preMap[course] = [] #valid!
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True