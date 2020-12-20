"""
957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
"""



class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cell_to_idx = defaultdict(int)
        updated_cells = cells.copy()
        for i in range(N):
            updated_cells = self.change_state(updated_cells)
            if tuple(updated_cells) in cell_to_idx:
                break
            cell_to_idx[tuple(updated_cells)] = i + 1
        
        if i == N - 1:
            return updated_cells
        else:
            steps =  i + 1 - cell_to_idx[tuple(updated_cells)]  # repeat every how many steps
            for _ in range(N % steps + steps):
                cells = self.change_state(cells)
            return cells
    
    def change_state(self, cells):
        res =  []
        for i in range(len(cells)):
            if i == 0:
                res.append(0)
            elif i == len(cells) - 1:
                res.append(0)
            else:
                if cells[i-1] == cells[i+1]:
                    res.append(1)
                else:
                    res.append(0)
        return res
