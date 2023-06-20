import heapq

n = int(input())

w = list(map(int, input().split()))

passenger = input()

intro = [(w_i, i + 1) for i, w_i in enumerate(w)]
extro = []

heapq.heapify(intro)
heapq.heapify(extro)

res = []

for p in passenger:
    if p == "0":
        w, ind = heapq.heappop(intro)
        res.append(str(ind))
        heapq.heappush(extro, (-1 * w, ind))
    else:
        res.append(str(heapq.heappop(extro)[1]))

print(" ".join(res))
