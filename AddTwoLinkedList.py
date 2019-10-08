# Time:  O(n)
# Space: O(1)

# Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1l1 and l2l2. Since each digit is in the range of 0 \ldots 90…9, summing two digits may "overflow". For example 5 + 7 = 125+7=12. In this case, we set the current digit to 22 and bring over the carry = 1carry=1 to the next iteration. carrycarry must be either 00 or 11 because the largest possible sum of two digits (including the carry) is 9 + 9 + 1 = 199+9+1=19.

# The pseudocode is as following:

# Initialize current node to dummy head of the returning list.
# Initialize carry to 00.
# Initialize pp and qq to head of l1l1 and l2l2 respectively.
# Loop through lists l1l1 and l2l2 until you reach both ends.
# Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
# Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
# Set sum = x + y + carrysum=x+y+carry.
# Update carry = sum / 10carry=sum/10.
# Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
# Advance both pp and qq.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
