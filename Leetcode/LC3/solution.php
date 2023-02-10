<?php
class Solution
{

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s)
    {
        $ss = "";
        $max_count = 0;
        for ($i = 0; $i < strlen($s); $i++) : // for each el
            $ss = substr($s, $i, strlen($s) - $i); // tmp substr
            $max_count = ($max_count == 0) ? 1 : $max_count; // el exists
            $tmp = ""; // init tmp
            for ($j = 0; $j < strlen($ss); $j++) : // for each remain el
                $char = $ss[$j]; // each char
                if (strpos($tmp, $char) === false) : // not in tmp
                    $tmp .= $char; // add to tmp
                    $count = strlen($tmp); // count is tmp len
                    if ($count > $max_count) : // update max count
                        $max_count = $count;
                    endif;
                else : // in tmp
                    break;
                endif;
            endfor;
            $substr = substr($ss, $j);
            if (strpos($tmp, $substr) !== false) :
                break;
            endif;
        endfor;
        return $max_count;
    }
}
