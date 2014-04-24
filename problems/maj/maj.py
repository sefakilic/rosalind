# http://rosalind.info/problems/maj/

if __name__ == '__main__':
    k, n = map(int, raw_input().split())
    for i in xrange(k):
        nums = map(int, raw_input().split())
        for n in set(nums):
            if nums.count(n) > len(nums)/2:
                print n,
                break
        else:
            print -1,
    print ''
    
