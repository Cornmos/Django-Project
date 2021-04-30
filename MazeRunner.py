""" This program uses turtle to draw a maze. User input determines the algorithm that will be used to traverse the maze.
This program shows how different search algorithms will operate and which will be more efficient.
"""

import turtle
from time import *
import random
import math
import sys
sys.setrecursionlimit(12000)
print(sys.getrecursionlimit())

maze_window = turtle.Screen()
maze_window.bgcolor("white")
maze_window.title("Maze Runner")
maze_turtle = turtle.Pen()
maze_turtle.speed(4)
maze_turtle.hideturtle()
user_turtle = turtle.Pen()
maze_list = [[-4, -4, 1], [4, -4, 0], [4, 1, 0], [3, 2, 1], [4, 2, 0], [4, 4, 0], [4, 4, 0], [-4, 4, 0], [-4, -4, 0],
             [-1, 4, 1], [-1, 3, 0], [-3, 3, 0], [-3, 1, 0], [-3, -1, 1], [-4, -1, 0], [-4, -3, 0], [-2, -3, 0],
             [0, -4, 1],
             [0, -3, 0], [1, -3, 0], [1, -3, 0], [4, -1, 1], [3, -1, 0], [3, 0, 0], [3, -1, 0], [3, -1, 0], [1, -1, 0],
             [1, 0, 0],
             [2, 0, 0], [1, 0, 0], [1, 2, 0], [0, 4, 1], [0, 3, 0], [3, 3, 0], [2, 3, 0], [2, 1, 0], [3, 1, 0],
             [0, 3, 1],
             [0, 2, 0], [-1, 2, 0], [-1, 1, 0], [-1, 2, 0], [-2, 2, 0], [-2, 0, 0], [-3, 0, 0], [-2, 0, 0], [-2, -2, 0],
             [-3, -2, 0], [-1, -2, 0], [0, -2, 0], [-1, -2, 0], [-1, -3, 0], [-1, -1, 0], [0, -2, 1], [0, 1, 0],
             [0, 0, 0],
             [-1, 0, 0], [0, -2, 1], [2, -2, 0], [2, -3, 0], [3, -3, 0], [3, -2, 0]]  # Create maze
newpath, wall_list, current_path = [], [], []
turtle.listen()  # For keyboard strokes


def maze_plan(x, y, z):  # Setup maze from Maze_build method and
    tcurrent = tpos(maze_turtle.position())
    if z == 1:
        maze_turtle.up()
        maze_turtle.goto(x * 60, y * 60)
    if z == 0:
        maze_turtle.down()
        maze_turtle.goto(x * 60, y * 60)
        tafter = tpos(maze_turtle.position())
        wall(tcurrent, tafter)


def maze_build(maze_list):  # Builds maze from maze_list
    for i in maze_list[0:-1]:
        maze_plan(i[0], i[1], i[2])


def wall(t_start, t_end):  # List wall collisions method called in Maze_path
    if t_start[0] - t_end[0] != 0:  # Check if traveled horizontal or vertical z=0 horizontal z=1 vertical
        z = 0
    else:
        z = 1
    x = min(t_start[z], t_end[z])  # Calculate area traveled
    a = int(abs(t_start[z] - t_end[z]) / 30) + 1  # Calculate how many times it needs to be appended
    for i in range(a):
        if z == 0:
            wall_list.append((x + (i * 30), t_start[1]))
        else:
            wall_list.append((t_start[0], x + (i * 30)))
    return wall_list  # Returns Wall collision list


def dbl(wall_list):  # Removes double figures from list
    slim_wall_list = []  # len(list went from 231 to 161
    for i in wall_list:
        if i not in slim_wall_list:
            slim_wall_list.append(i)
    return slim_wall_list


