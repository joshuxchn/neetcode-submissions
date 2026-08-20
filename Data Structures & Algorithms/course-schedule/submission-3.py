class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []
        
        for pair in prerequisites:
            course, req = pair[0], pair[1]
            prereqs[course].append(req)
        
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            
            visiting.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            #why do we need this? dfs is only for the current course
                #ex: Consider 1->2. the set would have 1, 2
                #Then add 0->1. 
                #This would be marked false because 0 is in the set 

            visiting.remove(course)
            prereqs[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        