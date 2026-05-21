# Tic-Tac-Toe AI using Minimax and Alpha-Beta Pruning

## Overview

This project is a Python implementation of an AI-powered Tic-Tac-Toe game using the **Minimax Algorithm** and **Alpha-Beta Pruning**.

The AI evaluates possible future game states recursively and selects the optimal move while assuming the opponent also plays optimally.

The project demonstrates classical artificial intelligence search techniques used in turn-based deterministic games.

---

# Features

- Interactive Tic-Tac-Toe gameplay
- Human vs AI mode
- Minimax algorithm implementation
- Alpha-Beta pruning optimization
- Recursive game tree search
- Win and draw detection
- Move validation system
- Board state evaluation

---

# Project Structure

```text
tic-tac-toe_ai/
│
├── main.py        # Game loop and user interaction
├── alpha.py       # Minimax and Alpha-Beta AI logic
└── README.md
```

---

# Algorithms Implemented

## 1. Minimax Algorithm

The Minimax algorithm is a recursive decision-making algorithm commonly used in adversarial games.

### Core Idea

- The AI player attempts to maximize the score.
- The human player attempts to minimize the score.
- The algorithm explores all possible future game states until a terminal state is reached.

### Terminal States

| State      | Score |
| ---------- | ----- |
| AI Wins    | +10   |
| Human Wins | -10   |
| Draw       | 0     |

### Workflow

1. Generate all possible moves.
2. Simulate each move.
3. Recursively evaluate future board states.
4. Assign scores to terminal states.
5. Choose the move with the best possible outcome.

### Characteristics

- Guarantees optimal play
- Explores the full game tree
- Computationally expensive for large search spaces

---

## 2. Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm.

### Purpose

It reduces unnecessary exploration in the game tree while still producing the same optimal result as standard minimax.

### Core Variables

| Variable | Meaning                            |
| -------- | ---------------------------------- |
| Alpha    | Best score maximizer can guarantee |
| Beta     | Best score minimizer can guarantee |

### Pruning Condition

```python
beta <= alpha
```

When this condition becomes true, further exploration of that branch is unnecessary.

### Benefits

- Faster execution
- Reduced search space
- Improved efficiency
- Same optimal decisions as minimax

---

# How the AI Works

The AI follows this process:

```text
Current Board
      ↓
Generate Possible Moves
      ↓
Simulate Future States
      ↓
Evaluate Outcomes using Minimax
      ↓
Prune Unnecessary Branches
      ↓
Choose Best Move
```

---

# Concepts Demonstrated

This project demonstrates:

- Recursive algorithms
- Tree search algorithms
- Adversarial search
- Game AI architecture
- State-space exploration
- Decision-making systems
- Alpha-Beta optimization

---

# Minimax vs Alpha-Beta Pruning

| Feature                   | Minimax | Alpha-Beta Pruning |
| ------------------------- | ------- | ------------------ |
| Optimal Move Selection    | Yes     | Yes                |
| Explores Entire Tree      | Yes     | No                 |
| Faster Execution          | No      | Yes                |
| Time Complexity           | Higher  | Reduced            |
| Efficient for Large Trees | Limited | Improved           |

---

# Running the Project

## Clone the Repository

```bash
git clone https://github.com/your-username/tic-tac-toe_ai.git
```

## Navigate to the Project Directory

```bash
cd tic-tac-toe_ai
```

## Run the Game

```bash
python main.py
```

---

# Example Gameplay

```text
____________
_O_|_X_|___
___|_X_|___
___|_O_|___
Your Turn
Enter row (0-2): 
Enter col (0-2): 0
```

---

# Future Improvements

Possible future enhancements include:

- Graphical User Interface (GUI)
- Difficulty levels
- Monte Carlo Tree Search (MCTS)
- Heuristic evaluation functions
- Multiplayer support
- Larger board dimensions
- Reinforcement learning integration

---

# Technologies Used

- Python
- Recursive algorithms
- Minimax search
- Alpha-Beta pruning

---

# Learning Outcomes

Through this project, the following concepts were explored:

- Minimax decision-making
- Alpha-Beta optimization
- Recursive search techniques
- Board state evaluation
- Artificial intelligence in games
- Tree traversal strategies

---

# Conclusion

This project demonstrates how classical AI search algorithms can be applied to game development. By combining Minimax with Alpha-Beta Pruning, the AI is capable of making efficient and optimal decisions while minimizing unnecessary computation.
