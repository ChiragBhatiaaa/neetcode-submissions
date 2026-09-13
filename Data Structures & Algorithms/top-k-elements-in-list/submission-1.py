class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for i in nums: 
            freq[i] = 1 + freq.get(i, 0)

        heap = []
        for num, freq in freq.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return[num for freq,num in heap]

