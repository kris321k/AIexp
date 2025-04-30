

import math


def printBoard(board) :

    for rows in board :


        print("|".join(rows))


        


def Isfull(board) :




    for i in range(3) :
        
        for j in range(3) :

            if board[i][j] == " " :

                return False
            

    
    return True


    


def CheckIsWinner(board, player) :



    for Rows in board :

        if all(cell == player for cell in Rows) :

            return True
    


    for cols in range(3) :

        if all(board[rows][cols] == player for rows in range(3)) :

            return True
        
    

    if all(board[i][i] == player for i in range(3)) :

        return True
    

    if all(board[i][2-i] == player for i in range(3)) :

        return True
    


    return False



def minmax(board, depth, isMaximizing) :


    if CheckIsWinner(board, "X") :

        return 1
    

    if CheckIsWinner(board, "O") :

        return -1
    

    if Isfull(board) :

        return 0
    



    if isMaximizing :


        bestScore = -math.inf

        for i in range(3) :

            for j in range(3) :


                if board[i][j] == " " :

                    board[i][j] = "O"

                    score = minmax(board, depth + 1, False)

                    board[i][j] = " "


                    bestScore = max(score, bestScore)


        
        return bestScore
    
    else :

        bestScore = math.inf


        for i in range(3) :

            for j in range(3) :

                if board[i][j] == " " :

                    board[i][j] = "X"

                    score = minmax(board, depth + 1, True)

                    board[i][j] = " "


                    bestScore = min(bestScore, score)


        

        return bestScore
    








def bestMove(board) :


    bestScore = -math.inf

    move = None




    for i in range(3) :

        for j in range(3) :

            if board[i][j] == " " :

                board[i][j] = "O"

                score = minmax(board, 0, False)

                board[i][j] = ""


                                                                        
                if score > bestScore :

                    bestScore = score

                    move = (i, j)

    

    return move



                    
def main() :

    #create a board 3 by 3

    board = [[" " for _ in range(3)] for _ in range(3)]




    while True :


        row = int(input("enter the row no\n"))

        col = int(input("enter the col no\n"))

        board[row][col] = "X"


        printBoard(board)

        print("player made a move\n")


        if CheckIsWinner(board, "X") :

            print("player is the winner\n")

            break


        if Isfull(board) :

            print("the game is tie\n")


            break


        

        move = bestMove(board)


        board[move[0]][move[1]] = "O"


        printBoard(board) 

        print("AI played the move\n")


        

        if CheckIsWinner(board, "O") :

            print("Ai is the winner\n")

            break


        if Isfull(board) :

            print("its a draw\n")

            break





if __name__ == "__main__" : 

    main()