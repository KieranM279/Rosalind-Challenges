
####    Step 1    ####    Import the data    ####

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

nodes, edges = Dictmaker('rosalind_tree2.txt')

####    Step 2    ####    Creates a dictionary of sub-trees    ####

def minEdges(nodes, edges):

    # Small equation to calculate the minimum number of edges required
    m = nodes-int(len(edges.keys()))-1

    print(m)

minEdges(nodes, edges)
