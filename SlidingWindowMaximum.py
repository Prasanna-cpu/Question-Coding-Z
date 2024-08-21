from collections import deque


def sliding_window_maximum(nums,k):
    if not nums or k==0:
        return []

    n=len(nums)
    deq=deque()
    max_in_windows=[]

    for i in range(n):
        while deq and deq[0]<i-k+1:
            deq.popleft()
        while deq and nums[deq[-1]]<=nums[i]:
            deq.pop()

        deq.append(i)

        # The front of the deque is the index of the largest element for the current window
        if i >= k - 1:
            max_in_windows.append(nums[deq[0]])

    return max_in_windows


