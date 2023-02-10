class Solution
{
public:
    int convertTime(string current, string correct)
    {
        int needed_min = (stoi(correct.substr(0, 2)) - stoi(current.substr(0, 2))) * 60 + (stoi(correct.substr(3, 2)) - stoi(current.substr(3, 2)));
        int needed_sixty = needed_min / 60;
        needed_min -= needed_sixty * 60;
        int needed_fifteen = needed_min / 15;
        needed_min -= needed_fifteen * 15;
        int needed_five = needed_min / 5;
        needed_min -= needed_five * 5;
        int needed_one = needed_min;
        return needed_sixty + needed_fifteen + needed_five + needed_one;
    }
};