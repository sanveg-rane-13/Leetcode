class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x : (-x[0], x[1]))
        sol = []
        
        for person in people:
            sol.insert(person[1], person)
            
        return sol
    
    
    
    
    
    

    
#people: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
#step 1: sorting by descending order of heights
#    [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
#    
#step 2: solution: []
#    - inserting at pos 0: [[7, 0]]
#    - inserting at pos 1: [[7, 0], [6, 1], [7, 1]]
#    - inserting at pos 1: [[7, 0], [6, 1], [7, 1]]
#    - inserting at pos 0: [[5, 0], [7, 0], [6, 1], [7, 1]]
#    - inserting at pos 2: [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
#    - inserting at pos 4: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]