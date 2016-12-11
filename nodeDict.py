import collections

def nodeDict(filename):
    nodes=open(filename, "r")
    #d = collections.OrderedDict()
    d = {}
    for line in nodes.readlines():
        lineList = line.replace("-", " ").strip().split(" ")

        for i in range(1, len(lineList)+1,2):
            try:
                d[lineList[0]].append(lineList[i])
            except KeyError:
                d[lineList[0]] = [lineList[i]]
#    print(d)
    return d


#nodeDict("graphOne.in")
