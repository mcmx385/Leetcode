#include <vector>
using namespace std;

vector<vector<int>> flipAndInvertImage(vector<vector<int>> &image)
{
    int rows = image.size();
    for (int i = 0; i < rows; ++i)
    {
        int cols = image[i].size();
        for (int j = 0, k = cols - 1; j <= k; ++j, --k)
        {
            int tmp = image[i][k];
            image[i][k] = !image[i][j];
            image[i][j] = !tmp;
        }
    }
    return image;
}
