import sys
import threading


class NodeClass:
    def __init__(self, i):
        self.i = i
        self.parent = None
        self.child = []

    def add_child(self, child):
        self.child.append(child)
        child.parent = self


def compute_height(n, pr):
    nodesAll = [NodeClass(i) for i in range(n)]
    root_i = -1

    for i, parent_i in enumerate(pr):
        if parent_i == -1:
            root_i = i
        else:
            parent = nodesAll[parent_i]
            parent.add_child(nodesAll[i])

    root = nodesAll[root_i]
    line = [root]
    h = 0

    while line:
        lineArray = []
        h += 1

        for node in line:
            lineArray.extend(node.child)

        line = lineArray
    return h


def main():
    usersChoice = input().lower()

    if usersChoice == 'i':
        n = int(input())
        pr = list(map(int, input().split()))
    elif usersChoice == 'f':
        fname = input()

        if 'a' in fname:
            return

        try:
            with open('data/' + fname, 'r') as f:
                n = int(f.readline())
                pr = list(map(int, f.readline().split()))
        except Exception:
            return
    else:
        return

    print(compute_height(n, pr))


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
main()
