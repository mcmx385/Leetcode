<?php
class Solution
{

    /**
     * @param String[][] $board
     * @return Boolean
     */
    function isValidSudoku($board)
    {
        for ($i = 0; $i < 9; $i++) : // col
            $col = array_column($board, $i);
            while (($pos = array_search(".", $col)) !== false) :
                unset($col[$pos]);
            endwhile;
            if (count($col) !== count(array_unique($col))) :
                return false;
            endif;
        endfor;
        for ($i = 0; $i < 9; $i++) : // row
            $row = $board[$i];
            while (($pos = array_search(".", $row)) !== false) :
                unset($row[$pos]);
            endwhile;
            if (count($row) !== count(array_unique($row))) :
                return false;
            endif;
        endfor;
        for ($i = 0; $i < 9; $i += 3) :
            for ($j = 0; $j < 9; $j += 3) :
                $tmp = [];
                $tmp[0] = $board[$i][$j];
                $tmp[1] = $board[$i + 1][$j];
                $tmp[2] = $board[$i + 2][$j];
                $tmp[3] = $board[$i][$j + 1];
                $tmp[4] = $board[$i + 1][$j + 1];
                $tmp[5] = $board[$i + 2][$j + 1];
                $tmp[6] = $board[$i][$j + 2];
                $tmp[7] = $board[$i + 1][$j + 2];
                $tmp[8] = $board[$i + 2][$j + 2];
                while (($pos = array_search(".", $tmp)) !== false) :
                    unset($tmp[$pos]);
                endwhile;
                if (count($tmp) !== count(array_unique($tmp))) :
                    return false;
                endif;
            endfor;
        endfor;
        return true;
    }
}
