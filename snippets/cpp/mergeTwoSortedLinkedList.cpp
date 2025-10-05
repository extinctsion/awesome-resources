// C++ program to merge two sorted linked lists
#include <bits/stdc++.h>
using namespace std;
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    if (l1->val < l2->val) {
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    } else {
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }
}
// Function to print and clean up the linked list
void printAndCleanup(ListNode* head) {
    cout << "Merged Linked List: ";
    while (head) {
        cout << head->val << " ";
        ListNode* temp = head;
        head = head->next;
        delete temp;  // Clean up memory
    }
    cout << endl;
}

int main() {
    // Example usage:
    ListNode* l1 = new ListNode(1);
    l1->next = new ListNode(3);
    l1->next->next = new ListNode(5);
    
    ListNode* l2 = new ListNode(2);
    l2->next = new ListNode(4);
    l2->next->next = new ListNode(6);
    
    ListNode* mergedList = mergeTwoLists(l1, l2);
    printAndCleanup(mergedList);
    
    return 0;
}