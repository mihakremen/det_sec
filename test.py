if __name__ == '__main__':
    with open('/home/runner/work/project_secret/project_secret/pathes.txt', 'r') as f:
        var = f.readline().split(' ')
    for path in var:
        path = path.rstrip()
        print(path)
    print(var)
 password: lovalova134
