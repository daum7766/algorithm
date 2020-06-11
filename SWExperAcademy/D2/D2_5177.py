#D2 5177 이진힙
def sort_heap(idx):
    if idx >= N:
        return
    if idx*2 < N and heap[idx] > heap[idx*2]:
        heap[idx], heap[idx*2] = heap[idx*2], heap[idx]
    if idx*2+1 < N and heap[idx] > heap[idx*2]:
        heap[idx], heap[idx*2+1] = heap[idx*2+1], heap[idx]
    sort_heap(idx*2)
    sort_heap(idx*2+1)

for t in range(int(input())):
    answer = 0
    N = int(input())
    heap = [0] + list(map(int, input().split()))
    sort_heap(1)
    idx = len(heap)-1
    while idx:
        idx //= 2
        answer += heap[idx]
    print('#{} {}'.format(t+1, answer))
    