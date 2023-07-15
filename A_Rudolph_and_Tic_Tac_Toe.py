# t = int(input())

# for _ in range(t):
#     breaked = False
#     tic_tac = []
#     symbols = set(["X", "+", "O"])
#     for i in range(3):
#         s = input()
#         if s[0] in symbols and s[0] == s[1] == s[2]:
#             print(s[0])
#             breaked = True
#             break
    

#         tic_tac.append(s)
#     if breaked:
#         continue
#     if tic_tac[0][0] in symbols and tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2]:
#         print(tic_tac[0][0])
#         continue
#     if tic_tac[0][2] in symbols and tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0]:
#         print(tic_tac[1][1])
#         continue
#     for i in range(3):
#         if tic_tac[0][i] in symbols and tic_tac[0][i] == tic_tac[1][i] == tic_tac[2][i]:
#             print(tic_tac[0][i])
#             breaked = True
#             break
#     if not breaked:
#         print("DRAW")

# # Loop through each test case
for _ in range(int(input())):
    # Read in the game board
    board = [input() for l in range(3)]
    # Check for horizontal wins
    for row in board:
        if row == "XXX":
            print("X")
            break
        elif row == "OOO":
            print("O")
            break
        elif row == "+++":
            print("+")
            break
    else:
        # Check for vertical wins
        for col in range(3):
            if board[0][col] != "." and board[0][col] == board[1][col] == board[2][col]:
                print(board[0][col])
                break
        else:
            # Check for diagonal wins
            if board[0][0] != "." and board[0][0] == board[1][1] == board[2][2]:
                print(board[0][0])
            elif board[0][2] != "." and board[0][2] == board[1][1] == board[2][0]:
                print(board[0][2])
            else:
                # Check for draw
                print("DRAW")
                
