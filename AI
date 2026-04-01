
class Environment:
    def __init__(self,goal_node):
        self.graph={
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        
        self.goal=goal_node
        
    def get_neighbor(self,node):
        return self.graph.get(node, [])
    
    def is_goal(self,node):
        return node==self.goal
    
class Agent:
    def __init__(self,start_node):
        self.queue=[start_node]
        self.visited=[]
        self.current_node=None
        
    def act(self,environment):
        if len(self.queue)==0:
            return "Fail"
        
        self.current_node=self.queue.pop(0)
        
        if environment.is_goal(self.current_node):
            return "Goal Found"

        if self.current_node not in self.visited:
            self.visited.append(self.current_node)
            
        neighbor=environment.get_neighbor(self.current_node)
        
        for i in neighbor:
            if i not in self.visited and i not in self.queue:
                self.queue.append(i)
                
        return "searching"
    
def run_agent(agent,environment,steps):
    for i in range(steps):
        print(f"the step is {i+1}")
        
        action=agent.act(environment)
        
        print(f"agent checked out {agent.current_node}")
        print(f"visited memory {agent.visited}")
        
        if action=="Goal Found":
            print(f"the goal found on node {agent.current_node}") 
            break
        elif action=="Fail":
            print("the agent failed")
            break 
        

e1=Environment(goal_node="F")
a=Agent(start_node="A")
run_agent(agent=a, environment=e1 ,steps=10)       
--------------------------------------------------------------------
class Environment:
    def __init__(self,goal_node):
        self.graph={
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        
        self.goal=goal_node
        
    def get_neighbor(self,node):
        return self.graph.get(node,[])
    
    def is_goal(self,node):
        return node==self.goal
    
class Agent:
        def __init__(self,start_node):
            self.stack=[start_node]
            self.visited=[]
            self.current_node=None
            
        
        def act(self,environment):
            if len(self.stack)==0:
                return "Fail"
            
            self.current_node=self.stack.pop()
            
            if environment.is_goal(self.current_node):
                return "Goal Found"
            
            if self.current_node not in self.visited:
                self.visited.append(self.current_node)
                neighbor=environment.get_neighbor(self.current_node)
                for i in neighbor:
                    if i not in self.visited and i not in self.stack:
                        self.stack.append(i)
                        
            return "searching......"
        
        
def run_agent(agent,environment,steps):
    
    for i in  range(steps):
        print(f"the step is {i+1}")
        print(f"stack is {agent.stack}")
        
        action=agent.act(environment)
        
        print(f"the agent checked {agent.current_node}")
        print(f"the agent visited {agent.visited}")
        
        if action=="Goal Found":
            print(f"the goal found on node {agent.current_node}")
            break
        elif action=="Fail":
            print("goal not found")
            break
        
                      

e1=Environment(goal_node="F")
a1=Agent(start_node="A")
run_agent(agent=a1, environment=e1, steps=10)
--------------------------------------------------------------
import heapq # Ye library VIP line (Priority Queue) banati hai

# 1. Environment Class (Ab Graph Cost ke sath hai)
class Environment:
    def __init__(self, goal_node):
        # Dictionary ke andar Dictionary (Node: {Padosi: Cost})
        self.graph = {
            'A': {'B': 2, 'C': 5},
            'B': {'D': 4, 'E': 1},
            'C': {'F': 6},
            'D': {},
            'E': {'F': 3},
            'F': {}
        }
        self.goal = goal_node

    def get_neighbors(self, node):
        return self.graph.get(node, {})

    def is_goal(self, node):
        return node == self.goal


# 2. Agent Class (UCS wala Dimagh)
class UCSAgent:
    def __init__(self, start_node):
        # Priority Queue mein hum (Total_Cost, Node_Name) rakhte hain
        # Shuru mein cost 0 hai aur node 'A' hai
        self.pq = [(0, start_node)]  
        self.visited = []
        self.current_node = None
        self.current_cost = 0

    def act(self, environment):
        if len(self.pq) == 0:
            return "Fail"

        # heapq.heappop hamesha usko nikalta hai jiski COST sab se KAM ho
        self.current_cost, self.current_node = heapq.heappop(self.pq)

        if environment.is_goal(self.current_node):
            return "Goal Found"

        # Agar node pehle visit nahi hua toh isko check karo
        if self.current_node not in self.visited:
            self.visited.append(self.current_node)
            
            # Padosiyon ko line mein lagao
            neighbors = environment.get_neighbors(self.current_node)
            for neighbor, step_cost in neighbors.items():
                if neighbor not in self.visited:
                    # Naye padosi tak ka total kharcha = Ab tak ka kharcha + Agle step ka kharcha
                    total_cost = self.current_cost + step_cost
                    # Naye node ko VIP line mein daal do
                    heapq.heappush(self.pq, (total_cost, neighbor))
                
        return "searching"


# 3. Main Loop
def run_agent(agent, environment, steps):
    for i in range(steps):
        print(f"\n--- Step {i+1} ---")
        # Line mein dekho kon kon kis cost ke sath khara hai
        print(f"Priority Queue (Cost, Node): {agent.pq}") 
        
        action = agent.act(environment)
        
        print(f"Agent at Node: {agent.current_node} (Total Cost: {agent.current_cost})")
        print(f"Visited Memory: {agent.visited}")
        
        if action == "Goal Found":
            print(f"\n🎉 UCS Agent ne '{agent.current_node}' dhoond liya! Total Cost lagi: {agent.current_cost}")
            break
        elif action == "Fail":
            print("\n❌ Priority Queue khali ho gayi, Goal nahi mila.")
            break

# === Program Run Karein ===
env = Environment(goal_node="F")
ucs_agent = UCSAgent(start_node="A")

run_agent(agent=ucs_agent, environment=env, steps=10)
---------------------------------------------------------------------
import heapq

# === QUESTION 1 SETUP ===
grid = [
    ['S', 1, '#', 2, 3],
    [2, '#', 2, '#', 1],
    [3, 2, 1, 2, 2],
    ['#', 2, '#', 1, 3],
    [2, 1, 2, 2, 'G']
]
rows, cols = 5, 5
start, goal = (0, 0), (4, 4)

def get_neighbors(r, c):
    neighbors = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Right, Down, Left, Up
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            neighbors.append((nr, nc))
    return neighbors

def get_cost(r, c):
    val = grid[r][c]
    return 0 if val in ['S', 'G'] else int(val)

# === ALGORITHMS ===
def bfs():
    print("\n--- BFS ---")
    queue = [(start, [start])]
    visited = []
    while queue:
        curr, path = queue.pop(0)
        if curr not in visited:
            visited.append(curr)
            if curr == goal: return print(f"Path: {path}\nExpanded: {visited}")
            for n in get_neighbors(*curr):
                if n not in visited: queue.append((n, path + [n]))

def dfs():
    print("\n--- DFS ---")
    stack = [(start, [start])]
    visited = []
    while stack:
        curr, path = stack.pop()
        if curr not in visited:
            visited.append(curr)
            if curr == goal: return print(f"Path: {path}\nExpanded: {visited}")
            for n in reversed(get_neighbors(*curr)):
                if n not in visited: stack.append((n, path + [n]))

def ucs():
    print("\n--- UCS ---")
    pq = [(0, start, [start])]
    visited, expanded = set(), []
    while pq:
        cost, curr, path = heapq.heappop(pq)
        if curr in visited: continue
        visited.add(curr); expanded.append(curr)
        if curr == goal: return print(f"Total Cost: {cost}\nPath: {path}\nExpanded: {expanded}")
        for n in get_neighbors(*curr):
            if n not in visited: heapq.heappush(pq, (cost + get_cost(*n), n, path + [n]))

# === RUN YAHAN SE HOGA ===
bfs()
dfs()
ucs()
------------------------------------------------------------------------------------------
class Environment:
    def __init__(self):
        # Image wali exact 5x5 grid
        self.grid = [
            ['A', '0', '0', '#', '#'],
            ['#', 'F', '0', '#', 'P'],
            ['0', '0', '0', 'F', '0'],
            ['0', '#', 'F', '#', '0'],
            ['0', '0', '0', '0', '0']
        ]
        self.rows = 5
        self.cols = 5
        self.start_node = (0, 0)  # Agent (A) ki starting position
        self.goal_node = (1, 4)   # Person (P) ki position

    def get_neighbors(self, node):
        r, c = node
        neighbors = []
        # Agent 4 directions mein ja sakta hai: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check karein ke agent grid ke andar hi rahe
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                # Agent sirf Safe Room '0' ya Person 'P' wale dabbe mein ja sakta hai
                # Fire 'F' aur Wall '#' par jana mana hai
                if self.grid[nr][nc] in ['0', 'P']:
                    neighbors.append((nr, nc))
                    
        return neighbors

    def is_goal(self, node):
        return node == self.goal_node


class DFSAgent:
    def __init__(self, start_node):
        # DFS Stack (LIFO). Isme hum (Current_Node, Path_So_Far) rakhenge
        # Taake aakhir mein exact rasta pata chal sake
        self.stack = [(start_node, [start_node])]
        self.visited = []

    def act(self, environment):
        if len(self.stack) == 0:
            return "Fail", []

        # Stack ke aakhir se node aur uska rasta nikalo
        current_node, current_path = self.stack.pop()

        if environment.is_goal(current_node):
            return "Goal Found", current_path

        if current_node not in self.visited:
            self.visited.append(current_node)

            # Padosi nikal kar stack mein dalo
            neighbors = environment.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    # Naya rasta bana kar stack mein rakh do
                    new_path = current_path + [neighbor]
                    self.stack.append((neighbor, new_path))
                    
        return "searching......", []


def run_agent(agent, environment, steps):
    for i in range(steps):
        action, final_path = agent.act(environment)
        
        if action == "Goal Found":
            print("\n🎉 Mubarak ho! DFS Agent ne Trapped Person (P) ko dhoond liya.")
            print(f"Final Path Taken (Row, Col): {final_path}")
            break
        elif action == "Fail":
            print("\n❌ Agent rasta dhoondne mein nakaam raha.")
            break


# === Program Yahan Se Run Hoga ===
building_env = Environment()
firefighter_agent = DFSAgent(start_node=building_env.start_node)

# Agent ko zyada se zyada 30 steps ka time diya hai rasta dhoondne ke liye
run_agent(agent=firefighter_agent, environment=building_env, steps=30)
---------------------------------------------------------------------------
import heapq

# === QUESTION 2 SETUP ===
grid = [
    ['S', 4, '#', 2, 0],
    [3, '#', 3, '#', 1],
    [2, 2, 2, 2, 1],
    ['#', 3, '#', 1, 2],
    [3, 2, 3, 2, 'G']
]
rows, cols = 5, 5
start, goal = (0, 0), (4, 4)

def get_neighbors(r, c):
    neighbors = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            neighbors.append((nr, nc))
    return neighbors

def get_h(r, c):
    val = grid[r][c]
    if val == 'S': return 4
    if val == 'G': return 0
    return int(val)

# === ALGORITHMS ===
def greedy():
    print("\n--- Greedy Best-First ---")
    pq = [(get_h(*start), start, [start])]
    visited, expanded = set(), []
    while pq:
        h, curr, path = heapq.heappop(pq)
        if curr in visited: continue
        visited.add(curr); expanded.append(curr)
        if curr == goal: return print(f"Path: {path}\nExpanded: {expanded}")
        for n in get_neighbors(*curr):
            if n not in visited: heapq.heappush(pq, (get_h(*n), n, path + [n]))

def a_star():
    print("\n--- A* Search ---")
    pq = [(get_h(*start), 0, start, [start])] # (f, g, current, path)
    visited, expanded = set(), []
    while pq:
        f, g, curr, path = heapq.heappop(pq)
        if curr in visited: continue
        visited.add(curr); expanded.append(curr)
        if curr == goal: return print(f"Total Cost (g): {g}\nPath: {path}\nExpanded: {expanded}")
        for n in get_neighbors(*curr):
            if n not in visited: 
                heapq.heappush(pq, (g + 1 + get_h(*n), g + 1, n, path + [n]))

# === RUN YAHAN SE HOGA ===
greedy()
a_star()
--------------------------------------------------------------------
import random

class Environment:
    def __init__(self):
        self.state=random.choice(["dirty","clean"])
        
    def get_percept(self):
        return self.state

    def execute_action(self,action):
        if action=="suck_dirty":
            self.state="CLEAN"
            print(f"the environment is {self.state}")
        elif action=="do_nothing":
            print(f"the environment is already {self.state}")
        
    def randomize(self):
        self.state=random.choice(["dirty","clean"])
        print(f"the mahol is now randomized {self.state}")
    
        
class ReflexAgent:
    def __init__(self):
        pass
    
    def act(self,percept):
        if percept=="dirty":
            return "suck_dirty"
        elif percept=="clean":
            return "do_nothing"
        
def run_agent(agent,environment,steps):
    for i in range(steps):
        print(f"the current step is {i+1}")
        
        current_percept=environment.get_percept()
        print(f"the current percept is {current_percept}")
        
        action=agent.act(current_percept)
        print(f"the agent will do {action}")
        
        environment.execute_action(action)
        
        if i<steps-1:
            environment.randomize()

room1=Environment()

vacuum_cleaner=ReflexAgent()

run_agent(agent=vacuum_cleaner, environment=room1, steps=3)
---------------------------------------------------------------
# class Environment:
#     def __init__(self):
#         # 3x3 grid banayi hai, jisme index 1 ('b'), 4 ('e'), aur 5 ('f') dirty hain
#         self.grid = ['Clean', 'Dirty', 'Clean',
#                      'Clean', 'Dirty', 'Dirty',
#                      'Clean', 'Clean', 'Clean']

#     def get_percept(self, position):
#         # Agent ko batata hai ke mojooda dabba kaisa hai
#         return self.grid[position]

#     def clean_room(self, position):
#         # Diye gaye dabbe ko saaf (Clean) kar deta hai
#         self.grid[position] = 'Clean'

#     def display_grid(self, agent_position):
#         # Grid ko 3x3 format mein print karta hai aur Agent ko [A] se show karta hai
#         print("\nCurrent Grid State:")
#         grid_with_agent = self.grid[:] # Grid ki copy banayi
#         grid_with_agent[agent_position] = "[A]" # Agent ki current position set ki

#         for i in range(0, 9, 3):
#             print(" | ".join(grid_with_agent[i:i + 3]))
#         print("-" * 25)


# class SimpleReflexAgent:
#     def __init__(self):
#         self.position = 0 # Agent hamesha dabbe 'a' (index 0) se start karega

#     def act(self, percept, grid):
#         # Agar current dabba ganda hai, toh safai ka action lo
#         if percept == 'Dirty':
#             grid[self.position] = 'Clean'
#             return 'Clean the room'
#         else:
#             return 'Room is clean'

#     def move(self):
#         # Agent ko agle dabbe par bhejo (jab tak 8 par na pohanch jaye)
#         if self.position < 8:
#             self.position += 1
#             return self.position


# def run_agent(agent, environment, steps):
#     for step in range(steps):
#         # 1. Agent mahol dekhta hai
#         percept = environment.get_percept(agent.position)
        
#         # 2. Agent dimagh laga kar action leta hai
#         action = agent.act(percept, environment.grid)
        
#         print(f"Step {step + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")
        
#         # 3. Screen par grid print hota hai
#         environment.display_grid(agent.position) 
        
#         # 4. Agar ganda tha toh environment mein pakki safai hoti hai
#         if percept == 'Dirty':
#             environment.clean_room(agent.position)
            
#         # 5. Agent agle dabbe par chala jata hai
#         agent.move()


# # === Program Yahan Se Run Hoga ===

# # Agent aur Environment banaye
# agent = SimpleReflexAgent()
# environment = Environment()

# # Agent ko 9 steps ke liye chalaya taake pure 9 dabbe (0 se 8) check ho jayein
# run_agent(agent, environment, 9)


# class Environment:
#     def __init__(self):
#         self.grid=["clean","dirty","clean",
#                    "dirty","clean","dirty",
#                    "dirty","dirty","clean"]
    
#     def get_percept(self, position):
#         return self.grid[position]
    
#     def clean_room(self,position):
#         self.grid[position]="clean"
    
#     def display_grid(self,agent_position):
#         print("current agent state")
#         grid_with_agent=self.grid[:]
#         grid_with_agent[agent_position]="[A]"
        
#         for i in (0,9,3):
#             print(" | ".join(grid_with_agent[i:i+3]))
            
#         print("-"*20)


# class SimpleReflex:
#     def __init__(self):
#         self.position=0
    
#     def act(self,percept,grid):
#         if percept=="dirty":
#             grid[self.position]="clean"
#             return "room cleaned"
#         else:
#             return "room already cleaned"
    
#     def move(self):
#         if self.position<8:
#             self.position+=1
#             return self.position
    

# def run_agent(agent,environment,steps):
#     for i in range(steps):
#         print(f"the step is {i+1} ")
        
#         current_percept=environment.get_percept(agent.position)
        
#         action=agent.act(current_percept,environment.grid)
        
#         environment.display_grid(agent.position)
        
#         if current_percept=="dirty":
#             environment.clean_room(agent.position)
        
#         agent.move()
        

# room1=Environment()

# vacuum_cleaner=SimpleReflex()

# run_agent(agent=vacuum_cleaner, environment=room1, steps=8)
        
        
        
        
class Environment:
    def __init__(self):
        self.grid=['clean', 'dirty', 'clean',
                     'clean', 'dirty', 'dirty',
                     'clean', 'clean', 'clean']
        
    def get_percept(self,position):
        return self.grid[position]
    
    def clean_room(self,position):
        self.grid[position]="clean"
    
    def display_grid(self,position):
        print("current state of the grid")
        agent_with_grid=self.grid[:]
        agent_with_grid[position]="[A]"
        
        for i in range(0,9,3):
            print(" | ".join(agent_with_grid[i:i+3]))
            
        print("-"*22)    

    
class Agent:
    def __init__(self):
        self.position=0
    
    def act(self,percept,grid):
        if percept=="dirty":
            grid[self.position]="clean"
            return "room cleaned"
        else:
            return "room already cleaned"
        
    def move(self):
        if self.position<8:
            self.position+=1
            return self.position
        
def run_agent(agent,environment,steps):
    for i in range(steps):
        print(f"the step is {i+1}")
        
        percept=environment.get_percept(agent.position)
        
        action=agent.act(percept,environment.grid)
        
        environment.display_grid(agent.position)
        
        if percept=="dirty":
            environment.clean_room(agent.position)
        
        agent.move()
            

room1=Environment()
v_agent=Agent()

run_agent(agent=v_agent,environment=room1,steps=9)
-------------------------------------------------------
import heapq

# === GRID SETUP FOR Q1 ===
# S=(0,0), G=(4,4). # = Obstacle. Numbers = Cost.
grid_q1 = [
    ['S', 1, '#', 2, 3],
    [2, '#', 2, '#', 1],
    [3, 2, 1, 2, 2],
    ['#', 2, '#', 1, 3],
    [2, 1, 2, 2, 'G']
]
rows, cols = 5, 5
start_node = (0, 0)
goal_node = (4, 4)

def get_neighbors(r, c):
    neighbors = []
    # Order: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid_q1[nr][nc] != '#':
            neighbors.append((nr, nc))
    return neighbors

def get_cost(r, c):
    val = grid_q1[r][c]
    if val in ['S', 'G']: return 0
    return int(val)

# 1. BFS (Breadth-First Search)
def bfs():
    queue = [(start_node, [start_node])]
    visited = []
    while queue:
        current, path = queue.pop(0)
        if current not in visited:
            visited.append(current)
            if current == goal_node:
                print(f"BFS Path: {path}\nBFS Expanded: {visited}\n")
                return
            for n in get_neighbors(*current):
                if n not in visited:
                    queue.append((n, path + [n]))

# 2. DFS (Depth-First Search)
def dfs():
    stack = [(start_node, [start_node])]
    visited = []
    while stack:
        current, path = stack.pop()
        if current not in visited:
            visited.append(current)
            if current == goal_node:
                print(f"DFS Path: {path}\nDFS Expanded: {visited}\n")
                return
            # Reverse neighbors for stack to expand Right/Down first
            for n in reversed(get_neighbors(*current)):
                if n not in visited:
                    stack.append((n, path + [n]))

# 3. UCS (Uniform Cost Search)
def ucs():
    # Priority Queue: (Total_Cost, Current_Node, Path)
    pq = [(0, start_node, [start_node])]
    visited = set()
    expanded = []
    
    while pq:
        cost, current, path = heapq.heappop(pq)
        if current in visited: continue
        
        visited.add(current)
        expanded.append(current)
        
        if current == goal_node:
            print(f"UCS Path: {path}\nUCS Expanded: {expanded}\nUCS Total Cost: {cost}\n")
            return
            
        for n in get_neighbors(*current):
            if n not in visited:
                new_cost = cost + get_cost(*n)
                heapq.heappush(pq, (new_cost, n, path + [n]))

print("--- QUESTION 1 OUTPUT ---")
bfs()
dfs()
ucs()
-----------------------------------------------------------------------------------
import heapq

# === GRID SETUP FOR Q2 ===
# Numbers = Heuristics (h). Cost of each step (g) = 1.
grid_q2 = [
    ['S', 4, '#', 2, 0],
    [3, '#', 3, '#', 1],
    [2, 2, 2, 2, 1],
    ['#', 3, '#', 1, 2],
    [3, 2, 3, 2, 'G']
]
rows, cols = 5, 5
start_node = (0, 0)
goal_node = (4, 4)

def get_neighbors_q2(r, c):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid_q2[nr][nc] != '#':
            neighbors.append((nr, nc))
    return neighbors

def get_heuristic(r, c):
    val = grid_q2[r][c]
    if val == 'S': return 4 # Start ki heuristic
    if val == 'G': return 0 # Goal ki heuristic
    return int(val)

# 1. Greedy Best-First Search (Uses only h)
def greedy():
    pq = [(get_heuristic(*start_node), start_node, [start_node])]
    visited = set()
    expanded = []
    
    while pq:
        h, current, path = heapq.heappop(pq)
        if current in visited: continue
        
        visited.add(current)
        expanded.append(current)
        
        if current == goal_node:
            print(f"Greedy Path: {path}\nGreedy Expanded: {expanded}\n")
            return
            
        for n in get_neighbors_q2(*current):
            if n not in visited:
                heapq.heappush(pq, (get_heuristic(*n), n, path + [n]))

# 2. A* Search (Uses g + h)
def a_star():
    # Priority Queue: (f_score, g_cost, Current_Node, Path)
    start_h = get_heuristic(*start_node)
    pq = [(start_h, 0, start_node, [start_node])]
    visited = set()
    expanded = []
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current in visited: continue
        
        visited.add(current)
        expanded.append(current)
        
        if current == goal_node:
            print(f"A* Path: {path}\nA* Expanded: {expanded}\nA* Total Path Cost (g): {g}\n")
            return
            
        for n in get_neighbors_q2(*current):
            if n not in visited:
                new_g = g + 1 # Assuming each step costs 1 moving to adjacent cell
                new_h = get_heuristic(*n)
                new_f = new_g + new_h
                heapq.heappush(pq, (new_f, new_g, n, path + [n]))

print("--- QUESTION 2 OUTPUT ---")
greedy()
a_star()
-----------------------------------------------------------------------------
import heapq

# 1. Environment Class (Graph with Costs AND Heuristics)
class Environment:
    def __init__(self, goal_node):
        # Graph mein (Padosi: Cost) hai. Isko g(n) kehte hain.
        self.graph = {
            'S': {'A': 1, 'B': 4},
            'A': {'B': 2, 'C': 5, 'G': 12},
            'B': {'C': 2},
            'C': {'G': 3},
            'G': {}
        }
        # Ye Agent ka Hint hai ke konsi jagah Goal se kitni door lag rahi hai. Isko h(n) kehte hain.
        self.heuristics = {
            'S': 7, 'A': 6, 'B': 4, 'C': 2, 'G': 0
        }
        self.goal = goal_node

    def get_neighbor(self, node):
        return self.graph.get(node, {})
        
    def get_heuristic(self, node):
        return self.heuristics.get(node, 0)

    def is_goal(self, node):
        return node == self.goal

# 2. A* Agent Class
class AStarAgent:
    def __init__(self, start_node, environment):
        # Priority Queue (VIP Line). Isme (f_score, actual_cost, node) save karenge
        # Shuru mein cost 0 hai. f_score = 0 + heuristic(start_node)
        start_h = environment.get_heuristic(start_node)
        self.pq = [(start_h, 0, start_node)]  
        self.visited = []
        self.current_node = None

    def act(self, environment):
        if len(self.pq) == 0:
            return "Fail"

        # heapq sab se kam f_score wale ko nikalega
        current_f, current_cost, self.current_node = heapq.heappop(self.pq)

        if environment.is_goal(self.current_node):
            return "Goal Found"

        if self.current_node not in self.visited:
            self.visited.append(self.current_node)
            
            neighbors = environment.get_neighbor(self.current_node)
            for neighbor, step_cost in neighbors.items():
                if neighbor not in self.visited:
                    # g(n) = Ab tak ka kharcha + Naye qadam ka kharcha
                    g_cost = current_cost + step_cost 
                    
                    # h(n) = Naye node ka Hint
                    h_cost = environment.get_heuristic(neighbor) 
                    
                    # f(n) = g(n) + h(n)  <--- YAHI A* KI JAAN HAI
                    # AGAR GREEDY BANANA HO TOH: f_cost = h_cost (Bas g_cost hata do!)
                    f_cost = g_cost + h_cost 
                    
                    heapq.heappush(self.pq, (f_cost, g_cost, neighbor))
                    
        return "searching......"

def run_agent(agent, environment, steps):
    for i in range(steps):
        print(f"\n--- Step {i+1} ---")
        action = agent.act(environment)
        print(f"Agent is checking: {agent.current_node}")
        
        if action == "Goal Found":
            print(f"🎉 Goal Found at {agent.current_node}!")
            break

# Run A* Search
env = Environment(goal_node="G")
astar_agent = AStarAgent(start_node="S", environment=env)
run_agent(astar_agent, env, 10)
-----------------------------------------------------------------
simple agents
---------------------------------------------------------------
class SimpleReflexAgent:
    def act(self, location, status):
        # Agar kachra hai, toh saaf karo
        if status == 'Dirty':
            return 'Suck (Kachra uthao)'
        
        # Agar kachra nahi hai, toh dusre kamre mein jao
        elif location == 'A':
            return 'Move Right (Kamra B mein jao)'
        elif location == 'B':
            return 'Move Left (Kamra A mein jao)'

# Run:
agent1 = SimpleReflexAgent()
print(agent1.act('A', 'Dirty')) # Output: Suck
----------------------------------------------------
class ModelBasedAgent:
    def __init__(self):
        # Agent ki Memory (Model of the world)
        self.memory = {'A': 'Unknown', 'B': 'Unknown'}

    def act(self, location, status):
        # Pehle apni memory update karo jo abhi dekha
        self.memory[location] = status

        # Agar dono saaf hain, toh aaraam karo (No infinite loop)
        if self.memory['A'] == 'Clean' and self.memory['B'] == 'Clean':
            return 'Stop (Kaam khatam)'

        # Baqi rules wahi Simple Reflex wale
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Move Right'
        elif location == 'B':
            return 'Move Left'

# Run:
agent2 = ModelBasedAgent()
print(agent2.act('A', 'Clean')) # A clean hai, B me jayega
print(agent2.act('B', 'Clean')) # B bhi clean mila, Memory update hui aur STOP ho jayega.
------------------------------------------------------------------------------------------
class GoalBasedAgent:
    def __init__(self, goal_location):
        self.goal = goal_location

    def act(self, current_location, map_graph):
        # Action lene se pehle ye dekhega ke Goal kahan hai
        if current_location == self.goal:
            return "Goal Reached! Chill."
        
        # Yahan ye BFS ya A* chala kar poora rasta (plan) banayega
        path = self.calculate_path_to_goal(current_location, map_graph)
        
        # Raste ka pehla qadam uthayega
        return f"Move towards {path[0]}"

    def calculate_path_to_goal(self, current, map_graph):
        # (Imagine here is the BFS/A* code we wrote earlier)
        return ["Next_Node"]
----------------------------------------------------------------------------------------------------
class UtilityBasedAgent:
    def act(self, current_location, possible_actions):
        best_action = None
        highest_utility = -999 # Shuru mein khushi zero hai
        
        # Har action ko check karega ke isme kitna faida/kharcha hai
        for action in possible_actions:
            # Utility Formula = Faida - Kharcha
            expected_utility = self.evaluate_happiness(current_location, action)
            
            if expected_utility > highest_utility:
                highest_utility = expected_utility
                best_action = action
                
        # Sab se faide-mand action return karega
        return best_action

    def evaluate_happiness(self, location, action):
        # Misaal: Agar action me time kam lag raha he to happiness zyada hogi
        return 10 # Example score
--------------------------------------------------------------------------------------------------
class LearningAgent:
    def __init__(self):
        # Iski performance ki history
        self.knowledge_base = {}

    def act(self, state):
        # Agar is state ka pehle se pata hai, toh purana knowledge use karo
        if state in self.knowledge_base:
            return self.knowledge_base[state]
        else:
            return "Try Random Action" # Shuru mein random try karega

    def learn(self, state, action, reward):
        # Kaam karne ke baad jo result (Reward) mila, us se seekho
        if reward > 0:
            print(f"Good! I learned that doing {action} in {state} is beneficial.")
            self.knowledge_base[state] = action
        else:
            print(f"Bad choice. I won't do {action} in {state} again.")
-----------------------------------------------------------------------------------------------------
agents with grid
---------------------------------------------------------------------
import random

print("--- 1. Simple Reflex Agent ---")
# Grid: 'D' = Dirty, 'C' = Clean
grid = [
    ['D', 'C'],
    ['C', 'D']
]

class SimpleReflexAgent:
    def act(self, r, c, grid):
        status = grid[r][c]
        if status == 'D':
            grid[r][c] = 'C' # Kachra saaf kar diya
            return f"Action: Suck (Cleaned {r},{c})"
        else:
            # Agar clean hai toh andha-dhund (random) move karo kyunke memory nahi hai
            move = random.choice(["Right", "Down", "Left", "Up"])
            return f"Action: Move {move} (Just wandering randomly)"

agent = SimpleReflexAgent()
# Agent (0,0) par hai
print(f"Step 1: {agent.act(0, 0, grid)}") 
# Agle step mein wo kahan jayega? Usko khud nahi pata!
print(f"Step 2: {agent.act(0, 0, grid)}") # Ab wahan 'C' hai, toh random move karega
--------------------------------------------------------------------------------
print("\n--- 2. Model-Based Agent ---")
grid_model = [
    ['D', 'D'],
    ['C', 'D']
]

class ModelBasedAgent:
    def __init__(self):
        # Dimagh mein grid ka naqsha (Memory)
        self.memory = set() 
        self.total_dirty_spots = 3 # Farz karo isey pata hai 3 kachre hain

    def act(self, r, c, grid):
        status = grid[r][c]
        
        # Memory update karo
        self.memory.add((r, c))
        
        if len(self.memory) == 4: # Agar poora grid ghoom lia
            return "Action: Stop! Pura grid visit ho gaya."

        if status == 'D':
            grid[r][c] = 'C'
            self.total_dirty_spots -= 1
            if self.total_dirty_spots == 0:
                return f"Action: Suck (Cleaned {r},{c}). STOP! Sab saaf ho gaya."
            return f"Action: Suck (Cleaned {r},{c})"
        else:
            return f"Action: Move to next unvisited room"

agent2 = ModelBasedAgent()
print(agent2.act(0, 0, grid_model))
print(agent2.act(0, 1, grid_model))
print(agent2.act(1, 1, grid_model)) # Yahan aakar isey pata chal jayega ke sab saaf hai
----------------------------------------------------------------------------------------
print("\n--- 3. Goal-Based Agent ---")
# Scenario: S se G jana hai
grid_goal = [
    ['S', '0', 'G'],
    ['#', '#', '0']
]

class GoalBasedAgent:
    def plan_path(self):
        # Is agent ka dimagh future ka sochta hai. Ye pehle map dekhta hai aur path plan karta hai
        print("Thinking... Planning path to Goal using Search...")
        # (Assume BFS runs here internally and finds the path)
        planned_path = ["Right", "Right"]
        return planned_path

    def act(self, path):
        print("Executing Plan:")
        for step in path:
            print(f"Moving {step}")
        print("Goal Reached!")

agent3 = GoalBasedAgent()
my_plan = agent3.plan_path()
agent3.act(my_plan)
---------------------------------------------------------------------
print("\n--- 4. Utility-Based Agent ---")
# Scenario: 2 raste. Rasta A (Cost 10, Aag). Rasta B (Cost 2, Safe)
paths = {
    "Path_Through_Fire": {"steps": 1, "danger_cost": 10},
    "Path_Around_Fire": {"steps": 3, "danger_cost": 1}
}

class UtilityBasedAgent:
    def act(self, available_paths):
        best_path = None
        best_utility = -999 # Shuru mein khushi negative hai

        for path_name, details in available_paths.items():
            # Utility Formula = (Goal Pohanchne ka Faida 100) - (Steps + Danger Cost)
            # Jo agent math aur cost/heuristic check kare, wo Utility agent hota hai!
            utility = 100 - (details["steps"] + details["danger_cost"])
            print(f"Checking {path_name}: Utility Score = {utility}")
            
            if utility > best_utility:
                best_utility = utility
                best_path = path_name
                
        return f"Action: I choose '{best_path}' because it has the highest utility ({best_utility})"

agent4 = UtilityBasedAgent()
print(agent4.act(paths))
---------------------------------------------------------------------------
print("\n--- 5. Learning Agent ---")
# Scenario: (0,1) par ek Trap hai.
grid_learn = [
    ['S', 'Trap', 'G']
]

class LearningAgent:
    def __init__(self):
        self.knowledge = {} # Ye iski "Seekh" (Learning) hai

    def act(self, current_pos):
        # Agar memory mein pehle se pata hai ke agay khatra hai, toh rasta badlo
        if current_pos in self.knowledge and self.knowledge[current_pos] == "Danger":
            return "Action: Jump over the Trap (Learned from past mistake!)"
        else:
            return "Action: Move Right (I don't know what's ahead)"

    def learn(self, state, reward):
        if reward < 0:
            print(f"Ouch! Critic says: Bad move. I learned that {state} leads to a trap.")
            self.knowledge[state] = "Danger" # Dimagh mein save kar lia

agent5 = LearningAgent()

print("--- First Run (Ignorant) ---")
action1 = agent5.act("Pos_0")
print(action1)
# Agent falls in trap and gets -10 reward
agent5.learn("Pos_0", reward=-10) 

print("\n--- Second Run (Experienced) ---")
action2 = agent5.act("Pos_0")
print(action2) # Ab isne apna behavior tabdeel kar liya!
-------------------------------------------------------------------------------------
