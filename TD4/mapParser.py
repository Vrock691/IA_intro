def parseMap(path):
    map = []
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        map.append([])
        for char in line:
            if (char == '0' or char == '1'):
                map[i].append(int(char))
    file.close()
    return map