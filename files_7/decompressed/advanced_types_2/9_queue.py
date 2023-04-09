from collections import deque

queue = deque([1, 2])
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)
queue.popleft()

print(queue)


max_e = 40000000
first_set = set(range(max_e))
second_set = set(range(max_e))
second_set = set([e for e in second_set if e % 7 == 0])
print(len(first_set))
print(len(second_set), "\n")
print(len(first_set - second_set))
