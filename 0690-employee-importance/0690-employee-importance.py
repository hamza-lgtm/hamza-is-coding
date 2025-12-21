"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for i in range(len(employees)):
            d[employees[i].id] = i

        queue = deque([employees[d[id]]])
        result = 0
        while queue:
            for _ in range(len(queue)):
                employee = queue.popleft()
                result += employee.importance
                print(result)
                if employee.subordinates:
                    for subordinate in employee.subordinates:
                        queue.append(employees[d[subordinate]])
        return result




        