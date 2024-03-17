<?php

function sequence_sum(int $begin, int $end, int $step): int {
  // May the Force be with you
  $sum = 0;
  for ($i = $begin; $i <= $end; $i+=$step) {
    $sum += $i;
  }
  return $sum;
}

echo sequence_sum(2,6,2);
echo("\n");
