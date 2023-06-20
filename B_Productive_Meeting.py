import heapq


t = int(input())


for _ in range(t):
    n = map(int, input().split())
    a = list(map(lambda x: -1 * int(x), input().split()))
    a = [[x, i] for i, x in enumerate(a)]
    heapq.heapify(a)
    res = []
    ans = 0

    while a:
        m_1, i_1 = heapq.heappop(a)
        if a:
            m_2, i_2 =  heapq.heappop(a)
        else:
            break

        m_1, m_2 = -1 * m_1, -1 * m_2 
        
        if not m_2 or not m_1:
            break

        res.append((i_1, i_2, m_2))
        ans += m_2
        m_1 -= m_2
        if m_1:
            heapq.heappush(a, [-1 * m_1, i_1])

    print(ans)
    for i_1, i_2, f in res:
        for j in range(f):
            print(i_1 + 1, i_2 + 1)
    
        
        


    
    
