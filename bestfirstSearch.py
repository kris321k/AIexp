import heapq



def BestFirstSearch(graph, start, goal, heu) :

    visited = set()

    queue = []

    queue.append(start)

    path = []

    parent = {start : None}

    

    




    while True :

        print(queue)


        node = queue.pop(0)


        visited.add(node)


        print("\n")




        if node == goal :


            while node is not None :

                path.append(node)

                node = parent[node]

            
            #printing the graph

            path.reverse()




            print("->".join(path))



            return
        




        for neigbour in graph[node] :


            if neigbour not in visited and neigbour not in queue:




                queue.append(neigbour)

                parent[neigbour] = node


                queue = sorted(queue, key = lambda x : heu[x])



    





def main() :


    graph = {}


    nodes = int(input("enter the number of edges\n"))


    for _ in range(nodes) :

        src = input("enter the src\n")

        dest = input("enter the destination\n")

        

        if src not in graph.keys() :

            graph[src] = []

        
        if dest not in graph.keys() :

            graph[dest] = []

        
        graph[src].append(dest)

        graph[dest].append(src)


    
    heuristicValues = {}


    for key in graph.keys() :

        heu = int(input(f"enter the heu for {key}"))

        heuristicValues[key] = heu




    start = input("enter the start node\n")

    goal = input("enter the goal node\n")

    BestFirstSearch(graph,start, goal,heuristicValues)






        


if __name__ == "__main__" :

    main()
