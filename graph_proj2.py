from linked_list import LinkedList

class Graph:
  """Representation of a simple Graph ADT using adjacency-list"""

  #------------------------- nested Edge class -------------------------
  class edge:
    """Lightweight edge structure for a graph."""

    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x

    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)

    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')

    def element(self):
      """Return element associated with this edge."""
      return self._element

    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)

        # two selector functions
        #    one returns the index of the node at the other end of the edge
        #    another returns a pointer to the next edge in the list

  #------------------------- nested Vertex class -------------------------
  class vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'

    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x

    def element(self):
      """Return element associated with this vertex."""
      return self._element

    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str(self._element)


        # data field for names

        #selector functions, return value of each data field
        #mutator funtons,ge modify eah data field
        #function firstEd returnds a pointer/reference to the first edge in the list of adjacent nodes
        #funtion addEdge adds a new edge to the adjacent list of the node

    # a function searchCity given the name of a city, it searches the graph for a
    # node with that name , adds a new node to the graph with that name if
    # there is no such node , and (in any case) returns the index of the node

    def searchCity(cityName):
