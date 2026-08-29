/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = 0;
        ListNode* node = head;
        while (node) {
            size++;
            node = node->next;
        }

        int index = size - n;
        if (!index) {
            ListNode* next = head->next;
            delete head;
            return next;
        }

        node = head;
        for (int i = 0; i < index - 1; ++i) {
            node = node->next;
        }

        ListNode* del = node->next;
        node->next = node->next->next;
        delete del;
        return head;
    }
};
