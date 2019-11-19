'''Flood plain maps are used to determine what zones in a map are likely to flood during a hurricane.
One factor that helps determine the higher-risk areas is the elevation of the land relative to the land surrounding it.

A land area is modeled as an n x m grid, where each cell represents a portion of land and has an elevation. Elevations are represented by integers. 
Two cells are considered neighbors of each other if they are connected by any of the 8 possible directions (up, down, right, left, or any of the 4 diagonals).

Your task is to find all the high points in the flood plain map. A high point is defined as a cell c where all neighboring cells have an elevation 
that is strictly less than the elevation of cell c. 

Implement the findHighPoints function such that it returns a 2D array (matrix) of booleans where True indicates that it is a high point, 
and False indicates that it is not.'''

# Input: n x m grid
# cell is high point if elevation is strictly higher than all 8 surrounding
# returns array of booleans == T,F
# if cell is high point, represented by a T
# if cell is not, represented by an F
    
def get_elevations(elevations, rows, cols):
    w, h = cols, rows
    flood_map = [[False for x in range(w)] for y in range(h)] 
    
    for i in range(rows):
        for j in range(cols):
            upper = lower = left = right = diagonalRightUp = diagonalRightDown = diagonalLeftUp = diagonalLeftDown = 0
            curr = elevations[i][j]
            
            # if there exists a neighboring cell in a given direction, save its elevation
            if (i-1 >= 0):               
                upper = elevations[i-1][j] 
            if (j-1 >= 0 and i-1 >= 0):
                diagonalLeftUp = elevations[i-1][j-1]
            if (j+1 < cols and i-1 >= 0):
                diagonalRightUp = elevations[i-1][j+1]
                
            if (i+1 < rows):
                lower = elevations[i+1][j]  
            if (j-1 >= 0 and i+1 < rows):
                diagonalLeftDown = elevations[i+1][j-1]
            if (j+1 < cols and i+1 < rows):
                diagonalRightDown = elevations[i+1][j+1]
                
            if (j-1 >= 0):
                left = elevations[i][j-1] 
                
            if (j+1 < cols):
                right = elevations[i][j+1] 
                
            # if the current cell has strinctly higher elevation than all of its neighbors, it is a high point      
            if (curr > upper and curr > lower and curr > right and curr > left and curr > diagonalRightUp and curr > diagonalRightDown and curr > diagonalLeftUp and curr > diagonalLeftDown):
                flood_map[i][j] = True
            else:
                flood_map[i][j] = False
            
    return flood_map

def findHighPoints(elevations):

    # len(elevations) == rows
    # len(elevations[0]) == cols
    rows = len(elevations)
    cols = len(elevations[0])

    return get_elevations(elevations, rows, cols)

def main():
    print("The elevation map for this plot of land is", findHighPoints([[5, 0, 0, 1],
                                                                        [0, 3, 4, 0],
                                                                        [2, 0, 0, 0]]))
    
# Expected Output:
# [[True, False, False, False],
#  [False, False, True, False],
#  [False, False, False, False]]
    
if __name__ == "__main__":
    main()
