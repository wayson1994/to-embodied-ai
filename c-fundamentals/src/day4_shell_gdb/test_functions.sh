#!/bin/bash
source functions.sh
testAdd() { assertEquals "2" "$(add 1 1)"; }
testFactorial() { assertEquals "6" "$(factorial 3)"; }
. /usr/share/shunit2/shunit2
