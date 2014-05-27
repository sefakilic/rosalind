import random

def ps(xs, k):
    """Given an array xs, return k smallest elements of the sorter array"""
    def partition(xs, n):
        """Partition the array such that the first partition has elements <= n
        and the second partition has elements > n"""
        return ([x for x in xs if x <= n], [x for x in xs if x > n])

    if k == 0:
        return []

    # select random element from list and partition the array
    lxs, rxs = partition(xs, random.choice(xs))

    if len(lxs) > k:
        return ps(lxs, k)
    else:
        return lxs + ps(rxs, k-len(lxs))


def ps_main():
    with open("rosalind_ps.txt") as f:
        f.readline()
        xs = map(int, f.readline().split())
        k = int(f.readline())

    print ' '.join(map(str, sorted(ps(xs, k))))

if __name__ == "__main__":
    ps_main()