def split_list(slim_wall_list):  # Split collision list into 4 part (-x,-y)(-x,y)(x,-y)(x,y)
    arrbl, arrtl, arrbr, arrtr, arrfull = [], [], [], [], []  # Reduces search time for collision
    for i in range(len(slim_wall_list)):
        if slim_wall_list[i][0] >= 0 and slim_wall_list[i][1] >= 0:
            arrtr.append(slim_wall_list[i])
        if slim_wall_list[i][0] >= 0 > slim_wall_list[i][1]:
            arrbr.append(slim_wall_list[i])
        if slim_wall_list[i][0] < 0 <= slim_wall_list[i][1]:
            arrtl.append(slim_wall_list[i])
        if slim_wall_list[i][0] < 0 and slim_wall_list[i][1] < 0:
            arrbl.append(slim_wall_list[i])
    arrfull = [arrtr] + [arrbr] + [arrtl] + [arrbl]
    return arrfull  # Return new sorted list .position() searches based on its coordinates


def tpos(x):  # Rounds numbers. Once turtle started moving user_turtle.position was out by a factor of e^-15
    # This made matching user_turtle.position to a list of position difficult even if the numbers differ slightly
    rnd = (round(x[0]), round(x[1]))
    return rnd


def start_position():  # Prevents turtle from resetting if wall is hit on the first command
    location_list = [(-30, 210)]
    return location_list


def check_choice():  # Check if choice is valid input
    global choice
    choice = input("Choose algorithm 1,2,3,4,5,6,7 1)Random 2) DFS 3)BFS 4)Complete search 5)User 6)Dijkstra search 7)Challenge")
    if choice.isdigit() == True:
        while int(choice) not in range(1, 8):
            print("I didn't understand try again")
            return check_choice()
    else:
        print("I didn't understand try again")
        return check_choice()


check_choice()  # Choose an algorithm
maze_build(maze_list)
arrfull = split_list(dbl(wall_list))
user_turtle.setheading(270)
location_list = start_position()  # Setup function


def setup(choice):  # Setup based on choice selected,
    user_turtle.up()
    user_turtle.goto(-30, 210)
    user_turtle.down()
    if choice == '1':  # Random
        user_turtle.color("purple")
        user_turtle.speed(4)
    if choice == '2':  # Depth first search
        user_turtle.speed(1)
        user_turtle.color("yellow")
    if choice == '3':  # BFS
        user_turtle.speed(1)
        user_turtle.color("orange")
    if choice == '4':  # Complete search
        user_turtle.color("blue")
        user_turtle.speed(1)
    if choice == '5':  # User
        user_turtle.speed(0)
        user_turtle.color("green")
    if choice == '6':  # Dijkstra search
        user_turtle.speed(1)
        user_turtle.color("red")
    if choice == '7':  # Challenge
        maze_window.bgcolor("black")
        user_turtle.speed(0)
        user_turtle.color("white")


def algorithm(choice):  # Choose algorithm to search maze with
    if tpos(user_turtle.position()) != (270.00, 90.00):
        if choice == '1':  # Random
            x = str(random.randint(1, 4) * 2)
            command(x)
        if choice == '2':  # Depth first search
            dfs_algorithm(1)
        if choice == '3':  # BFS
            bfs_algorithm(1)
        if choice == '4':  # BFS algorithm
            search(tpos(user_turtle.position()), dbl(wall_list), location_list)
        if choice == '5':  # User traversal
            user()
        if choice == '6':  # Dijkstra search
            search(tpos(user_turtle.position()), dbl(wall_list), location_list)
        if choice == '7':  # Challenge
            user()
    else:
        finish()


def command(x):  # Set direction based on command. Method called in algorithm()
    if x == '2':
        user_turtle.setheading(270)
    if x == '4':
        user_turtle.setheading(180)
    if x == '6':
        user_turtle.setheading(0)
    if x == '8':
        user_turtle.setheading(90)
    if x == '2' or x == '4' or x == '6' or x == '8':
        user_turtle.forward(30)
        user_turtle.goto(check(tpos(user_turtle.position()), location_list, arrfull))
        location_list.append(tpos(user_turtle.position()))
    algorithm(choice)


