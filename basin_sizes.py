'''A group of farmers has some elevation data, and we are going to help them understand how rainfall flows over their farmland.

We will represent the land as a two-dimensional array of altitudes and use the following model, based on the idea that water flows downhill.

If a cell's four neighboring cells all have higher altitudes, we call this cell a sink; water collects in sinks.
Otherwise, water will flow to the neighboring cell with the lowest altitude. 
If a cell is not a sink, you may assume it has a unique lowest neighbor and that this neighbor will be lower than the cell.

Cells that drain into the same sink - directly or indirectly - are said to be part of the same basin.
Your challenge is to partition the map into basins. In particular, given a map of elevations, your code should partition the map into basins and output the sizes of the basins, in descending order.'''

import sys

# This solution uses a dynamic programming approach; it stores basins in an array, and later retrieves the paths
# to find and return the size of each

# this function stores the water flow path through basins and into sinks
def create_flood_path(flood_map, S):
    
    flood_direction_map = [['C'], ]
    sinks = []
    
    for i in range(1, S**2+1):
        
        path = []
        
        curr = flood_map[i]
        
        # get upper neighbor if not first row
        if (i > S):
            upper = flood_map[i-S]  
        else: 
            upper = sys.maxsize
        
        # get lower neighbor if not last row
        if ((i + S) <= S**2):
            lower = flood_map[i+S]
        else:
            lower = sys.maxsize
        
        # get left neighbor if not first column
        if ((i % S) != 1):
            left = flood_map[i-1]
        else:
            left = sys.maxsize
            
        # get right neighbor if not last column
        if ((i % S) != 0): 
            right = flood_map[i+1]
        else:
            right = sys.maxsize
        
        # find the lowest lying neighboring plot - water will flow in this direction
        lowest_neighbor = min(curr, upper, lower, right, left)
            
        # because neighbors are unique, we can assume there's a unique minimum value - 
        # either the current, left, right, lower or upper plot, so:
        
        # assign codes based on flood direction, ie: water flows to upper neighbor == 'U'         
        if lowest_neighbor == curr:
            path.append('C')
            sinks.append(i)
            
        elif lowest_neighbor == upper:
            path.append('U')
            
        elif lowest_neighbor == right:
            path.append('R')
            
        elif lowest_neighbor == lower:
            path.append('D')
            
        elif lowest_neighbor == left:
            path.append('L')
        
        # store flow codes for flow path finding
        flood_direction_map.append(path)
        
        # format map to access elements via m[i] indexing
        flood_direction_map = [','.join(x) for x in flood_direction_map]
        
    return flood_direction_map, sinks

# recursive function that retraces the steps to get basin sizes
def retrieve_basin_size(flood_map, i, S):

    up = 0 
    right = 0
    down = 0
    left = 0
    
    # if the lower neighbor pointed up, visit it
    if ((i + S) <= S**2) and (flood_map[i+S] == 'U'): 
        down = retrieve_basin_size(flood_map, i+S, S)
    
    # if the upper neighbor pointed down, visit it
    if (i > S) and (flood_map[i-S] == 'D'): 
        up = retrieve_basin_size(flood_map, i-S, S)
    
    # if the left neighbor pointed right, visit it
    if ((i % S) != 1) and (flood_map[i-1] == 'R'): 
        left = retrieve_basin_size(flood_map, i-1, S)
        
    # if the right neighbor pointed left, visit it
    if ((i % S) != 0) and (flood_map[i+1] == 'L'): 
        right = retrieve_basin_size(flood_map, i+1, S)
    
    # size counter
    return (1 + up + down + left + right)

def basin_size_list(flood_map, S):
    
    flood_direction_map, sinks = create_flood_path(flood_map, S)
    
    basin_sizes = []
    
    for i in sinks:
        size = retrieve_basin_size(flood_direction_map, i, S)
        basin_sizes.append(size)
        
    return sorted(basin_sizes, reverse=True)
    
def main():
    
    flood_map = [5, 
                 1, 0, 2, 5, 8, 
                 2, 3, 4, 7, 9, 
                 3, 5, 7, 8, 9, 
                 1, 2, 5, 4, 2, 
                 3, 3, 5, 2, 1]
    
    S = flood_map[0]
    
    print("The size of the land plot is", S, "by", S, ", or", S**2)
    print("The sorted basin sizes are", basin_size_list(flood_map, S))
    
    # Expected Output:
    # [11, 7, 7]
    
if __name__ == "__main__":
    main()
