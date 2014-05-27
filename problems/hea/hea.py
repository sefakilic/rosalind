# http://rosalind.info/problems/hea/
import math

def heapify(heap, i):
    """Given a heap and recently added element at heap[i], perform up-heap
    operation to conserve the heap property"""
    if i==0:
        return
    parent = (i-1)/2
    child = i
    if heap[parent] > heap[child]:
        return
    else:
        heap[parent], heap[child] = heap[child], heap[parent]
        heapify(heap, parent)
    
def hs():
    with open("rosalind_hea.txt") as f:
        n = int(f.readline().strip())
        A = map(int, f.readline().split())
    heap = []
    # build heap here
    for i in range(len(A)):
        # add element to the bottom level of the heap.
        heap.append(A[i])
        # heapify
        heapify(heap, i)
    # print heap
    print ' '.join(map(str, heap))

if __name__ == "__main__":
    hs()
