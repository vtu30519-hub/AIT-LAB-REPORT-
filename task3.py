import networkx as nx
def a_str_pathfinding(graph,start_node,goal_node,heuristic):
    try:
        path=nx.astar_path(graph,star_node,goal_node,heuristic=heuristic,)
        return path
    except nx.networkxNoPath:
        return None
if __name__=="__main__":
    G=nx.graph()
    G.add_edge('S','A',weight=2)
    G.add_edge('S','B',weight=3)
    G.add_edge('A','G',weight=1)
    G.add_edge('B','G',weight=2)
    heuristic_values={'S':5,'A':2,'B':3,'G':0}
    def example_heuristic(u, v):
        return heuristic_values.get(u,0)
    start='S'
    goal='G'
    path=a_star_pathfinding(G,start,goal,example_heuristic)
    if path:
        print(f"path found from {start} to {goal}: {path}")
        length=nx.astart_path_length(G,start,goal,heuristic=example_heuristic)  
        print(f"path length:{length}")
    else:
        print(f"No path fount from {start} to {goal}.")                                                                                                                                                                                                           
