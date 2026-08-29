/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
    unordered_map<Node*, Node*> copied;
public:
    Node* copyRandomList(Node* head) {
        Node* og_cursor = head;
        Node* new_prev = nullptr;
        Node* new_curr = nullptr;
        while (og_cursor) {
            new_curr = new Node(og_cursor->val);
            copied[og_cursor] = new_curr;
            if (new_prev) new_prev->next = new_curr;
            new_prev = new_curr;
            og_cursor = og_cursor->next;
        }
        og_cursor = head;
        while (og_cursor) {
            copied[og_cursor]->random = copied[og_cursor->random];
            og_cursor = og_cursor->next;
        }
        return copied[head];
    }
};
