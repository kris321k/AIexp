import heapq



def Manhattan(Puzzle) :

    distance = 0


    for i in range(3) :

        for j in range(3) :

            if Puzzle[i][j] != 0 :

                Val = Puzzle[i][j]

                Goal_x = (Val - 1) //3


                Goal_y = (Val - 1) % 3

                distance += abs(Goal_x - i) + abs(Goal_y - j)


    
    return distance


def FindIndex(Puzzle) :


    for i in range(3) :

        for j in range(3) :

            if Puzzle[i][j] == 0 :

                return(i, j)
            




moves = [

    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]


def toTupple(Puzzle) :

    return tuple(tuple(row) for row in Puzzle)



def toList(Puzzle) :


    return list(list(row) for row in Puzzle)





def eightPuzzle(Start, Goal) :


    visited = set()


    Start = toTupple(Start)

    parent = {Start : None}


    path = []


    heap = []


    heapq.heappush(heap, (Manhattan(Start), Start))


    while heap :


        Heu, node = heapq.heappop(heap)


        if node == Goal :


            node = toTupple(node) 


            while node is not None :

                path.append(node)

                node = parent[node]

            

            for items in path :

                for rows in items :

                    print(rows)

                
                print()

            


            return

        

        x, y = FindIndex(Start)


        for xi, yi in moves :

            nxi, nyi = x + xi, y + yi


            new_start = [row[:] for row in Start]


            new_start[nxi], new_start[nyi] = new_start[x], new_start[y]


            new_start = toTupple(new_start)


            if new_start not in visited :



                parent[new_start] = node

                heapq.heappush(heap, (Manhattan(new_start), toList(new_start)))




def main() :

    puzzle = []


    goalState = []

    print("enter the state state:\n")

    for i in range(3) :

        row = input(f"enter the row {i} :\n").split(" ")

        row = list(map(int, row))


        puzzle.append(row)

    
    
    print("enter the goal state: \n")

    for i in range(3) :

        row = input(f"enter the row {i} :\n").split(" ")

        row = list(map(int, row))


        goalState.append(row)


    
    eightPuzzle(puzzle, goalState)






if __name__ == "__main__" :

    main()
