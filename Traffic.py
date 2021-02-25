D, I, S, V, F = list(map(int, input().split()))

streets = []
for _ in range(S):
    # each entry has b, e, l
    street = input().split()
    street[0] = int(street[0])
    street[1] = int(street[1])
    street[3] = int(street[3])
    streets.append(street)

paths = []
for _ in range(V):
    path = input().split()
    path[0] = int(path[0])
    paths.append(path)
