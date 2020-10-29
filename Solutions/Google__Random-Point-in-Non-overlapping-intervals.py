Given a list of non-overlapping intervals, generate a number that is drawn uniformly from one of the intervals.

Similar with random pick with weight, here we use number of points in the interval as weight.
Firslty, create a weight list w, where w[i] is the number of points in the interval. 
Secondly, use a prefix_sum list to store the prefix_sum of the weight list.
Then generate a rand_int and use binary search to find which rectangle the rand_int belongs to. 
