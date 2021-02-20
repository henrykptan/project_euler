// By starting at the top of the triangle below and moving to adjacent numbers on the row below,
// the maximum total from top to bottom is 23.
//
//					3
//				7 		4
//			2		4		6
//		8 		5 		9 		3
//
// That is, 3 + 7 + 4 + 9 = 23.
//
// Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text
// file containing a triangle with one-hundred rows.
// - Starting from the bottom row n, for each pair of nums in row n below a num in row n-1, take the max and add that
// to the num in row n-1
// - Then repeat, until you get to the top
// - The remaining number is the max sum

package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func nilCheck(e error) {
	if e != nil {
		panic(e)
	}
}

func getMaxInt(int1 int, int2 int) int {
	if int1 >= int2 {
		return int1
	} else {
		return int2
	}
}

func readFile() [][]int {
	dat, err := ioutil.ReadFile("p067_triangle")
	nilCheck(err)

	var intListLines [][]int
	for _, line := range strings.Split(string(dat), "\r\n") {
		var intListLine []int
		for _, num := range strings.Split(line, " ") {
			i, err := strconv.Atoi(num)
			nilCheck(err)
			intListLine = append(intListLine, i)
		}
		intListLines = append(intListLines, intListLine)
	}
	return intListLines
}

func mergeConsecutiveRows(rowAbove []int, rowBelow []int) []int {
	var outputRowAbove []int
	for index, num := range rowAbove {
		maxNumBelow := getMaxInt(rowBelow[index], rowBelow[index+1])
		outputRowAbove = append(outputRowAbove, num + maxNumBelow)
	}
	return outputRowAbove
}

func main() {
	triangleRows := readFile()
	numberOfRows := len(triangleRows)
	maxSumRow := triangleRows[numberOfRows - 1]

	for i := numberOfRows-1; i >= 1; i-- {
		maxSumRow = mergeConsecutiveRows(triangleRows[i-1], maxSumRow)
	}
	fmt.Println(maxSumRow)
}
