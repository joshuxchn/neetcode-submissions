class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #1 prereq of 2, add of of 1's prereqs to 2
        reqs = {}
        for i in range(numCourses):
            reqs[i] = set()
        
        for x, y in prerequisites:
            reqs[x].add(y)
            if y in reqs and len(reqs[y]) > 0:
                for r in reqs[y]:
                    reqs[x].add(r)
        #check other way
        for x, y in reversed(prerequisites):
            reqs[x].add(y)
            if y in reqs and len(reqs[y]) > 0:
                for r in reqs[y]:
                    reqs[x].add(r)
        print(reqs)
        result = []
        for course, requirement in queries:
            if requirement in reqs[course]:
                result.append(True)
            else:
                result.append(False)

        return result