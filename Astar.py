import heapq




def AstarAlgo(graph, heuristic, edgeCost, Start, Goal) :


    visited = set() 


    path = []

    heap = []

    parent = {Start : None}

    CostFromStart = {Start : 0}


    heapq.heappush(heap, (heuristic[Start], Start))




    while heap :


        heu, node = heapq.heappop(heap)


        if node == Goal :

            while node is not None :

                path.append(node)

                node = parent[node]



            


            path.reverse()

            print("->".join(path))


            return


        
        for neigbour in graph[node] :

            tentative_g = CostFromStart[node] + edgeCost.get((node, neigbour))



            if neigbour not in CostFromStart or tentative_g < CostFromStart[neigbour] :

                CostFromStart[neigbour] = tentative_g

                parent[neigbour] = node


                f_score = tentative_g + heuristic[node]


                heapq.heappush(heap, (f_score, neigbour))





def main() :


    graph = {}

    nodes = int(input("enter the number of edges\n"))

    edgeCost = {}

    heuristic = {}


    for _ in range(nodes) :

        src = input("enter the src : \n")

        dest = input("enter the dest :\n")

        cost = int(input("enter the edge cost : \n"))


        if src not in graph.keys() :

            graph[src] = []

        
        if dest not in graph.keys() :

            graph[dest] = []

        
        graph[src].append(dest)

        graph[dest].append(src)


        edgeCost[(src, dest)] = cost

        edgeCost[(dest, src)] = cost


        

    

    for keys in graph.keys() :


        heu = int(input(f"enter the heuritisc for {keys} : \n"))

        heuristic[keys] = heu

    

    start = input("enter the start node :\n")

    goal = input("enter the goal node: \n")


    for key, value in graph.items() :

        print(key)

        print()

        print(value)

    

    print(heuristic)





    AstarAlgo(graph, heuristic, edgeCost, start, goal)




if __name__ == "__main__" :

    main()

