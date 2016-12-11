from linked_list import LinkedList
import collections
from nodeDict import nodeDict

class Graph:
  """Representation of a simple Graph ADT using adjacency-list"""

  #------------------------- nested Edge class -------------------------
  class Edge:
    """Lightweight edge structure for a graph."""

    __slots__ = '_origin', '_destination'#, '_element'

    def __init__(self, u, v):#, x=None):
      """Do not call constructor directly. x represents the next edge"""
      self._origin = u
      self._destination = v
      #self._next = x

    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)

    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      if v is self._origin:
        return self._destination
      elif v is self._destination:
        return self._origin
      else:
        raise ValueError('v not incident to edge')

    def next_edge(self, lnk_list):
      """Return the subsequent edge in the graph."""
      #lnk_list = theGraph#[self._origin]
      current = lnk_list.search(self) # returns a node in linked list
      next_loc =  current.get_next() # returns the next node
      #required_edge = next_loc.get_data() # returns the next edge
      if next_loc != None:
        return next_loc.get_data()
      else:
        return None

    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0}<->{1})'.format(self._origin,self._destination)

        # two selector functions
        #    one returns the index of the node at the other end of the edge
        #    another returns a pointer to the next edge in the list

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_cityName', '_cityValue'

    def __init__(self, x,y):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._cityName = x
      self._cityValue = y

    def cityName(self):
      """Return element associated with this vertex."""
      return self._cityName

    def get_val(self):
      return self._cityValue

    def changeVal(self, newVal):
      self._cityValue = newVal

    def changeName(self, newName):
      self._cityName = newName

    def firstEdge(self, theGraph):
      """ returns the first edge from the adjacency-list of the vertex

      theGraph            the graph the node is in"""
      edges = theGraph[self]
      first = edges.get_head_value()
      return first

    def addEdge(self, theGraph, newEdge):
      """ adds an edge to the adjacent list of the node

      theGraph            the graph the node is in
      newEdge             the edge to be added"""
      edges = theGraph[self]
      edges.insert(newEdge)

    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str("{0},{1}".format(self._cityName, self._cityValue))

        # data field for names

        #selector functions, return value of each data field
        #mutator funtons,ge modify eah data field
        #function firstEd returnds a pointer/reference to the first edge in the list of adjacent nodes
        #funtion addEdge adds a new edge to the adjacent list of the node

    # a function searchCity given the name of a city, it searches the graph for a
    # node with that name , adds a new node to the graph with that name if
    # there is no such node , and (in any case) returns the index of the node

  #------------------------- Graph functions -------------------------
  def __init__(self):
    """Create an empty graph (undirected, by default).

    Graph is undirected.
    """
    self._cities = collections.OrderedDict()
    self._count = 0

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._cities:
      raise ValueError('Vertex does not belong to this graph.')

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    found = False
    lnk_list = self._cities[u]
    current = lnk_list.get_head_value()
    while not found:
      if current:
        if current.opposite(u) == v:
          return current
        try:
          current = current.next_edge(lnk_list)
        except:
          return None
      else:
        return None

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    for i in self._cities:
      if i.cityName() == x:
        return i
    v = self.Vertex(x,self._count)
    self._cities[v] = LinkedList()
    self._count += 1
    return v

  def insert_edge(self, u, v):
    """Insert and return a new Edge from u to v with integer x as pointer to next edge in linked list.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
    if self.get_edge(u, v) is None:      # includes error checking
      #raise ValueError('u and v are already adjacent')
      #e = self.Edge(u, v)#, x)
      #lnk_list = self._cities[u]
      e = self.Edge(u, v)
      u.addEdge(self._cities, e)
      v.addEdge(self._cities, e)

      return e
    else:
      return self.get_edge(u, v)

  def searchCity(self, cityName):
    for i in self._cities:
      if i.cityName() == cityName:
        return i._cityValue
    self.insert_vertex(cityName)
    return self._count

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
    #for i in range(1):
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
  #vertex = stack.pop()
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
      #v = a_Graph.insert_vertex(vertex)
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
  # if a_Graph._count > visited_ver: a_Graph._cities.keys() - visited_ver
  num_visited_ver, num_visited_edge, components, cycle = 0,0,[],False
  remaining_nodes = list(a_Graph._cities.keys())
  #run_n = 0
  while num_visited_ver < a_Graph._count:
    if remaining_nodes:
      current_node = remaining_nodes[0]
      #print(run_n)
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
    #run_n+=1
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
 #printGraph(G)
 printComponents(G,num_lines)
 

