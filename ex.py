import heapq



def BestFirstSearch(graph, start, goal, heu) :

    visited = set()

    queue = []



    path = []

    parent = {start : None}

    heapq.heappush(queue, (heu[start], start))







    while True :

        print(queue)


        heu_value, node = heapq.heappop(queue)



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


            if neigbour not in visited :




                heapq.heappush(queue, (heu[neigbour], neigbour))


                parent[neigbour] = node


                



    





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
