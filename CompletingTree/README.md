# Completing a tree
## Usage
```Python
# Creates two variables: nodes (number of nodes), edges (adjacency list)
nodes, edges = Dictmaker('rosalind_tree2.txt')
# Calculates the minimum number of edges required to complete the tree
minEdges(nodes, edges)
```
## Methods
#### Step 1 - Import the data - Dictmaker()
This function parses through the Rosalind text file and saves the number of nodes and then creates a dictionary of the edges in the adjacency list.

edges = {edge number:['node A', 'node B']}
```Python
def Dictmaker(filename):

    # Open the data and intialize required variables
    data = open(filename)
    counter = 0
    edges = {}

    # Parse the data
    for ln in data:

        # format data properly
        ln = ln.strip()
        ln = ln.split()

        # Identify the number of nodes and the adjacency list
        if counter == 0:
            n = int(ln[0])
        elif counter != 0:
            no = int(counter)
            edge = ln

            # Generate the dictionary
            edges[no] = edge

        counter += 1

    # Return total node number and adjacency 'dictionary'
    return(n, edges)
```
#### Step 2 - Calculate the minimum number of edges - minEdges()
Simple function which takes the number of number of nodes and subtracts the number of edges plus 1: (i.e. min = nodes - edges - 1)
```Python
def minEdges(nodes, edges):

    # Small equation to calculate the minimum number of edges required
    m = nodes - int(len(edges.keys())) - 1

    print(m)
```