def check(x, location_list, arrfull):  # Collision check against 4 different lists
    if x[0] >= 0 and x[1] >= 0:
        if x in arrfull[0]:
            return location_list[-1]
    if x[0] >= 0 > x[1]:
        if x in arrfull[1]:
            return location_list[-1]
    if x[0] < 0 <= x[1]:
        if x in arrfull[2]:
            return location_list[-1]
    if x[0] < 0 and x[1] < 0:
        if x in arrfull[3]:
            return location_list[-1]
    return x


def set_heading(position,location_list):  # Points the turtle in the direction it is moving
    horizontal= position[0]-location_list[-1][0]
    vertical=position[1]-location_list[-1][1]
    if horizontal == 30:
        user_turtle.setheading(0)
    if horizontal == -30:
        user_turtle.setheading(180)
    if vertical == 30:
        user_turtle.setheading(90)
    if vertical == -30:
        user_turtle.setheading(270)
    return


def dfs_algorithm(counter):  # Depth first search directions
    t_spot = tpos(user_turtle.position())
    if t_spot != (270.00, 90.00):
        if user_turtle.heading() == 0: # East
            front = (t_spot[0]+30,t_spot[1])
            right = (t_spot[0],t_spot[1]-30)
            left = (t_spot[0],t_spot[1]+30)
        if user_turtle.heading() == 90:  # North
            front = (t_spot[0],t_spot[1]+30)
            right = (t_spot[0]+30,t_spot[1])
            left = (t_spot[0]-30,t_spot[1])
        if user_turtle.heading() == 180:  # West
            front = (t_spot[0]-30,t_spot[1])
            right = (t_spot[0],t_spot[1]+30)
            left = (t_spot[0],t_spot[1]-30)
        if user_turtle.heading() == 270:  # South
            front = (t_spot[0],t_spot[1]-30)
            right = (t_spot[0]+30,t_spot[1])
            left = (t_spot[0]-30,t_spot[1])
        return dfs_goto(front,right,left,counter)
    else:
        finish()


