#include <iostream>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
};
int pow(int a, int b)
{
    int res = a;
    for (int i = 0; i < b - 1; ++i, res *= a)
        ;
    return res;
}
ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
{
    int num1 = 0, num2 = 0, count = 0;
    ListNode *tmp1 = l1, *tmp2 = l2;
    while (tmp1 != nullptr && tmp2 != nullptr)
    {
        num1 += tmp1->val * pow(10, count);
        num2 += tmp2->val * pow(10, count);
        ++count;
        tmp1 = tmp1->next;
        tmp2 = tmp2->next;
    }
    int num3 = num1 + num2;
    ListNode *l3 = new ListNode(num3 % 10);
    num3 /= 10;
    ListNode *tmp3 = l3;
    while (num3 > 0)
    {
        ListNode *tmp = new ListNode(num3 % 10);
        tmp3->next = tmp;
        tmp3 = tmp3->next;
        num3 /= 10;
    }
    return l3;
}
int main()
{
    ListNode *l1, *l2;
    ListNode *result = addTwoNumbers(l1, l2);
}