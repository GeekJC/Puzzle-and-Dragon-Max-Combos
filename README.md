# Puzzle-and-Dragon-Max-Combos
An exercise trying to find the max. combos on 6*5 grid

Given a 6 * 5 grid G that every index contains a random element from 6 different type (say A,B,C,D,E,F), there will be N waves to destroy the elements, until no more elements can be destroyed. 

The elements can only be destroyed when there appears with 3 or more consecutive elements from same type horizontally or vertically. Matches with more than 3 elements that in same type will be considered as 1 combo. For instance, a 2 x 3 clearance / a horizontal column of 3 and a vertical row of 3 that are connected by an element in the middle, will be considered as 1 combo. The system will scan through the grid from (0,0) to (4,5) on row-first basis, i.e. (0,0) -> (0,1) -> (0,2) -> …  -> (0,5) -> (1,0) -> (1,1) -> … -> (4,5) for 1 wave. After each wave, the remaining elements will be dropped vertically and start the next wave, no elements will be filled after each wave. 

With given G, player can rearrange the elements with any possible arrangement for initial round, but the total number of each element types must remain the same after the arrangement. 

Example flow, 

1. 0 combos
AAACDF
BDCCEF
BDEEEE
BBBCDF
CDAAAF

2. 4 combos
AAACDF
BDCCEF
BDEEEE
BBBCDF
CDAAAF

XXXXXX
XXXXXF
XDXCDF
XDXCEF
CDCCDF

3. 4 + 3, 7 combos total

XXXXXX
XXXXXF
XDXCDF
XDXCEF
CDCCDF

XXXXXX
XXXXXX
XXXXDX
XXXXEX
CXCXDX

The goal is to find the best initial arrangement in order to get highest possible number of combos with either approach from below:

	1. Design an algorithm to find the arrangement .
	2. Use Machine Learning to train the model to find the arrangement.

*Reference: http://pad.wikia.com/wiki/Game_Mechanics


Analyzing the problem:

With above requirements, we can easily found that the max. combos for each grid will only be 10. Because the will only be 6 * 5 = 30 of elements, and in most ideal case we can destroy the elements with 3 consecutive elements, which is equal to 30 / 3 = 10. 

From here we can further simplify the problem. Given that we can relocate the elements with any arrangement we want, the initial arrangement can’t provide useful information for us now. All we need to know is the number of different elements. Take above pattern as an example, we can simplify it to a 1-D array A: {6, 5, 5, 5, 5, 4}, which equals to the total numbers of the array {A, B, C, D, E, F}. Since there are no possible ways to achieve higher combos with insufficient elements, we can simply find the sum of A % 3, which is 2 + 1 + 1 + 1 + 1 + 1 = 7 in this case. 

Note that above algorithm is only suitable when it happens to be a relatively even distribution. When a single element has a total number = 15, it reaches its maximum combos, which is 5. See below as an example,

AXAXAA
AXAXAA
AXAXAA
XXXXXX
AAAXXX

When we try to add A on the into the grid, it will not increase the no, of combos but with a possibility to connect the matches and hence reduce the number of combos. 

When number of A >= 21, there will only be 9 or less free spaces for us to insert the A, that will not be possible to not connect any existing matches. Therefore, starting from A = 21, the combos will decrease with the rise of number of A.

Number of A = 20, example grid:

AXAXAA
AXAXAA
AXAXAA
XAXAXX
AAAAAA


