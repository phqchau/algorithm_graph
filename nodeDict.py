def nodeDict(filename):
    nodes=open(filename, "r")
    d = {}
    for line in nodes.readlines():
        lineList = line.replace("-", " ").strip().split(" ")

        for i in range(1, len(lineList)+1,2):
            try:
                d[lineList[0]].append(lineList[i])
            except KeyError:
                d[lineList[0]] = [lineList[i]]
    return d
    print(d)
