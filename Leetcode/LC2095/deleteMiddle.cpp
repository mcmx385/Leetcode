#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int countNode(ListNode *head)
{
    int count = 0;
    while (head != nullptr)
    {
        ++count;
        head = head->next;
    }
    return count;
}

int calcMiddle(int total)
{
    return total / 2 + 1;
}

ListNode *goNode(ListNode *head, int position)
{
    for (int i = 0; i < position - 1; ++i)
    {
        head = head->next;
    }
    return head;
}

ListNode *deleteMiddle(ListNode *head)
{
    int total = countNode(head);
    int position = calcMiddle(total);
    cout << "position: " << position << endl;
    ListNode *curr = goNode(head, position - 1);
    if (curr->next == nullptr)
    {
        delete head;
        return nullptr;
    }
    if (curr->next->next != nullptr)
    {
        ListNode *next = curr->next->next;
        delete curr->next;
        curr->next = next;
    }
    else
    {
        delete curr->next;
        curr->next = nullptr;
    }
    return head;
}

int main()
{
    ListNode *head = new ListNode(1);
    ListNode *temp = head;
    for (int i = 2; i <= 7; ++i)
    {
        temp->next = new ListNode(i);
        temp = temp->next;
    }
    int total = countNode(head);
    cout << "Total: " << total << endl;
    int middle = calcMiddle(total);
    cout << "Middle: " << middle << endl;
    return 0;
}