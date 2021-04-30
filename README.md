# Maze Runner
Created by Conner Mostert

Maze Runner

Using the turtle library, I constructed a maze. the first turtle draws the maze and the locations of the walls are saved 
in a list. The second turtle is used to traverse through the maze. The concept idea behind this program is to check the 
efficiency of search algorithms. There are 5 algorithms to choose from or you can traverse through the maze yourself by 
selecting user and using the arrow keys. My fastest time was 15 seconds. 

Random: Bogosearch selects its path at random and tries to reach the end of the maze. It has no intelligence on top of it
, it just runs trough randomly. Fastest time was 17 minutes and the slowest was 158 minutes.

DFS: checks for available paths (Front, right, left) if front is available it will travel there first. If front is not available
it will check the sides. If no paths exist at the current location the turtle will return to the previous location and search for 
a new path. This process is repeated until a new path is discovered.

BFS: checks the sides first for available paths (Right, left, front) travels right or left first but if they are not available 
it will travel forward. If no paths exist at the current location the turtle will return to the previous location and search for 
a new path. This process is repeated until a new path is discovered.

Complete search: Checks all available paths at the location and then travels down 1 path and saves the other path in a list.
If the path taken is a dead end the turtle returns to the location of the path not taken and travels down it. This method saves 
time since the turtle doesn't need to backtrack to find a new path it knows where available paths are.

User: The user can use the arrows to traverse the maze and reach the destination.

Dijkstra search: (I cant pronounce it) This algorithm searches every path that is available at a location. If multiple paths exist
the algorithm will do a calculation to determine the best path to take. The calculation uses Pythagoras to calculate the distance 
from the new path to destination and travels down that path. The path closest to the destination is not necessarily the correct path
and can be blocked. Dijkstra search can only calculate the shortest path but not if the path is correct. Still this is the most 
efficient algorithm in the code.

Challenge search: This algorithm is similar to User except the walls and background are the same color so the user
can’t see where the walls are located. This is to simulate a search algorithm that can’t see where the walls are located
and has to calculate the path without knowing the path.
