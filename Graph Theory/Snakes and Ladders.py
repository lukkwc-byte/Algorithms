"""
This is a program that calculates the minimum number of rolls to get 
to square 100. It accepts multiple test cases of board layouts
"""

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ladders = log_translations(n)
        m = int(input())
        snakes = log_translations(m)
        print(str(min_rolls(snakes, ladders)))

"""
Given the number of snakes or ladders (i.e. translations) returns 
a dictionary with  the start points being keys and the end points being
the value
"""
def log_translations(n):
    translations = {}
    for x in range(n):
        start, end = [int(i) for i in input().split()]
        translations[start] = end
    return translations

"""
Uses breadth first search to calculate the number of rolls to
get to 100 then returns that value. The breadth first search finds neighbour nodes 
(i.e. adjacent squares useing the getAdjacent method)
"""
def min_rolls(snakes, ladders):
    q = [1]
    v = set()
    d = [0] * 101
    found = False
    
    while q != [] and found == False:
        c = q.pop(0)
        nextSix = [c + i for i in range(1, 7)]
        adjacent = get_adjacent(nextSix, snakes, ladders)
        for square in adjacent:
            if square == 100:
                return d[c] + 1
            if square not in v:
                v.add(square)
                d[square] = d[c] + 1
                q.append(square)
    
    if found == False:
        return -1
"""
Finds neighbour nodes by checking if the next six squares
are snakes or ladders or if they are greater than 100 (then no move)
"""    
def get_adjacent(nextSix, snakes, ladders):
    adjacent = []
    for square in nextSix:
        if square in snakes:
            adjacent.append(snakes[square])
        elif square in ladders:
            adjacent.append(ladders[square])
        elif square <= 100:
            adjacent.append(square)
    return adjacent

main()