import collections

def nodeDict(filename):
    nodes=open(filename, "r")
    #d = collections.OrderedDict()
    d = {}
    num_lines = 0
    for line in nodes.readlines():
        lineList = line.replace("-", " ").strip().split(" ")

        for i in range(1, len(lineList)+1,2):
            num_lines += 1
            try:
                d[lineList[0]].append(lineList[i])
            except KeyError:
                d[lineList[0]] = [lineList[i]]
#    print(d)
    return d, num_lines//2


#nodeDict("graphOne.in")
