import random


# Set the board to start_state
def start_state():
  board = [[' ',' ',' '],
          [' ',' ',' '],
          [' ',' ',' ']]
  return board


# pick start player randomly
def pick_player():
  players = ["X","O"]
  if random.random() < 0.5:
    currentplayer = players[0]
  else:
    currentplayer = players[1]
  print(f"Current player is {currentplayer}")
  return currentplayer


# check available spots
def check_empty_spot(board):
  is_empty_spot = []
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] == ' ':
        is_empty_spot.append([r,c])
  return is_empty_spot


# current player play randomly
def random_move():
  global board
  global currentplayer
  global oppositeplayer
  next_move = random.choice(is_empty_spot)
  board[next_move[0]][next_move[1]] = currentplayer
  #currentplayer = "X" if currentplayer == "O" else "X"
  if currentplayer == "X":
    currentplayer = "O"
    oppositeplayer = "X"
  else:
    currentplayer = "X"
    oppositeplayer = "O"
  return



# AI's best move using Minimax algorithm
def best_move():
    global board
    global currentplayer
    global oppositeplayer
    if currentplayer == "X":
      oppositeplayer = "O"
    else:
      oppositeplayer = "X"
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = currentplayer
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = currentplayer
        if currentplayer == "X":
          currentplayer = "O"
        else:
          currentplayer = "X"

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    scores = {
        currentplayer: 1,
        oppositeplayer: -1,
        "drew": 0
    }

    # if game ends, return score"(1,-1,0)
    winner = check_winner(board)
    if winner:
        return scores[winner]

    if is_maximizing:
        max_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = currentplayer
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_score = max(max_score, score)
        return max_score
    else:
        min_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = oppositeplayer
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_score = min(min_score, score)
        return min_score


# check winning condition is made
def check_winner(board):
  # Check rows
  the_winner = None
  for r in range(len(board)):
    if board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][1] != ' ':
      the_winner = board[r][1]
      return the_winner
  # Check columns
  for c in range(len(board[0])):
    if board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[1][c] != ' ':
      the_winner = board[1][c]
      return the_winner
  # Check diagonal
  if board[1][1] == board[0][0] and board[1][1] == board[2][2] and board[1][1] != ' ':
    the_winner = board[1][1]
    return the_winner
  if board[1][1] == board[0][2] and board[1][1] == board[2][0] and board[1][1] != ' ':
    the_winner = board[1][1]
    return the_winner
  # Check drew
  open_spots = sum(row.count(' ') for row in board)
  if the_winner is None and open_spots == 0:
    the_winner = "drew"
    return the_winner
  return the_winner



# game play starts
board = start_state()
currentplayer = pick_player()
is_empty_spot = check_empty_spot(board)

# move and check empty spot until game ends
while len(is_empty_spot) > 0:
  #random_move()
  best_move()
  #update is_empty_spot_number
  is_empty_spot = check_empty_spot(board)
  the_winner = check_winner(board)
  if the_winner:
    break

# when game is end, print the board
print(f"{board[0]}\n{board[1]}\n{board[2]}")
print(f"The winner is {the_winner}")










