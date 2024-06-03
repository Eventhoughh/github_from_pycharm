class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        l3 = head
        while l1 and l2:
            if l1.val < l2.val:
                # 重点： 时刻保持下一个 .next 结构是一个 ListNode
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        if l1 == None:
            while l2:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        else:
            while l1:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
        return head.next

if __name__ == "__main__":
    s = Solution()
    #输入：    1->2->4
    #          1->3->4
    # 输出：1->1->2->3->4->4
    l1 = ListNode(1)
    tmp = ListNode(2)
    l1.next = tmp
    tmp.next = ListNode(4)
    l2 = ListNode(1)
    tmp = ListNode(3)
    l2.next = tmp
    tmp.next = ListNode(4)
    r = s.mergeTwoLists(l1,l2)
    print(r.val)
    # 先判断是否为 None ， 再去打印
    while r.next != None:
        r = r.next
        print(r.val)
# 迭代初始：建立头指针FNode，和一个前向指针pre初始指向FNode。
# 迭代开始：将pre.next指向两链表中值小的节点上，pre前移。
# 迭代结束：定有一方链表指针为None，将pre.next指向将另一方当前节点上。返回FNode.next
# 特殊情况：一开始两链表均为None，返回值也是None，满足条件。
# ————————————————