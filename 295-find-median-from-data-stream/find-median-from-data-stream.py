import heapq

class MedianFinder:

    def __init__(self):
        """
        Initialize two heaps:

        small -> max heap (we store negatives to simulate max heap)
        large -> min heap (normal heap)

        small contains the smaller half of numbers
        large contains the larger half of numbers
        """
        self.small = []  # max heap (store negative numbers)
        self.large = []  # min heap
    
    def addNum(self, num):
        """
        Add a number into our data structure.
        Steps:
        1. Always push into small first (as negative).
        2. Fix ordering if needed.
        3. Balance sizes.
        """

        # Step 1:
        # Push into small heap as negative
        # This makes it behave like a max heap
        heapq.heappush(self.small, -num)

        # Step 2:
        # Ensure ordering rule:
        # All elements in small must be <= elements in large.
        #
        # Since small stores negatives,
        # -self.small[0] gives the largest number in small.
        #
        # If largest in small > smallest in large,
        # we must move that element to large.
        if self.small and self.large and (-self.small[0] > self.large[0]):
            
            # Remove largest from small
            val = -heapq.heappop(self.small)
            
            # Push it into large
            heapq.heappush(self.large, val)

        # Step 3:
        # Balance sizes so difference never exceeds 1.

        # If small has more than 1 extra element
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # If large has more elements
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        Return the median.

        Case 1: Odd total count
                small has one extra element.
                Median = top of small.

        Case 2: Even total count
                Median = average of tops of both heaps.
        """

        # If odd number of elements
        if len(self.small) > len(self.large):
            return -self.small[0]

        # If even number of elements
        return (-self.small[0] + self.large[0]) / 2.0