'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

test_cases = [([4,2,8], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]), ([1,4,2,6],[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]), ([1,4,2,6,8], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])]

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, head):
            if not head:
                return True
            if not node:
                return False

            if node.val == head.val:
                return dfs(node.left, head.next) or dfs (node.right, head.next)
            return False
        if not root:
            return False
        return dfs(root,head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)