class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

        # Bubble sort
        for i in range(n+m):
            swapped = False

            for j in range(0, (n+m)-i-1):
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
                    swapped = True

            if swapped == False:
                break


if __name__ == "__main__":
    solution = Solution()
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    nums1 = [1,2,4,5,6,0]
    m = 5
    nums2 = [3]
    n = 1
    solution.merge(nums1, m, nums2, n)    