def dfs_goto(front,right,left,counter):  # DFS Algorithms (Front,Right,Left)
    user_turtle.down()
    arrfull = dbl(wall_list)
    if front not in arrfull and front not in location_list:
        user_turtle.goto(front[0],front[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return dfs_algorithm(counter)
    if right not in arrfull and right not in location_list:
        user_turtle.goto(right[0],right[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return dfs_algorithm(counter)
    if left not in arrfull and left not in location_list:
        user_turtle.goto(left[0],left[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return dfs_algorithm(counter)
    else:
        user_turtle.up()
        counter = counter + 1
        user_turtle.goto(location_list[-counter][0],location_list[-counter][1])
        return dfs_algorithm(counter)


def bfs_algorithm(counter):  # Set direction for Breath first search
    t_spot = tpos(user_turtle.position())
    if t_spot != (270.00, 90.00):
        if user_turtle.heading() == 0: # East
            front = (t_spot[0]+30,t_spot[1])
            right = (t_spot[0],t_spot[1]-30)
            left = (t_spot[0],t_spot[1]+30)
            back = (t_spot[0]-30,t_spot[1])
        if user_turtle.heading() == 90:  # North
            front = (t_spot[0],t_spot[1]+30)
            right = (t_spot[0]+30,t_spot[1])
            left = (t_spot[0]-30,t_spot[1])
            back = (t_spot[0],t_spot[1]-30)
        if user_turtle.heading() == 180:  # West
            front = (t_spot[0]-30,t_spot[1])
            right = (t_spot[0],t_spot[1]+30)
            left = (t_spot[0],t_spot[1]-30)
            back = (t_spot[0]+30,t_spot[1])
        if user_turtle.heading() == 270:  # South
            front = (t_spot[0],t_spot[1]-30)
            right = (t_spot[0]+30,t_spot[1])
            left = (t_spot[0]-30,t_spot[1])
            back = (t_spot[0],t_spot[1]+30)
        return bfs_goto(front,right,left,back,counter)
    else:
        finish()


def bfs_goto(front,right,left,back,counter):  # bFS Algorithms (Right,Left,Back,Front)
    user_turtle.down()
    arrfull = dbl(wall_list)
    if right not in arrfull and right not in location_list:
        user_turtle.goto(right[0],right[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return bfs_algorithm(counter)
    if left not in arrfull and left not in location_list:
        user_turtle.goto(left[0],left[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return bfs_algorithm(counter)
    if back not in arrfull and back not in location_list:
        user_turtle.goto(back[0],back[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return bfs_algorithm(counter)
    if front not in arrfull and front not in location_list:
        user_turtle.goto(front[0],front[1])
        set_heading(tpos(user_turtle.position()), location_list)
        location_list.append(tpos(user_turtle.position()))
        counter = 1
        return bfs_algorithm(counter)
    else:
        user_turtle.up()
        counter = counter + 1
        user_turtle.goto(location_list[-counter][0],location_list[-counter][1])
        return bfs_algorithm(counter)

# Complete search algorithm methods
def search(pos, arrfull, location_list):  # complete search algorithm checks if path is possible
    counter = 0
    if (pos[0], pos[1] - 30) not in arrfull and (pos[0], pos[1] - 30) not in location_list:
        current_path.append((pos[0], pos[1] - 30))
        counter += 1
    if (pos[0], pos[1] + 30) not in arrfull and (pos[0], pos[1] + 30) not in location_list:
        current_path.append((pos[0], pos[1] + 30))
        counter += 1
    if (pos[0] + 30, pos[1]) not in arrfull and (pos[0] + 30, pos[1]) not in location_list:
        current_path.append((pos[0] + 30, pos[1]))
        counter += 1
    if (pos[0] - 30, pos[1]) not in arrfull and (pos[0] - 30, pos[1]) not in location_list:
        current_path.append((pos[0] - 30, pos[1]))
        counter += 1
    search_check(current_path, counter)


def search_check(current_path, counter):  # If 2 paths exist save not taken path in list
    if counter > 1:  # More than 1 path exists
        newpath.append(tpos(user_turtle.position()))
    if counter < 1:  # No paths exist from current location go to new path
        user_turtle.up()
        user_turtle.goto(newpath[-1])
        newpath.pop(-1)
        user_turtle.down()
    if choice == '4':
        if counter >= 1:  # Turtle goes to open path and appends position
            user_turtle.goto(current_path[-1])
            location_list.append(tpos(user_turtle.position()))
            current_path.pop(-1)

    if choice == '6':
        if counter > 1:  # Turtle goes to open path and appends position
            path = dijkstra_search(current_path)
            user_turtle.goto(current_path[-path])
            location_list.append(tpos(user_turtle.position()))
            current_path.pop(-path)
        else:
            user_turtle.goto(current_path[-1])
            location_list.append(tpos(user_turtle.position()))
            current_path.pop(-1)
    return algorithm(choice)


# User input Methods
def user():  # Takes input from user to traverse maze
    user_turtle.speed(0.5)
    turtle.onkey(up, 'Up')
    turtle.onkey(right, 'Right')
    turtle.onkey(left, 'Left')
    turtle.onkey(down, "Down")


def up():  # User command up arrow
    if tpos(user_turtle.position()) != (270.00, 90.00):
        command('8')


def left():  # User command left arrow
    if tpos(user_turtle.position()) != (270.00, 90.00):
        command('4')


def right():  # User command right arrow
    if tpos(user_turtle.position()) != (270.00, 90.00):
        command('6')


def down():  # User command down arrow
    if tpos(user_turtle.position()) != (270.00, 90.00):
        command('2')


def dijkstra_search(current_path):  # Calculate the distance from path location to destination using Pythagoras theorem
    path1 = math.sqrt((current_path[-1][0] - 270) ** 2 + (current_path[-1][1] - 90) ** 2)
    path2 = math.sqrt((current_path[-2][0] - 270) ** 2 + (current_path[-2][1] - 90) ** 2)
    if path1 > path2:
        return 2
    else:
        return 1


# Once maze is complete finish method
def finish():
    now = time()
    user_turtle.setheading(270)
    print("finish")
    print("result:", '{0:.2f}'.format(now - timedelta), "seconds")
    print("Maze will stay open to see the routes taken", "\nGoodbye")



setup(choice)
timedelta = time()
algorithm(choice)
turtle.done()

"""Errors:
- Random sort can't finish, a recursion error occurs because the same methods are called to many times without resolution 
so the program thinks its an infinite loop issue. If the commands for random were submitted in the same method as the
execution of the command it will bypass the issue and run till complete. Fastest time to get trough maze was 17 minutes,
slowest time was 158 minutes.
- After the maze is completed the program ends. The program can't be called several times because a recursion error will
appear and stop the program

Notes:
- Maze stays open after completion to analyse the routes taken, but the maze doesn't except commands anymore. Click X 
will close the window without error on the terminal.
- Original maze wall list has 280 elements. After removing doubles it has 163 elements. The list is then split into 4 
parts with an average of 40 elements in the list. Instead of list search 280 elements per turtle movement the search 
time is reduced to approximately 40 elements per turtle movement 7 times less.
- Random search: the turtles move is set at random and can move anywhere. This is proof of concept of a search algorithm
that is very inefficient. Fastest time trough the maze was 17 minutes and the slowest time was 158 minutes. It also 
shows that all walls are impassable.  
- DF search: the algorithm traverses trough the maze by checking the front path first then the sides.
- BF search: The algorithm traverses trough the maze by checking the right then left then front paths.
- Complete search: This algorithm logs all possible paths from the current location. If the algorithm has 2 possible paths
it will choose 1 path and append the other path in a list. If the algorithm has no possible moves it will return to a 
not taken path. This reduces the time to traverse the maze because it knows where the next available path is. Fastest 
time was 17 seconds
- User traversal: The user controls the turtle to reach the end of the maze. The user needs to press an arrow key and 
the turtle will travel to that location. So arrow keys need to be pressed repeatedly to traverse the maze. This 
simulates the search algorithms decision making and traversal of the maze. The search algorithm calculates its next move
 and moves 1 step at a time. The fastest i could traverse the maze was 15 seconds. (Can you do better?) 
- Dijkstra search: This algorithm is an improvement of the Colplete search algorithms. If the turtle has 2 possible paths 
to take it will calculate which path is the shortest by calculating the path's start point distance to the destination 
using pythagoras. The shortest distance start point will be selected and the turtle will travel down that path. The 
calculated path is not always the correct path as seen at the far left side of the maze. Dijkstra search can only 
calculate the shortest path but cant calculate if the path reaches the destination. Fastest time is 10.5 seconds
- Challenge search: This algorithm is similar to User except the walls and background are the same color so the user
cant see where the walls are located. This is to simulate a search algorithm that cant see where the walls are located
and has to calculate the path without knowing the path.
- Comlete search and Dijkstra search moves 4 times slower than all the other algorithms. This is to show how the turtles 
move and its not just a line streak on the screen. This also evens out the difference between User search and the other
algorithms.
Results: Fastest time trough the maze
Random (Bogo-search) = 1050 seconds
Depth first search = 26.6 seconds
Breath first search = 43 seconds
Complete search = 17 seconds
User traversal = 15 seconds
Dijkstra search = 11 seconds
Challenge= 38 seconds
"""