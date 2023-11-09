q = input()

queue = []


def enqueue(elem):
    queue.append(elem)


def dequeue():
    return queue.pop(0)


for i in range(int(q)):
    query = input().split()
    if query[0] == "1":
        enqueue(query[1])
    elif query[0] == "2":
        dequeue()
    elif query[0] == "3":
        print(queue[0])
