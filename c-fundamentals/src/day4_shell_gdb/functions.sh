#!/bin/bash
add() {
  echo $(( $1 + $2 ))
}
factorial() {
  local n=$1
  (( n <= 1 )) && echo 1 || echo $(( n * $(factorial $((n-1))) ))
}