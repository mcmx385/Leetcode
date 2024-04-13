<?php
class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target)
    {
        if ($pos = array_search($target, $nums)):
            return $pos;
        else:
            for ($i = 0; $i < count($nums); $i++):
                if ($nums[$i] >= $target):
                    return $i;
                endif;
            endfor;
            return $i;
        endif;
    }
}
