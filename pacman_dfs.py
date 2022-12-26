import re
### get the inputs ###
P = tuple(map(int, re.findall('\d+',input())))
F = tuple(map(int, re.findall('\d+',input())))
Size = tuple(map(int, re.findall('\d+',input())))
Ground = []

for r in range(0,int(Size[0])):
    Ground.append(list(input()))

### DFS ###

Closed = []
Open = []
Open.append((int(P[0]), int(P[1])))
parent = {}
parent[P] = [P]
# end the loop if all possible node's are explored
while len(Open) != 0:
        node = Open.pop()
        if node not in Closed+Open:
            Closed.append(node)
            if node[0] == (11,14):
                pass
            #if the Pacman fineds food break the loop
            if node == F:
                Path = parent[node]
                break
            # create neighbouring indexes
            UP, DOWN, LEFT, RIGHT = node[0]-1, node[0]+1, node[1]-1, node[1]+1

            # search for boundary and update nodes to Open
            if UP > 0 and Ground[UP][node[1]] == '-' or Ground[UP][node[1]] == '.' and (UP,node[1]) not in Open+Closed:
                Open.append((UP, node[1]))
                parent[(UP, node[1])] = parent[node] + [(UP, node[1])]
                Ground[UP][node[1]] = '#'

            if LEFT > 0  and Ground[node[0]][LEFT] == '-' or  Ground[node[0]][LEFT] == '.' and (node[0],LEFT) not in Open+Closed:
                Open.append((node[0], LEFT))
                parent[(node[0], LEFT)] = parent[node] + [(node[0], LEFT)]
                Ground[node[0]][LEFT] = '#'

            if RIGHT < Size[1] and Ground[node[0]][RIGHT] == '-' or Ground[node[0]][RIGHT] == '.' and (node[0], RIGHT) not in Open+Closed:
                Open.append((node[0], RIGHT))
                parent[(node[0], RIGHT)] = parent[node] + [(node[0], RIGHT)]
                Ground[node[0]][RIGHT] = '#'

            if DOWN < Size[0] and Ground[DOWN][node[1]] == '-' or Ground[DOWN][node[1]] == '.' and (DOWN, node[1]) not in Open+Closed:
                Open.append((DOWN, node[1]))
                parent[(DOWN, node[1])] = parent[node] + [(DOWN, node[1])]
                Ground[DOWN][node[1]] = '#'
                
              

print(len(Closed))
for n in Closed:
    print(f'{n[0]} {n[1]}')

print(len(Path)-1)
for n in Path:
    print(f'{n[0]} {n[1]}')
