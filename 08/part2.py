file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

# parse the input for boxes
boxes = [(int(a), int(b), int(c)) for a,b,c in [line.split(",") for line in data.split("\n")]]

# euclidean distance squared
# no square root saves time, the ordering is the same even when you don't square root
def sq_distance(left, right):
    la,lb,lc = left
    ra,rb,rc = right
    return (ra - la) * (ra - la) + (rb - lb) * (rb - lb) + (rc - lc) * (rc - lc)

# find every connection and store its distance
# connections are represented as (a, b) where a and b are indices of the original boxes in `boxes`
# a < b always, so that no connections get double counted
connections = []
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        connections.append((sq_distance(boxes[i], boxes[j]), (i, j)))

# tree-representation of circuits
# network[0] = -5 => 0 is the owner of a circuit with 5 nodes
# network[1] = 0 => 1 is part of the same network as 0
# network[2] = 1 => 2 is part of the same network as 1
# network[14] = 19 is possible, it doesn't strictly have to descend
networks = {}

def get_network(node):
    if node not in networks:
        return (node, 1)
    if networks[node] >= 0:
        return get_network(networks[node])
    return (node, -networks[node])

for a, b in ([connection for _, connection in sorted(connections)]):
    # a < b always, and the lower number is always the "circuit owner"
    anet, anet_size = get_network(a)
    bnet, bnet_size = get_network(b)
    # if both nodes already in the same network skip, otherwise merge their sizes and update the references
    if anet != bnet:
        networks[bnet] = anet
        networks[anet] = -(bnet_size + anet_size)
    if networks[anet] == -len(boxes):
        print("the whole set of boxes is now in one circuit!")
        print(boxes[a][0] * boxes[b][0])
        break