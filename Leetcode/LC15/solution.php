<?php
class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function threeSum($nums)
    {
        sort($nums);
        $tmp = [];
        $len = count($nums);
        for ($i = 0; $i < $len - 2; ++$i):
            if ($i == 0 || ($i > 0 && $nums[$i] != $nums[$i - 1])):
                $sum = -$nums[$i];
                $low = $i + 1;
                $high = $len - 1;
                while ($low < $high) {
                    if ($nums[$low] + $nums[$high] == $sum) {
                        $list = [$nums[$i], $nums[$low], $nums[$high]];
                        sort($list);
                        array_push($tmp, $list);
                        while ($low < $high && $nums[$low] == $nums[$low + 1])
                            ++$low;
                        while ($low < $high && $nums[$high] == $nums[$high - 1])
                            --$high;
                        ++$low;
                        --$high;
                    } else if ($nums[$low] + $nums[$high] > $sum) {
                        --$high;
                    } else {
                        ++$low;
                    }
                }
            endif;
        endfor;
        return $tmp;
    }
}
