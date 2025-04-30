
import math

def FindMinDistance(distance) :


    min = math.inf

    minNode = None

    for key in distance.keys() :


        if distance[key] < min :


            min = distance[key]

            minNode = key

    

    return minNode




def djikstra(graph, edgeCost, Start) :


    visited = set()


    path = []

    parent = {Start : None}


    distance = {}

    distance[Start] = 0


    for keys in graph.keys() :

        if keys != Start :


            distance[keys] = math.inf


    


    while True :


        node = FindMinDistance(distance)

        visited.add(node)


        
        for neigbour in graph[node] :


            if distance[node] + edgeCost.get((node, neigbour)) < distance[neigbour] :


                parent[neigbour] = node


                distance[neigbour] = distance[node] + edgeCost.get((node, neigbour))

        

        #printing the path


        while node is not None :

            path.append(node)

            node = parent[node]

        
        path.reverse()


        print("->".join(path))




def main() :

    graph = []

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




if __name__ == "__main__" :

    main()


