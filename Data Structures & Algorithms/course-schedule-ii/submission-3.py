class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []
        
        for pair in prerequisites:
            course, req = pair[0], pair[1]
            prereqs[course].append(req)

        
        used = set()
        output = []
        visiting = set()

        def dfs(course):
            if course in visiting:
                #we've seen the same course (prereq) twice for our course
                return False

            if course in used:
                #course is already valid in our path
                return True
            
            visiting.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
                #check is too late, next prereq could be linked prior
                if prereq in used: continue 
                
            #why do we need this? dfs is only for the current course
                #ex: Consider 1->2. the set would have 1, 2
                #Then add 0->1. 
                #This would be marked false because 0 is in the set 

            
            #why do we need to mark?
                #Consider 1->2, 0->2, if we don't mark 2, we call 1 and 2
                #for the amnt of times 2 is called. 
            visiting.remove(course)
            prereqs[course] = []

            #nature of dfs: because of all the dfs calls above, the first completed call will add the first prereq
            #Consider 3->2->1, 3->4. 1 will call 2, 2 will call 3, then 3 will be added. Then we skip "3" in 4's call
            #Consider 2, 1->3, 1->2. Then 3 calls 2, 2 calls 1 (gets added). Then 3 tries to call 1 again (?) but we already added it. Waste of a call
            if not course in used:
                used.add(course)
                output.append(course)
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
        