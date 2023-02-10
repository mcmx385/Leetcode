<?php
class Solution
{
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target)
    {
        $temp = [];
        $count = 0;
        foreach ($nums as $num) :
            $temp = $nums;
            unset($temp[$count]);
            $pos = array_search($target - $num, $temp);
            if ($pos) :
                return [$count, $pos];
            endif;
            $count += 1;
        endforeach;
    }
}
