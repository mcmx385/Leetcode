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
    ListNode* swapPairs(ListNode* head) {
        ListNode* prev, *curr=head, *second, *third;
        
        if(curr!=nullptr && curr->next!=nullptr){
            second=curr->next;
            third=curr->next->next;
            prev=curr;

            second->next=curr;
            curr->next=third;
            
            head=second;
            curr=third;
        }
        
        while(curr!=nullptr && curr->next!=nullptr){
            second=curr->next;
            third=curr->next->next;
            
            second->next=curr;
            curr->next=third;
            prev->next=second;
            
            prev=curr;
            curr=third;
        }
        
        return head;
    }
};