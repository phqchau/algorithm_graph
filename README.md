Implementation
You are required to implement this program using an adequate set of abstract data types. An adequate set of ADTs will include:
• a type for graph nodes which includes all of the per-node data your algorithm requires
• a type which will represent edges in the adjacency list representation of the graph
The graph itself (the adjacency list) can simply be represented as an array of graph nodes. By including all the per-node data in the graph node data type, you will avoid the need to implement these attributes as arrays parallel to the adjacency list representation of the graph.

For edges, you will likely only need:
• an initialization function
• two selector functions
o one returns the index of the node at the other end of the edge
o another returns a pointer to the next edge in the list

For the nodes in the graph, provide the following:
• A data field used to store the name of the city
• Selector functions: return the value of each data field
• Mutator functions: modify each data field of a node
• A function firstEdge: returns a pointer/reference to the first edge in the list of adjacent nodes
• A function addEdge: adds a new edge to the adjacent list of the node

For the graph, provide the following:
• A function searchCity: given the name of a city, it searches the graph for a node with that name, adds a new node to the graph with that name if there is no such node, and (in any case) returns the index of the node

In order to verify that your ADTs and the input function are working correctly, you should implement a test program that reads the input file, builds the adjacency list for the graph and traverses the structure as an array of graph vertices, listing each node by name and index along with the indexes of vertices it is adjacent to. (See Figure 2.)
