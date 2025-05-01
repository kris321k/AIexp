
import math




def FindMinDistance(distance, visited) :


    min = math.inf

    minNode = None

    for key in distance.keys() :


        if distance[key] < min and key not in visited :


            min = distance[key]

            minNode = key

    



    

    return minNode




def djikstra(graph, edgeCost, Start) :


    visited = set()



    parent = {Start : None}








    distance = {keys : math.inf for keys in graph.keys() if keys != Start}

    distance[Start] = 0


    






    for i in range(10) :


        node = FindMinDistance(distance, visited)

        




        if node == None :

            break


        node2 = node



        visited.add(node)


        
        for neigbour in graph[node]:


            if distance[node] + edgeCost.get((node, neigbour)) < distance[neigbour] :


                parent[neigbour] = node



                distance[neigbour] = distance[node] + edgeCost.get((node, neigbour))


                print(distance)


        

        #printing the path

    
    for CurrentNode in graph.keys() :

        path = []

        if CurrentNode == Start :

            continue


        while CurrentNode is not None :

            path.append(CurrentNode)

            CurrentNode = parent[CurrentNode]

        
        path.reverse()

        print("->".join(path))



def main() :

    graph = {}

    edgeCost = {}





    edges = int(input("enter the number of edges: \n"))

    for _ in range(edges) :


        src = input("enter the src: \n")

        dest = input("enter the dest: \n")

        cost = int(input("enter the edge Cost : \n"))




        if src not in graph.keys() :

            graph[src] = []

        

        if dest not in graph.keys() :

            graph[dest] = []

        

        graph[src].append(dest)

        graph[dest].append(src)

        edgeCost[(src, dest)] = cost

        edgeCost[(dest, src)] = cost

    
    start = input("enter the start node:\n")


    
    djikstra(graph, edgeCost, start)


if __name__ == "__main__" :

    main()


