from graphClass import Graph
from nodeDict import nodeDict

#------------------------- Functionality Functions -------------------------
G = Graph()

def textToGraph():
  fname = input("What file do you want to use?")
  readData, num_lines = nodeDict(fname)
  #print(readData)
  for i in readData.keys():
    origin = G.insert_vertex(i)
  for i in readData.keys():
    for j in readData[i]:
      origin = G.insert_vertex(i)
      dest = G.insert_vertex(j)
      e = G.insert_edge(origin, dest)
      #if e == None:
      #  e = G.insert_edge(dest, origin)
      #print(origin.cityName(),e.opposite(origin).cityName())
  return G, num_lines

def printGraph(a_Graph):
  for vertices in a_Graph._cities:
    name,val = vertices.cityName(), vertices.get_val()
    print("Node: {0}, Name: {1}".format(val,name))
    currentCityLinkedList = a_Graph._cities[vertices]
    currentEdge = currentCityLinkedList.get_head_value()
    while currentEdge:
      edge_val = currentEdge.opposite(vertices).get_val()
      print("\tEdge: {0}".format(edge_val))
      #print(a_Graph._cities[vertices].size())
      currentEdge = currentEdge.next_edge(a_Graph._cities[vertices])

def DFS_visit(a_Graph, start_v):
  visited_ver = []
  visited_edge = []
  stack = [start_v]
  cycle = False
  pre,vertex = None,None
  while stack:
    pre = vertex
    vertex = stack.pop()

    if pre and vertex:
      v_edge = a_Graph.get_edge(pre, vertex)
    
      if v_edge:
        if v_edge not in visited_edge:
          visited_edge.append(v_edge)
          #print(v_edge)
          if vertex in visited_ver:
            cycle = True
        else:
          continue

    if vertex not in visited_ver:
      #print(vertex.cityName())
      visited_ver.append(vertex)
      currentCityLinkedList = a_Graph._cities[vertex]
      currentEdge = currentCityLinkedList.get_head_value()
      while currentEdge:
        edge_name = currentEdge.opposite(vertex)
        stack.append(edge_name)
        #print(edge_name)
        oldEdge = currentEdge
        currentEdge = currentEdge.next_edge(a_Graph._cities[vertex])
        if oldEdge == currentEdge:
          break
    else:
      vertex = pre

  return visited_ver, visited_edge, cycle

def DFS(a_Graph):
  num_visited_ver, num_visited_edge, components, cycle = 0,0,[],False
  remaining_nodes = list(a_Graph._cities.keys())
  while num_visited_ver < a_Graph._count:
    if remaining_nodes:
      current_node = remaining_nodes[0]
      new_ver, new_edges, new_cycle = DFS_visit(a_Graph,current_node)
      if new_cycle == True:
        cycle = new_cycle
      num_visited_ver += len(new_ver)
      num_visited_edge += len(new_edges)
      #print(len(new_edges))
      named_ver = [i.cityName() for i in new_ver]
      #print(named_ver)
      components.append(named_ver)
      remaining_nodes = list(set(remaining_nodes) - set(new_ver))
    else:
      break
  return components, num_visited_ver, num_visited_edge, cycle

def printComponents(a_Graph, num_lines):
  components, num_visited_ver, num_visited_edge, cycle = DFS(a_Graph)
  print("Read {0} cities and {1} edges".format(num_visited_ver, num_lines))
  print("Number of connected components: {0}".format(len(components)))
  for i in range(len(components)):
    print("  Connected Component {0}:".format(i+1))
    for j in components[i]:
      print("\t{0}".format(j))
  if cycle:
    print("Graph Contains a Cycle")
  else:
    print("Graph Does Not Contain a Cycle")

if __name__ == '__main__':
 G, num_lines = textToGraph()
 printComponents(G,num_lines)