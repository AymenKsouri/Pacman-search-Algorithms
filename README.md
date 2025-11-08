# 👾 Pac-Man Search Algorithms Project

This project is part of the **Foundations of Artificial Intelligence (IA)** 

The goal is to make Pac-Man find paths efficiently through different mazes using algorithms such as **Depth-First Search**, **Breadth-First Search**, **Uniform-Cost Search**, and **A\***.

---

## 🧠 Implemented Algorithms

- 🔍 **Depth-First Search (DFS)**
- 🌐 **Breadth-First Search (BFS)**
- 💰 **Uniform-Cost Search (UCS)**
- ⭐ **A\*** (A-Star Search with Manhattan Heuristic)

Each algorithm must return a list of legal Pac-Man moves that reach the goal without passing through walls.

---

## 🗂️ Project Structure

Pacman-Search-Algorithms/
│
├── search.py             # Your implementations of DFS, BFS, UCS, A*
├── searchAgents.py       # Search agents that use the algorithms
├── pacman.py             # Main Pac-Man game file
├── game.py               # Core game logic
├── ghostAgents.py        # Ghost AI definitions
├── util.py               # Stack, Queue, and PriorityQueue classes
├── layouts/              # Maze layout files (.lay)
├── test_cases/           # Automated test cases
├── autograder.py         # Automatic testing script
└── README.md             # Project documentation

---

## 🚀 How to Run the Project

This project was designed for **Python 2.6 or 2.7**.  
Make sure your terminal or environment is set to use Python 2 before running.

### 1️⃣ Run Pac-Man manually
python pacman.py

### 2️⃣ Test a simple agent
python pacman.py --layout testMaze --pacman GoWestAgent

### 3️⃣ Run with your search algorithms

Depth-First Search:
python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch

Breadth-First Search:
python pacman.py -l mediumMaze -p SearchAgent -a fn=breadthFirstSearch

Uniform-Cost Search:
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=uniformCostSearch

A* Search:
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

---

## 🧪 Automatic Testing

Run the provided autograder to check your implementation:
python autograder.py

It will test correctness, path cost, and algorithm efficiency.

---

## ⚙️ Requirements

This project was developed for **Python 2.6 or 2.7**.  
No additional external libraries are required — it runs with the **standard Python library** only.  
You do not need pygame, torch, or any modern AI frameworks.

---

## 📚 Educational Context

- **Course:** Fondements en Intelligence Artificielle (IA)  
- **Institution:** Institut Supérieur des Technologies de l’Information et de la Communication (ISTIC)  
- **University:** Université de Carthage, Tunisia  
- **Instructors:** Khaled Belghith, Manel Mrabet, Akram Khemiri  
- **Base Project:** UC Berkeley CS188 – *Introduction to Artificial Intelligence*  
  - Course: https://inst.eecs.berkeley.edu/~cs188/sp21/  
  - Projects: https://inst.eecs.berkeley.edu/~cs188/sp19/projects.html  

---

## 👤 Author

**Aymen Ksouri**  
🎓 3nd-Year Computer Science Student  
📍 ISTIC, Université de Carthage  
🌐 https://github.com/AymenKsouri

---

⭐ *If you found this project educational, consider giving it a star on GitHub!*

