input = """
Before: [3, 0, 0, 1]
0 3 0 2
After:  [3, 0, 1, 1]

Before: [2, 0, 0, 2]
4 0 3 1
After:  [2, 1, 0, 2]

Before: [0, 1, 1, 1]
14 0 0 2
After:  [0, 1, 0, 1]

Before: [3, 0, 1, 1]
11 0 0 3
After:  [3, 0, 1, 1]

Before: [1, 2, 2, 0]
9 0 2 1
After:  [1, 0, 2, 0]

Before: [0, 2, 3, 3]
11 2 2 3
After:  [0, 2, 3, 1]

Before: [2, 0, 1, 2]
4 0 3 2
After:  [2, 0, 1, 2]

Before: [2, 0, 2, 2]
6 3 3 3
After:  [2, 0, 2, 0]

Before: [0, 1, 2, 2]
1 1 2 3
After:  [0, 1, 2, 0]

Before: [0, 3, 0, 0]
14 0 0 0
After:  [0, 3, 0, 0]

Before: [2, 2, 0, 2]
4 0 3 3
After:  [2, 2, 0, 1]

Before: [2, 3, 2, 1]
13 2 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 1, 2]
4 0 3 1
After:  [2, 1, 1, 2]

Before: [1, 2, 2, 1]
9 0 2 0
After:  [0, 2, 2, 1]

Before: [2, 2, 0, 2]
4 0 3 1
After:  [2, 1, 0, 2]

Before: [1, 0, 2, 3]
9 0 2 1
After:  [1, 0, 2, 3]

Before: [1, 1, 3, 2]
10 1 3 1
After:  [1, 0, 3, 2]

Before: [0, 2, 1, 3]
14 0 0 1
After:  [0, 0, 1, 3]

Before: [2, 1, 2, 1]
11 0 0 1
After:  [2, 1, 2, 1]

Before: [1, 1, 2, 2]
3 2 3 1
After:  [1, 2, 2, 2]

Before: [3, 0, 2, 3]
8 1 0 1
After:  [3, 0, 2, 3]

Before: [1, 3, 2, 2]
9 0 2 2
After:  [1, 3, 0, 2]

Before: [2, 0, 3, 2]
4 0 3 2
After:  [2, 0, 1, 2]

Before: [2, 1, 1, 2]
10 1 3 1
After:  [2, 0, 1, 2]

Before: [2, 1, 2, 3]
1 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 1, 2, 1]
1 1 2 3
After:  [3, 1, 2, 0]

Before: [2, 2, 2, 3]
5 2 2 1
After:  [2, 2, 2, 3]

Before: [2, 0, 2, 2]
4 0 3 2
After:  [2, 0, 1, 2]

Before: [2, 3, 1, 1]
11 0 0 0
After:  [1, 3, 1, 1]

Before: [2, 3, 2, 2]
4 0 3 1
After:  [2, 1, 2, 2]

Before: [3, 1, 3, 0]
0 1 0 1
After:  [3, 1, 3, 0]

Before: [3, 1, 2, 3]
12 3 0 3
After:  [3, 1, 2, 1]

Before: [1, 0, 3, 1]
6 3 3 1
After:  [1, 0, 3, 1]

Before: [0, 1, 2, 3]
1 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 2, 1, 3]
2 1 3 1
After:  [1, 0, 1, 3]

Before: [1, 2, 2, 3]
9 0 2 2
After:  [1, 2, 0, 3]

Before: [3, 3, 3, 2]
11 0 2 1
After:  [3, 1, 3, 2]

Before: [2, 1, 0, 2]
10 1 3 3
After:  [2, 1, 0, 0]

Before: [3, 3, 3, 3]
5 3 3 0
After:  [3, 3, 3, 3]

Before: [0, 3, 2, 0]
13 0 0 0
After:  [1, 3, 2, 0]

Before: [3, 0, 2, 2]
3 2 3 3
After:  [3, 0, 2, 2]

Before: [1, 3, 2, 1]
9 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 3]
1 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 1, 0, 2]
15 1 0 1
After:  [1, 1, 0, 2]

Before: [0, 1, 1, 3]
2 2 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 3, 3]
0 3 0 3
After:  [3, 1, 3, 3]

Before: [0, 0, 3, 3]
14 0 0 3
After:  [0, 0, 3, 0]

Before: [2, 1, 2, 2]
1 1 2 2
After:  [2, 1, 0, 2]

Before: [2, 1, 0, 2]
4 0 3 0
After:  [1, 1, 0, 2]

Before: [2, 1, 2, 1]
7 3 2 0
After:  [1, 1, 2, 1]

Before: [3, 1, 2, 2]
10 1 3 2
After:  [3, 1, 0, 2]

Before: [3, 1, 1, 3]
0 1 0 2
After:  [3, 1, 1, 3]

Before: [3, 0, 2, 1]
7 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 2, 0, 2]
4 0 3 0
After:  [1, 2, 0, 2]

Before: [0, 3, 3, 3]
13 3 3 0
After:  [1, 3, 3, 3]

Before: [2, 1, 2, 3]
5 3 3 3
After:  [2, 1, 2, 3]

Before: [1, 1, 2, 1]
7 3 2 0
After:  [1, 1, 2, 1]

Before: [3, 0, 1, 3]
2 2 3 2
After:  [3, 0, 0, 3]

Before: [0, 2, 2, 1]
14 0 0 2
After:  [0, 2, 0, 1]

Before: [0, 3, 3, 1]
14 0 0 2
After:  [0, 3, 0, 1]

Before: [0, 1, 2, 2]
3 2 3 0
After:  [2, 1, 2, 2]

Before: [0, 3, 2, 0]
14 0 0 1
After:  [0, 0, 2, 0]

Before: [0, 1, 2, 2]
10 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 3, 2, 1]
7 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 0, 2, 3]
9 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 3, 2, 2]
6 3 3 0
After:  [0, 3, 2, 2]

Before: [0, 0, 0, 3]
13 3 3 0
After:  [1, 0, 0, 3]

Before: [2, 0, 2, 2]
3 2 3 0
After:  [2, 0, 2, 2]

Before: [0, 0, 2, 2]
3 2 3 3
After:  [0, 0, 2, 2]

Before: [2, 2, 2, 1]
7 3 2 0
After:  [1, 2, 2, 1]

Before: [3, 3, 1, 3]
0 3 0 2
After:  [3, 3, 3, 3]

Before: [1, 1, 1, 1]
15 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 2, 2, 0]
9 0 2 3
After:  [1, 2, 2, 0]

Before: [2, 2, 2, 1]
12 2 0 2
After:  [2, 2, 1, 1]

Before: [2, 1, 2, 2]
1 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 0, 2, 2]
5 2 2 2
After:  [1, 0, 2, 2]

Before: [0, 0, 2, 2]
3 2 3 1
After:  [0, 2, 2, 2]

Before: [0, 1, 0, 2]
10 1 3 1
After:  [0, 0, 0, 2]

Before: [3, 1, 1, 3]
2 2 3 1
After:  [3, 0, 1, 3]

Before: [0, 2, 1, 0]
8 0 1 3
After:  [0, 2, 1, 0]

Before: [1, 1, 3, 3]
2 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 0, 2, 2]
14 0 0 0
After:  [0, 0, 2, 2]

Before: [1, 2, 2, 3]
9 0 2 3
After:  [1, 2, 2, 0]

Before: [2, 2, 1, 3]
5 3 3 1
After:  [2, 3, 1, 3]

Before: [2, 2, 2, 2]
4 0 3 0
After:  [1, 2, 2, 2]

Before: [0, 0, 3, 0]
14 0 0 3
After:  [0, 0, 3, 0]

Before: [3, 2, 2, 0]
12 2 1 1
After:  [3, 1, 2, 0]

Before: [2, 1, 1, 2]
4 0 3 2
After:  [2, 1, 1, 2]

Before: [3, 2, 2, 3]
5 3 3 3
After:  [3, 2, 2, 3]

Before: [3, 2, 2, 2]
3 2 3 0
After:  [2, 2, 2, 2]

Before: [0, 0, 0, 1]
6 3 3 0
After:  [0, 0, 0, 1]

Before: [1, 1, 0, 0]
15 1 0 1
After:  [1, 1, 0, 0]

Before: [0, 0, 1, 1]
14 0 0 2
After:  [0, 0, 0, 1]

Before: [1, 3, 0, 3]
13 3 3 1
After:  [1, 1, 0, 3]

Before: [1, 1, 3, 1]
15 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 1, 2, 1]
5 2 2 2
After:  [1, 1, 2, 1]

Before: [3, 2, 2, 1]
7 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 0]
15 1 0 2
After:  [1, 1, 1, 0]

Before: [0, 0, 3, 0]
11 2 2 0
After:  [1, 0, 3, 0]

Before: [0, 2, 2, 3]
12 2 1 2
After:  [0, 2, 1, 3]

Before: [0, 0, 3, 2]
14 0 0 3
After:  [0, 0, 3, 0]

Before: [1, 3, 2, 3]
13 2 2 2
After:  [1, 3, 1, 3]

Before: [1, 1, 2, 1]
7 3 2 3
After:  [1, 1, 2, 1]

Before: [0, 1, 3, 0]
8 0 1 1
After:  [0, 0, 3, 0]

Before: [1, 0, 2, 2]
9 0 2 0
After:  [0, 0, 2, 2]

Before: [0, 1, 0, 3]
8 0 1 3
After:  [0, 1, 0, 0]

Before: [0, 2, 1, 3]
2 1 3 3
After:  [0, 2, 1, 0]

Before: [2, 3, 2, 3]
11 0 0 0
After:  [1, 3, 2, 3]

Before: [0, 0, 2, 1]
6 3 3 3
After:  [0, 0, 2, 0]

Before: [2, 2, 3, 2]
11 0 0 0
After:  [1, 2, 3, 2]

Before: [3, 1, 2, 1]
7 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 2, 2, 1]
7 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 1, 0, 3]
14 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 1, 2, 1]
9 0 2 3
After:  [1, 1, 2, 0]

Before: [0, 3, 3, 3]
8 0 1 3
After:  [0, 3, 3, 0]

Before: [0, 3, 0, 3]
13 3 3 3
After:  [0, 3, 0, 1]

Before: [0, 2, 2, 3]
8 0 3 0
After:  [0, 2, 2, 3]

Before: [2, 3, 2, 1]
12 2 0 0
After:  [1, 3, 2, 1]

Before: [0, 3, 3, 0]
8 0 1 0
After:  [0, 3, 3, 0]

Before: [1, 1, 1, 2]
10 1 3 3
After:  [1, 1, 1, 0]

Before: [0, 3, 1, 1]
8 0 3 0
After:  [0, 3, 1, 1]

Before: [2, 1, 3, 3]
2 1 3 0
After:  [0, 1, 3, 3]

Before: [1, 1, 2, 3]
1 1 2 2
After:  [1, 1, 0, 3]

Before: [3, 3, 2, 3]
2 2 3 3
After:  [3, 3, 2, 0]

Before: [0, 1, 1, 3]
13 3 2 0
After:  [0, 1, 1, 3]

Before: [0, 2, 0, 2]
13 0 0 1
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 3]
1 1 2 0
After:  [0, 1, 2, 3]

Before: [0, 3, 3, 3]
11 2 2 1
After:  [0, 1, 3, 3]

Before: [0, 2, 3, 2]
8 0 2 3
After:  [0, 2, 3, 0]

Before: [3, 1, 1, 0]
0 1 0 0
After:  [1, 1, 1, 0]

Before: [2, 1, 2, 1]
0 2 0 3
After:  [2, 1, 2, 2]

Before: [0, 1, 2, 3]
13 3 3 1
After:  [0, 1, 2, 3]

Before: [1, 0, 2, 0]
9 0 2 3
After:  [1, 0, 2, 0]

Before: [3, 1, 2, 0]
11 0 0 0
After:  [1, 1, 2, 0]

Before: [0, 2, 1, 0]
14 0 0 1
After:  [0, 0, 1, 0]

Before: [2, 1, 3, 2]
4 0 3 3
After:  [2, 1, 3, 1]

Before: [0, 2, 2, 3]
2 1 3 0
After:  [0, 2, 2, 3]

Before: [2, 3, 3, 1]
11 2 2 1
After:  [2, 1, 3, 1]

Before: [0, 2, 2, 1]
12 2 1 2
After:  [0, 2, 1, 1]

Before: [2, 3, 2, 2]
3 2 3 2
After:  [2, 3, 2, 2]

Before: [2, 3, 3, 2]
4 0 3 0
After:  [1, 3, 3, 2]

Before: [3, 1, 3, 3]
0 3 0 0
After:  [3, 1, 3, 3]

Before: [0, 2, 1, 3]
8 0 3 2
After:  [0, 2, 0, 3]

Before: [2, 1, 2, 2]
3 2 3 3
After:  [2, 1, 2, 2]

Before: [2, 2, 2, 2]
12 2 1 1
After:  [2, 1, 2, 2]

Before: [2, 1, 2, 2]
3 2 3 1
After:  [2, 2, 2, 2]

Before: [3, 0, 3, 3]
0 3 0 2
After:  [3, 0, 3, 3]

Before: [1, 0, 3, 0]
11 2 2 3
After:  [1, 0, 3, 1]

Before: [0, 2, 2, 0]
12 2 1 1
After:  [0, 1, 2, 0]

Before: [1, 1, 0, 0]
15 1 0 2
After:  [1, 1, 1, 0]

Before: [2, 1, 0, 2]
4 0 3 1
After:  [2, 1, 0, 2]

Before: [1, 2, 2, 3]
2 2 3 2
After:  [1, 2, 0, 3]

Before: [3, 1, 2, 3]
2 1 3 1
After:  [3, 0, 2, 3]

Before: [1, 1, 1, 3]
15 1 0 2
After:  [1, 1, 1, 3]

Before: [1, 2, 3, 0]
11 2 2 3
After:  [1, 2, 3, 1]

Before: [1, 1, 0, 2]
15 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 1, 3, 2]
10 1 3 3
After:  [3, 1, 3, 0]

Before: [1, 1, 2, 2]
3 2 3 0
After:  [2, 1, 2, 2]

Before: [2, 1, 2, 1]
1 1 2 1
After:  [2, 0, 2, 1]

Before: [3, 1, 3, 1]
0 1 0 2
After:  [3, 1, 1, 1]

Before: [3, 1, 1, 2]
0 1 0 2
After:  [3, 1, 1, 2]

Before: [1, 3, 3, 1]
12 2 3 2
After:  [1, 3, 0, 1]

Before: [3, 1, 1, 2]
10 1 3 3
After:  [3, 1, 1, 0]

Before: [1, 1, 1, 2]
10 1 3 0
After:  [0, 1, 1, 2]

Before: [0, 1, 0, 2]
8 0 3 3
After:  [0, 1, 0, 0]

Before: [3, 0, 0, 3]
5 3 3 1
After:  [3, 3, 0, 3]

Before: [1, 1, 2, 2]
1 1 2 1
After:  [1, 0, 2, 2]

Before: [0, 0, 1, 1]
6 3 3 3
After:  [0, 0, 1, 0]

Before: [1, 2, 2, 2]
6 3 3 3
After:  [1, 2, 2, 0]

Before: [2, 3, 2, 1]
7 3 2 3
After:  [2, 3, 2, 1]

Before: [3, 3, 1, 1]
11 0 0 0
After:  [1, 3, 1, 1]

Before: [3, 0, 2, 1]
7 3 2 2
After:  [3, 0, 1, 1]

Before: [2, 0, 3, 2]
4 0 3 1
After:  [2, 1, 3, 2]

Before: [2, 3, 2, 1]
5 2 2 1
After:  [2, 2, 2, 1]

Before: [1, 1, 0, 2]
10 1 3 3
After:  [1, 1, 0, 0]

Before: [0, 3, 1, 3]
8 0 2 1
After:  [0, 0, 1, 3]

Before: [2, 0, 1, 2]
4 0 3 1
After:  [2, 1, 1, 2]

Before: [1, 3, 3, 3]
5 3 3 0
After:  [3, 3, 3, 3]

Before: [2, 2, 2, 2]
4 0 3 3
After:  [2, 2, 2, 1]

Before: [3, 1, 2, 0]
1 1 2 1
After:  [3, 0, 2, 0]

Before: [1, 3, 3, 1]
6 3 3 3
After:  [1, 3, 3, 0]

Before: [1, 1, 3, 1]
15 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 1, 1, 1]
15 1 0 1
After:  [1, 1, 1, 1]

Before: [1, 3, 2, 3]
5 3 3 0
After:  [3, 3, 2, 3]

Before: [2, 0, 2, 1]
7 3 2 2
After:  [2, 0, 1, 1]

Before: [0, 1, 1, 2]
10 1 3 2
After:  [0, 1, 0, 2]

Before: [0, 2, 1, 3]
2 2 3 2
After:  [0, 2, 0, 3]

Before: [1, 1, 2, 0]
1 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 0, 1, 3]
2 2 3 2
After:  [1, 0, 0, 3]

Before: [3, 1, 0, 3]
0 3 0 3
After:  [3, 1, 0, 3]

Before: [0, 2, 0, 1]
8 0 3 0
After:  [0, 2, 0, 1]

Before: [3, 1, 1, 0]
11 0 0 1
After:  [3, 1, 1, 0]

Before: [1, 2, 2, 2]
6 3 3 1
After:  [1, 0, 2, 2]

Before: [1, 2, 1, 3]
2 2 3 3
After:  [1, 2, 1, 0]

Before: [0, 3, 3, 2]
14 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 2, 2, 1]
7 3 2 2
After:  [2, 2, 1, 1]

Before: [2, 2, 0, 2]
4 0 3 2
After:  [2, 2, 1, 2]

Before: [0, 1, 1, 3]
8 0 2 1
After:  [0, 0, 1, 3]

Before: [2, 1, 1, 2]
10 1 3 3
After:  [2, 1, 1, 0]

Before: [3, 0, 2, 3]
13 3 2 1
After:  [3, 0, 2, 3]

Before: [0, 3, 2, 1]
14 0 0 3
After:  [0, 3, 2, 0]

Before: [2, 3, 2, 1]
5 2 2 0
After:  [2, 3, 2, 1]

Before: [2, 1, 2, 3]
2 2 3 0
After:  [0, 1, 2, 3]

Before: [0, 1, 3, 2]
10 1 3 1
After:  [0, 0, 3, 2]

Before: [1, 1, 2, 0]
9 0 2 2
After:  [1, 1, 0, 0]

Before: [0, 3, 0, 3]
14 0 0 0
After:  [0, 3, 0, 3]

Before: [0, 2, 0, 3]
2 1 3 0
After:  [0, 2, 0, 3]

Before: [0, 0, 2, 1]
13 2 2 3
After:  [0, 0, 2, 1]

Before: [0, 1, 2, 2]
1 1 2 2
After:  [0, 1, 0, 2]

Before: [3, 1, 3, 3]
2 1 3 3
After:  [3, 1, 3, 0]

Before: [0, 3, 2, 0]
5 2 2 0
After:  [2, 3, 2, 0]

Before: [1, 2, 2, 1]
9 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 3, 2, 3]
2 2 3 3
After:  [1, 3, 2, 0]

Before: [2, 3, 0, 2]
4 0 3 3
After:  [2, 3, 0, 1]

Before: [2, 2, 3, 1]
12 2 3 0
After:  [0, 2, 3, 1]

Before: [0, 1, 2, 2]
13 0 0 1
After:  [0, 1, 2, 2]

Before: [1, 0, 2, 1]
7 3 2 2
After:  [1, 0, 1, 1]

Before: [0, 3, 3, 0]
14 0 0 2
After:  [0, 3, 0, 0]

Before: [3, 0, 3, 1]
11 0 2 0
After:  [1, 0, 3, 1]

Before: [1, 2, 0, 1]
6 3 3 0
After:  [0, 2, 0, 1]

Before: [2, 1, 2, 1]
1 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 3, 2, 3]
0 3 0 0
After:  [3, 3, 2, 3]

Before: [0, 3, 2, 3]
5 3 3 0
After:  [3, 3, 2, 3]

Before: [0, 1, 3, 3]
14 0 0 3
After:  [0, 1, 3, 0]

Before: [0, 0, 3, 1]
13 0 0 1
After:  [0, 1, 3, 1]

Before: [0, 3, 2, 2]
3 2 3 2
After:  [0, 3, 2, 2]

Before: [2, 2, 2, 3]
2 1 3 0
After:  [0, 2, 2, 3]

Before: [2, 2, 2, 3]
12 2 1 0
After:  [1, 2, 2, 3]

Before: [0, 0, 1, 0]
14 0 0 3
After:  [0, 0, 1, 0]

Before: [1, 1, 1, 2]
15 1 0 0
After:  [1, 1, 1, 2]

Before: [2, 0, 2, 1]
7 3 2 0
After:  [1, 0, 2, 1]

Before: [3, 0, 2, 1]
11 0 0 3
After:  [3, 0, 2, 1]

Before: [3, 1, 2, 2]
10 1 3 3
After:  [3, 1, 2, 0]

Before: [0, 1, 2, 3]
13 3 1 0
After:  [0, 1, 2, 3]

Before: [0, 1, 0, 3]
14 0 0 3
After:  [0, 1, 0, 0]

Before: [0, 3, 2, 3]
8 0 2 3
After:  [0, 3, 2, 0]

Before: [1, 3, 2, 2]
9 0 2 0
After:  [0, 3, 2, 2]

Before: [1, 0, 2, 1]
9 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 1, 0, 3]
2 1 3 1
After:  [0, 0, 0, 3]

Before: [0, 0, 2, 3]
14 0 0 0
After:  [0, 0, 2, 3]

Before: [2, 2, 2, 1]
12 2 1 0
After:  [1, 2, 2, 1]

Before: [3, 3, 3, 1]
0 3 0 3
After:  [3, 3, 3, 1]

Before: [3, 3, 0, 1]
0 3 0 1
After:  [3, 1, 0, 1]

Before: [0, 1, 2, 3]
1 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 3, 3, 3]
0 3 0 3
After:  [3, 3, 3, 3]

Before: [1, 0, 2, 2]
3 2 3 1
After:  [1, 2, 2, 2]

Before: [1, 2, 2, 2]
12 2 1 3
After:  [1, 2, 2, 1]

Before: [0, 1, 1, 2]
10 1 3 1
After:  [0, 0, 1, 2]

Before: [1, 0, 2, 2]
9 0 2 2
After:  [1, 0, 0, 2]

Before: [1, 1, 2, 2]
10 1 3 1
After:  [1, 0, 2, 2]

Before: [3, 3, 1, 1]
0 3 0 1
After:  [3, 1, 1, 1]

Before: [2, 1, 2, 2]
12 2 0 0
After:  [1, 1, 2, 2]

Before: [2, 0, 3, 2]
4 0 3 0
After:  [1, 0, 3, 2]

Before: [2, 2, 3, 2]
4 0 3 3
After:  [2, 2, 3, 1]

Before: [2, 3, 3, 3]
13 3 3 2
After:  [2, 3, 1, 3]

Before: [3, 3, 2, 1]
7 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 3, 2, 0]
8 0 2 2
After:  [0, 3, 0, 0]

Before: [0, 1, 3, 2]
13 2 1 1
After:  [0, 0, 3, 2]

Before: [0, 1, 2, 2]
13 0 0 0
After:  [1, 1, 2, 2]

Before: [2, 2, 1, 3]
2 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 1, 1, 0]
15 1 0 1
After:  [1, 1, 1, 0]

Before: [2, 2, 2, 2]
3 2 3 2
After:  [2, 2, 2, 2]

Before: [1, 1, 2, 3]
15 1 0 3
After:  [1, 1, 2, 1]

Before: [2, 0, 3, 2]
4 0 3 3
After:  [2, 0, 3, 1]

Before: [3, 0, 3, 3]
0 3 0 3
After:  [3, 0, 3, 3]

Before: [0, 2, 1, 1]
8 0 2 1
After:  [0, 0, 1, 1]

Before: [1, 3, 2, 0]
5 2 2 3
After:  [1, 3, 2, 2]

Before: [0, 2, 2, 1]
6 3 3 1
After:  [0, 0, 2, 1]

Before: [1, 1, 3, 0]
15 1 0 1
After:  [1, 1, 3, 0]

Before: [2, 0, 1, 3]
5 3 3 0
After:  [3, 0, 1, 3]

Before: [1, 1, 2, 1]
15 1 0 1
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 2]
3 2 3 0
After:  [2, 1, 2, 2]

Before: [1, 1, 3, 2]
15 1 0 3
After:  [1, 1, 3, 1]

Before: [0, 2, 1, 1]
14 0 0 0
After:  [0, 2, 1, 1]

Before: [0, 0, 2, 0]
5 2 2 1
After:  [0, 2, 2, 0]

Before: [0, 1, 2, 3]
2 1 3 2
After:  [0, 1, 0, 3]

Before: [3, 1, 2, 2]
3 2 3 0
After:  [2, 1, 2, 2]

Before: [1, 2, 2, 2]
9 0 2 2
After:  [1, 2, 0, 2]

Before: [2, 2, 2, 1]
5 2 2 1
After:  [2, 2, 2, 1]

Before: [1, 1, 2, 1]
7 3 2 1
After:  [1, 1, 2, 1]

Before: [3, 0, 0, 1]
0 3 0 3
After:  [3, 0, 0, 1]

Before: [3, 2, 3, 3]
12 3 0 3
After:  [3, 2, 3, 1]

Before: [3, 1, 2, 2]
10 1 3 1
After:  [3, 0, 2, 2]

Before: [1, 0, 1, 3]
13 3 2 1
After:  [1, 0, 1, 3]

Before: [0, 0, 0, 2]
14 0 0 1
After:  [0, 0, 0, 2]

Before: [3, 0, 3, 1]
0 3 0 1
After:  [3, 1, 3, 1]

Before: [1, 1, 2, 3]
1 1 2 3
After:  [1, 1, 2, 0]

Before: [3, 1, 2, 1]
1 1 2 1
After:  [3, 0, 2, 1]

Before: [3, 3, 0, 3]
13 3 3 2
After:  [3, 3, 1, 3]

Before: [3, 3, 2, 3]
2 2 3 2
After:  [3, 3, 0, 3]

Before: [1, 2, 2, 1]
9 0 2 2
After:  [1, 2, 0, 1]

Before: [3, 1, 0, 1]
0 3 0 1
After:  [3, 1, 0, 1]

Before: [2, 2, 3, 2]
4 0 3 0
After:  [1, 2, 3, 2]

Before: [2, 0, 2, 1]
7 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 2, 2]
9 0 2 2
After:  [1, 1, 0, 2]

Before: [0, 1, 3, 2]
6 3 3 2
After:  [0, 1, 0, 2]

Before: [3, 3, 0, 2]
6 3 3 3
After:  [3, 3, 0, 0]

Before: [3, 1, 3, 1]
11 0 2 2
After:  [3, 1, 1, 1]

Before: [0, 1, 2, 1]
7 3 2 3
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 1]
7 3 2 1
After:  [1, 1, 2, 1]

Before: [3, 1, 0, 2]
10 1 3 2
After:  [3, 1, 0, 2]

Before: [0, 1, 3, 2]
14 0 0 2
After:  [0, 1, 0, 2]

Before: [0, 3, 0, 2]
14 0 0 1
After:  [0, 0, 0, 2]

Before: [0, 1, 2, 1]
1 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 1]
9 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 2]
10 1 3 2
After:  [0, 1, 0, 2]

Before: [1, 0, 2, 2]
3 2 3 2
After:  [1, 0, 2, 2]

Before: [2, 3, 3, 1]
12 2 3 3
After:  [2, 3, 3, 0]

Before: [2, 0, 3, 1]
12 2 3 0
After:  [0, 0, 3, 1]

Before: [2, 1, 2, 1]
7 3 2 2
After:  [2, 1, 1, 1]

Before: [3, 3, 2, 2]
3 2 3 0
After:  [2, 3, 2, 2]

Before: [0, 1, 0, 1]
8 0 1 1
After:  [0, 0, 0, 1]

Before: [1, 1, 2, 1]
6 3 3 2
After:  [1, 1, 0, 1]

Before: [0, 1, 2, 2]
1 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 3, 1, 3]
2 2 3 2
After:  [3, 3, 0, 3]

Before: [3, 2, 1, 3]
5 3 3 1
After:  [3, 3, 1, 3]

Before: [2, 1, 2, 2]
4 0 3 0
After:  [1, 1, 2, 2]

Before: [3, 3, 2, 2]
13 2 2 2
After:  [3, 3, 1, 2]

Before: [2, 1, 3, 2]
4 0 3 2
After:  [2, 1, 1, 2]

Before: [3, 0, 2, 2]
3 2 3 1
After:  [3, 2, 2, 2]

Before: [2, 0, 1, 2]
4 0 3 3
After:  [2, 0, 1, 1]

Before: [3, 2, 2, 0]
5 2 2 3
After:  [3, 2, 2, 2]

Before: [0, 0, 3, 3]
5 3 3 3
After:  [0, 0, 3, 3]

Before: [0, 1, 0, 3]
13 3 1 0
After:  [0, 1, 0, 3]

Before: [2, 2, 3, 2]
4 0 3 2
After:  [2, 2, 1, 2]

Before: [0, 3, 0, 1]
14 0 0 2
After:  [0, 3, 0, 1]

Before: [3, 3, 3, 0]
11 0 0 2
After:  [3, 3, 1, 0]

Before: [0, 3, 3, 3]
14 0 0 1
After:  [0, 0, 3, 3]

Before: [2, 2, 1, 1]
6 3 3 2
After:  [2, 2, 0, 1]

Before: [3, 2, 0, 3]
5 3 3 0
After:  [3, 2, 0, 3]

Before: [2, 2, 2, 3]
2 1 3 1
After:  [2, 0, 2, 3]

Before: [2, 3, 2, 2]
3 2 3 1
After:  [2, 2, 2, 2]

Before: [0, 1, 2, 1]
7 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 1, 2, 2]
3 2 3 1
After:  [0, 2, 2, 2]

Before: [3, 1, 2, 0]
0 1 0 2
After:  [3, 1, 1, 0]

Before: [2, 2, 2, 0]
0 2 0 1
After:  [2, 2, 2, 0]

Before: [1, 1, 3, 0]
15 1 0 0
After:  [1, 1, 3, 0]

Before: [0, 3, 0, 3]
5 3 3 0
After:  [3, 3, 0, 3]

Before: [3, 3, 3, 3]
0 3 0 0
After:  [3, 3, 3, 3]

Before: [3, 0, 2, 0]
5 2 2 2
After:  [3, 0, 2, 0]

Before: [2, 3, 2, 2]
6 3 3 0
After:  [0, 3, 2, 2]

Before: [1, 0, 2, 3]
9 0 2 0
After:  [0, 0, 2, 3]

Before: [2, 3, 2, 0]
5 2 2 1
After:  [2, 2, 2, 0]

Before: [3, 3, 3, 1]
12 2 3 3
After:  [3, 3, 3, 0]

Before: [1, 1, 1, 3]
2 2 3 2
After:  [1, 1, 0, 3]

Before: [3, 1, 1, 2]
11 0 0 2
After:  [3, 1, 1, 2]

Before: [1, 1, 0, 2]
15 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 1, 1, 1]
15 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 1, 0, 3]
2 1 3 2
After:  [0, 1, 0, 3]

Before: [2, 0, 2, 2]
3 2 3 2
After:  [2, 0, 2, 2]

Before: [0, 3, 3, 3]
11 2 2 3
After:  [0, 3, 3, 1]

Before: [0, 1, 2, 2]
3 2 3 3
After:  [0, 1, 2, 2]

Before: [0, 3, 3, 0]
8 0 1 1
After:  [0, 0, 3, 0]

Before: [3, 1, 3, 2]
10 1 3 1
After:  [3, 0, 3, 2]

Before: [3, 2, 2, 3]
12 2 1 2
After:  [3, 2, 1, 3]

Before: [3, 2, 2, 0]
5 2 2 0
After:  [2, 2, 2, 0]

Before: [3, 1, 1, 2]
10 1 3 1
After:  [3, 0, 1, 2]

Before: [3, 0, 3, 1]
11 0 2 2
After:  [3, 0, 1, 1]

Before: [3, 1, 0, 3]
0 1 0 1
After:  [3, 1, 0, 3]

Before: [0, 1, 2, 1]
7 3 2 2
After:  [0, 1, 1, 1]

Before: [2, 1, 2, 0]
12 2 0 1
After:  [2, 1, 2, 0]

Before: [0, 1, 0, 2]
14 0 0 2
After:  [0, 1, 0, 2]

Before: [2, 3, 2, 1]
0 2 0 3
After:  [2, 3, 2, 2]

Before: [1, 1, 0, 2]
10 1 3 1
After:  [1, 0, 0, 2]

Before: [3, 1, 2, 3]
13 3 3 2
After:  [3, 1, 1, 3]

Before: [2, 3, 2, 3]
0 2 0 1
After:  [2, 2, 2, 3]

Before: [3, 1, 2, 3]
1 1 2 3
After:  [3, 1, 2, 0]

Before: [2, 2, 1, 2]
4 0 3 0
After:  [1, 2, 1, 2]

Before: [0, 0, 3, 1]
14 0 0 0
After:  [0, 0, 3, 1]

Before: [3, 2, 3, 0]
11 0 2 3
After:  [3, 2, 3, 1]

Before: [2, 1, 1, 1]
11 0 0 1
After:  [2, 1, 1, 1]

Before: [3, 2, 2, 2]
12 2 1 2
After:  [3, 2, 1, 2]

Before: [0, 1, 3, 2]
10 1 3 2
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 2]
15 1 0 1
After:  [1, 1, 2, 2]

Before: [0, 0, 3, 3]
8 0 2 3
After:  [0, 0, 3, 0]

Before: [2, 0, 0, 0]
11 0 0 1
After:  [2, 1, 0, 0]

Before: [3, 2, 3, 3]
0 3 0 2
After:  [3, 2, 3, 3]

Before: [2, 2, 2, 2]
4 0 3 2
After:  [2, 2, 1, 2]

Before: [1, 1, 1, 3]
15 1 0 0
After:  [1, 1, 1, 3]

Before: [0, 1, 2, 0]
8 0 1 0
After:  [0, 1, 2, 0]

Before: [3, 1, 3, 1]
12 2 3 0
After:  [0, 1, 3, 1]

Before: [1, 1, 2, 2]
3 2 3 2
After:  [1, 1, 2, 2]

Before: [3, 1, 2, 2]
3 2 3 1
After:  [3, 2, 2, 2]

Before: [1, 1, 0, 1]
15 1 0 0
After:  [1, 1, 0, 1]

Before: [2, 3, 1, 3]
2 2 3 3
After:  [2, 3, 1, 0]

Before: [2, 0, 3, 1]
12 2 3 2
After:  [2, 0, 0, 1]

Before: [2, 0, 0, 3]
8 1 0 0
After:  [0, 0, 0, 3]

Before: [1, 1, 2, 0]
15 1 0 0
After:  [1, 1, 2, 0]

Before: [3, 0, 0, 0]
8 2 0 3
After:  [3, 0, 0, 0]

Before: [2, 0, 2, 2]
0 2 0 3
After:  [2, 0, 2, 2]

Before: [2, 0, 2, 2]
4 0 3 3
After:  [2, 0, 2, 1]

Before: [0, 2, 2, 1]
7 3 2 2
After:  [0, 2, 1, 1]

Before: [2, 2, 0, 1]
6 3 3 1
After:  [2, 0, 0, 1]

Before: [2, 1, 1, 2]
10 1 3 2
After:  [2, 1, 0, 2]

Before: [2, 0, 1, 3]
2 2 3 0
After:  [0, 0, 1, 3]

Before: [2, 0, 0, 2]
4 0 3 3
After:  [2, 0, 0, 1]

Before: [1, 2, 2, 2]
3 2 3 0
After:  [2, 2, 2, 2]

Before: [0, 3, 2, 1]
8 0 1 0
After:  [0, 3, 2, 1]

Before: [0, 2, 2, 3]
8 0 3 2
After:  [0, 2, 0, 3]

Before: [0, 2, 2, 0]
5 2 2 3
After:  [0, 2, 2, 2]

Before: [3, 0, 3, 1]
12 2 3 0
After:  [0, 0, 3, 1]

Before: [0, 2, 1, 3]
2 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 1, 2, 2]
1 1 2 0
After:  [0, 1, 2, 2]

Before: [2, 0, 2, 0]
0 2 0 2
After:  [2, 0, 2, 0]

Before: [0, 1, 3, 2]
10 1 3 3
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 0]
15 1 0 3
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 3]
1 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 3, 1, 3]
2 2 3 3
After:  [1, 3, 1, 0]

Before: [2, 3, 2, 0]
12 2 0 1
After:  [2, 1, 2, 0]

Before: [3, 0, 3, 3]
12 3 0 2
After:  [3, 0, 1, 3]

Before: [3, 1, 1, 3]
2 2 3 0
After:  [0, 1, 1, 3]

Before: [3, 2, 2, 3]
2 1 3 3
After:  [3, 2, 2, 0]

Before: [2, 2, 2, 1]
7 3 2 3
After:  [2, 2, 2, 1]

Before: [1, 1, 1, 1]
6 2 3 3
After:  [1, 1, 1, 0]

Before: [2, 3, 2, 3]
5 2 2 2
After:  [2, 3, 2, 3]

Before: [2, 3, 2, 2]
4 0 3 0
After:  [1, 3, 2, 2]

Before: [0, 1, 2, 1]
13 2 2 2
After:  [0, 1, 1, 1]

Before: [1, 3, 2, 2]
9 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 0, 0, 3]
14 0 0 1
After:  [0, 0, 0, 3]

Before: [0, 2, 0, 0]
14 0 0 2
After:  [0, 2, 0, 0]

Before: [1, 3, 2, 1]
9 0 2 3
After:  [1, 3, 2, 0]

Before: [3, 2, 2, 3]
13 3 2 1
After:  [3, 0, 2, 3]

Before: [1, 0, 2, 0]
9 0 2 0
After:  [0, 0, 2, 0]

Before: [0, 3, 2, 1]
5 2 2 1
After:  [0, 2, 2, 1]

Before: [3, 1, 2, 3]
1 1 2 1
After:  [3, 0, 2, 3]

Before: [0, 3, 1, 2]
14 0 0 2
After:  [0, 3, 0, 2]

Before: [2, 1, 1, 3]
13 3 2 1
After:  [2, 0, 1, 3]

Before: [0, 0, 2, 2]
6 3 3 3
After:  [0, 0, 2, 0]

Before: [0, 1, 3, 0]
8 0 2 0
After:  [0, 1, 3, 0]

Before: [1, 1, 1, 2]
15 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 1, 3, 2]
8 0 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 3, 3]
15 1 0 0
After:  [1, 1, 3, 3]

Before: [2, 2, 1, 2]
11 0 1 0
After:  [1, 2, 1, 2]

Before: [1, 0, 2, 2]
3 2 3 0
After:  [2, 0, 2, 2]

Before: [0, 0, 2, 2]
3 2 3 0
After:  [2, 0, 2, 2]

Before: [2, 2, 2, 2]
3 2 3 0
After:  [2, 2, 2, 2]

Before: [2, 2, 2, 0]
12 2 0 0
After:  [1, 2, 2, 0]

Before: [0, 1, 1, 2]
10 1 3 0
After:  [0, 1, 1, 2]

Before: [0, 0, 0, 2]
14 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 3, 3, 3]
13 3 3 2
After:  [1, 3, 1, 3]

Before: [3, 2, 2, 3]
5 3 3 0
After:  [3, 2, 2, 3]

Before: [1, 1, 3, 1]
15 1 0 1
After:  [1, 1, 3, 1]

Before: [2, 3, 2, 2]
4 0 3 2
After:  [2, 3, 1, 2]

Before: [3, 3, 2, 3]
0 3 0 1
After:  [3, 3, 2, 3]

Before: [1, 1, 2, 0]
9 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 2, 2, 0]
9 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 3, 2, 1]
7 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 0, 2, 3]
5 2 2 0
After:  [2, 0, 2, 3]

Before: [2, 0, 0, 2]
4 0 3 2
After:  [2, 0, 1, 2]

Before: [3, 3, 1, 1]
0 3 0 2
After:  [3, 3, 1, 1]

Before: [0, 3, 3, 0]
14 0 0 1
After:  [0, 0, 3, 0]

Before: [3, 2, 1, 1]
0 3 0 1
After:  [3, 1, 1, 1]

Before: [1, 1, 2, 2]
15 1 0 0
After:  [1, 1, 2, 2]

Before: [2, 2, 1, 2]
6 3 3 0
After:  [0, 2, 1, 2]

Before: [2, 1, 2, 2]
4 0 3 2
After:  [2, 1, 1, 2]

Before: [1, 1, 1, 2]
10 1 3 1
After:  [1, 0, 1, 2]

Before: [1, 1, 0, 0]
15 1 0 0
After:  [1, 1, 0, 0]

Before: [1, 2, 2, 3]
9 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 0, 1, 2]
4 0 3 0
After:  [1, 0, 1, 2]

Before: [1, 3, 3, 3]
12 3 2 3
After:  [1, 3, 3, 1]

Before: [3, 1, 1, 2]
0 1 0 0
After:  [1, 1, 1, 2]

Before: [3, 0, 2, 1]
0 3 0 3
After:  [3, 0, 2, 1]

Before: [3, 3, 0, 1]
0 3 0 0
After:  [1, 3, 0, 1]

Before: [1, 3, 3, 2]
6 3 3 2
After:  [1, 3, 0, 2]

Before: [0, 2, 1, 0]
8 0 2 2
After:  [0, 2, 0, 0]

Before: [2, 2, 2, 0]
12 2 0 2
After:  [2, 2, 1, 0]

Before: [2, 1, 2, 3]
5 2 2 0
After:  [2, 1, 2, 3]

Before: [0, 0, 1, 3]
5 3 3 3
After:  [0, 0, 1, 3]

Before: [1, 0, 2, 3]
13 2 2 2
After:  [1, 0, 1, 3]

Before: [1, 1, 2, 3]
15 1 0 2
After:  [1, 1, 1, 3]

Before: [2, 2, 2, 2]
3 2 3 3
After:  [2, 2, 2, 2]

Before: [1, 1, 0, 1]
15 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 3]
15 1 0 0
After:  [1, 1, 2, 3]

Before: [1, 1, 0, 3]
2 1 3 1
After:  [1, 0, 0, 3]

Before: [2, 0, 2, 1]
12 2 0 1
After:  [2, 1, 2, 1]

Before: [0, 2, 1, 2]
8 0 1 1
After:  [0, 0, 1, 2]

Before: [1, 1, 2, 3]
1 1 2 1
After:  [1, 0, 2, 3]

Before: [0, 3, 2, 3]
2 2 3 0
After:  [0, 3, 2, 3]

Before: [0, 0, 2, 3]
13 3 3 2
After:  [0, 0, 1, 3]

Before: [2, 1, 3, 2]
10 1 3 1
After:  [2, 0, 3, 2]

Before: [1, 1, 2, 3]
2 1 3 3
After:  [1, 1, 2, 0]

Before: [0, 0, 3, 2]
14 0 0 2
After:  [0, 0, 0, 2]

Before: [0, 2, 2, 1]
7 3 2 3
After:  [0, 2, 2, 1]

Before: [1, 0, 3, 2]
11 2 2 3
After:  [1, 0, 3, 1]

Before: [3, 2, 3, 3]
11 0 0 1
After:  [3, 1, 3, 3]

Before: [0, 3, 2, 2]
14 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 2, 1, 1]
6 3 3 2
After:  [3, 2, 0, 1]

Before: [0, 2, 2, 3]
2 2 3 0
After:  [0, 2, 2, 3]

Before: [1, 2, 1, 2]
6 3 3 3
After:  [1, 2, 1, 0]

Before: [2, 1, 2, 1]
7 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 1, 2]
10 1 3 2
After:  [1, 1, 0, 2]

Before: [0, 0, 1, 1]
14 0 0 1
After:  [0, 0, 1, 1]

Before: [3, 3, 3, 1]
11 0 2 1
After:  [3, 1, 3, 1]

Before: [2, 1, 2, 2]
12 2 0 2
After:  [2, 1, 1, 2]

Before: [1, 2, 2, 1]
7 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 2, 2, 2]
9 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 3, 2, 1]
7 3 2 3
After:  [3, 3, 2, 1]

Before: [2, 1, 1, 2]
6 3 3 3
After:  [2, 1, 1, 0]

Before: [2, 2, 1, 3]
2 2 3 2
After:  [2, 2, 0, 3]

Before: [3, 2, 2, 2]
3 2 3 1
After:  [3, 2, 2, 2]

Before: [2, 2, 2, 1]
0 2 0 0
After:  [2, 2, 2, 1]

Before: [0, 1, 3, 1]
14 0 0 1
After:  [0, 0, 3, 1]

Before: [2, 0, 3, 1]
8 1 0 0
After:  [0, 0, 3, 1]

Before: [2, 3, 0, 2]
4 0 3 2
After:  [2, 3, 1, 2]

Before: [2, 0, 2, 2]
3 2 3 1
After:  [2, 2, 2, 2]

Before: [0, 0, 3, 2]
8 0 2 2
After:  [0, 0, 0, 2]

Before: [3, 1, 1, 2]
10 1 3 2
After:  [3, 1, 0, 2]

Before: [3, 2, 2, 1]
7 3 2 2
After:  [3, 2, 1, 1]

Before: [2, 2, 2, 2]
4 0 3 1
After:  [2, 1, 2, 2]

Before: [1, 1, 2, 2]
9 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 0, 2, 2]
5 2 2 1
After:  [3, 2, 2, 2]

Before: [0, 2, 0, 1]
14 0 0 0
After:  [0, 2, 0, 1]

Before: [2, 2, 2, 1]
5 2 2 0
After:  [2, 2, 2, 1]

Before: [2, 1, 2, 3]
1 1 2 1
After:  [2, 0, 2, 3]

Before: [2, 3, 0, 2]
4 0 3 1
After:  [2, 1, 0, 2]

Before: [2, 3, 2, 1]
7 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 0, 2, 2]
12 2 0 0
After:  [1, 0, 2, 2]

Before: [1, 2, 2, 2]
3 2 3 2
After:  [1, 2, 2, 2]

Before: [0, 0, 2, 1]
7 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 2, 3, 3]
11 2 2 3
After:  [2, 2, 3, 1]

Before: [3, 3, 2, 0]
5 2 2 2
After:  [3, 3, 2, 0]

Before: [3, 2, 2, 2]
3 2 3 2
After:  [3, 2, 2, 2]

Before: [2, 3, 2, 2]
4 0 3 3
After:  [2, 3, 2, 1]

Before: [2, 1, 1, 2]
11 0 0 1
After:  [2, 1, 1, 2]

Before: [0, 0, 2, 1]
7 3 2 2
After:  [0, 0, 1, 1]

Before: [0, 2, 1, 0]
14 0 0 3
After:  [0, 2, 1, 0]

Before: [1, 1, 2, 0]
15 1 0 1
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 3]
1 1 2 1
After:  [0, 0, 2, 3]

Before: [0, 3, 1, 0]
14 0 0 3
After:  [0, 3, 1, 0]

Before: [0, 2, 3, 2]
8 0 3 0
After:  [0, 2, 3, 2]

Before: [0, 1, 3, 3]
13 0 0 0
After:  [1, 1, 3, 3]

Before: [2, 1, 2, 0]
1 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 0, 1, 1]
11 0 0 0
After:  [1, 0, 1, 1]

Before: [0, 2, 1, 3]
14 0 0 3
After:  [0, 2, 1, 0]

Before: [0, 2, 2, 1]
14 0 0 0
After:  [0, 2, 2, 1]

Before: [0, 2, 3, 0]
14 0 0 1
After:  [0, 0, 3, 0]

Before: [2, 2, 2, 2]
3 2 3 1
After:  [2, 2, 2, 2]

Before: [3, 0, 2, 1]
7 3 2 3
After:  [3, 0, 2, 1]

Before: [2, 2, 2, 1]
6 3 3 0
After:  [0, 2, 2, 1]

Before: [2, 1, 3, 2]
10 1 3 2
After:  [2, 1, 0, 2]

Before: [2, 1, 2, 2]
5 2 2 3
After:  [2, 1, 2, 2]

Before: [3, 2, 1, 1]
0 3 0 3
After:  [3, 2, 1, 1]

Before: [2, 1, 2, 3]
1 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 3, 2, 0]
0 2 0 1
After:  [2, 2, 2, 0]

Before: [3, 0, 3, 1]
11 0 0 3
After:  [3, 0, 3, 1]

Before: [2, 3, 1, 1]
6 2 3 2
After:  [2, 3, 0, 1]

Before: [2, 0, 3, 2]
11 2 2 0
After:  [1, 0, 3, 2]

Before: [0, 1, 1, 2]
10 1 3 3
After:  [0, 1, 1, 0]

Before: [0, 1, 3, 3]
12 3 2 2
After:  [0, 1, 1, 3]

Before: [0, 1, 1, 2]
14 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 1, 2, 3]
1 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 1, 2, 2]
1 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 0, 1]
14 0 0 3
After:  [0, 1, 0, 0]

Before: [2, 0, 0, 1]
6 3 3 1
After:  [2, 0, 0, 1]

Before: [1, 2, 1, 3]
13 3 2 3
After:  [1, 2, 1, 0]

Before: [2, 1, 2, 1]
6 3 3 3
After:  [2, 1, 2, 0]

Before: [0, 1, 0, 2]
6 3 3 3
After:  [0, 1, 0, 0]

Before: [3, 1, 0, 2]
8 2 0 0
After:  [0, 1, 0, 2]

Before: [1, 1, 3, 3]
12 3 2 0
After:  [1, 1, 3, 3]

Before: [0, 1, 2, 1]
5 2 2 3
After:  [0, 1, 2, 2]

Before: [1, 0, 3, 0]
11 2 2 0
After:  [1, 0, 3, 0]

Before: [3, 3, 2, 1]
5 2 2 0
After:  [2, 3, 2, 1]

Before: [0, 2, 2, 3]
14 0 0 3
After:  [0, 2, 2, 0]

Before: [3, 0, 1, 3]
2 2 3 3
After:  [3, 0, 1, 0]

Before: [2, 3, 3, 2]
4 0 3 3
After:  [2, 3, 3, 1]

Before: [1, 1, 3, 2]
15 1 0 2
After:  [1, 1, 1, 2]

Before: [1, 1, 2, 2]
9 0 2 0
After:  [0, 1, 2, 2]

Before: [2, 1, 2, 2]
10 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 0]
1 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 1, 1, 3]
14 0 0 1
After:  [0, 0, 1, 3]

Before: [1, 1, 2, 3]
13 3 1 0
After:  [0, 1, 2, 3]

Before: [1, 1, 1, 2]
6 3 3 1
After:  [1, 0, 1, 2]

Before: [2, 1, 2, 2]
5 2 2 1
After:  [2, 2, 2, 2]

Before: [0, 2, 2, 0]
14 0 0 0
After:  [0, 2, 2, 0]

Before: [0, 0, 2, 2]
8 0 2 2
After:  [0, 0, 0, 2]

Before: [0, 1, 2, 0]
14 0 0 3
After:  [0, 1, 2, 0]

Before: [1, 3, 2, 2]
9 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 2, 2, 0]
12 2 1 0
After:  [1, 2, 2, 0]

Before: [2, 1, 3, 2]
4 0 3 0
After:  [1, 1, 3, 2]

Before: [0, 1, 2, 1]
1 1 2 1
After:  [0, 0, 2, 1]

Before: [3, 0, 3, 3]
11 0 0 0
After:  [1, 0, 3, 3]

Before: [0, 3, 2, 1]
7 3 2 0
After:  [1, 3, 2, 1]

Before: [3, 1, 1, 3]
12 3 0 0
After:  [1, 1, 1, 3]

Before: [0, 2, 2, 1]
7 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 1, 3, 2]
10 1 3 3
After:  [1, 1, 3, 0]

Before: [1, 1, 2, 1]
1 1 2 1
After:  [1, 0, 2, 1]

Before: [2, 0, 1, 2]
6 3 3 0
After:  [0, 0, 1, 2]

Before: [2, 0, 2, 0]
0 2 0 3
After:  [2, 0, 2, 2]

Before: [0, 2, 3, 3]
13 3 3 0
After:  [1, 2, 3, 3]

Before: [1, 1, 0, 3]
15 1 0 3
After:  [1, 1, 0, 1]

Before: [2, 0, 1, 1]
11 0 0 2
After:  [2, 0, 1, 1]

Before: [2, 3, 0, 2]
6 3 3 2
After:  [2, 3, 0, 2]

Before: [3, 1, 1, 2]
10 1 3 0
After:  [0, 1, 1, 2]

Before: [2, 3, 0, 1]
6 3 3 1
After:  [2, 0, 0, 1]

Before: [3, 1, 2, 1]
1 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 2]
10 1 3 0
After:  [0, 1, 0, 2]

Before: [2, 1, 2, 1]
1 1 2 2
After:  [2, 1, 0, 1]

Before: [2, 1, 0, 2]
10 1 3 2
After:  [2, 1, 0, 2]

Before: [1, 1, 2, 2]
15 1 0 2
After:  [1, 1, 1, 2]

Before: [2, 3, 0, 2]
4 0 3 0
After:  [1, 3, 0, 2]

Before: [1, 1, 2, 1]
1 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 1, 2, 3]
13 3 3 0
After:  [1, 1, 2, 3]

Before: [3, 0, 2, 3]
0 3 0 1
After:  [3, 3, 2, 3]

Before: [0, 1, 2, 1]
1 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 1, 2]
4 0 3 3
After:  [2, 2, 1, 1]

Before: [3, 3, 0, 3]
11 0 0 0
After:  [1, 3, 0, 3]

Before: [3, 3, 2, 2]
3 2 3 1
After:  [3, 2, 2, 2]

Before: [1, 3, 2, 3]
2 2 3 0
After:  [0, 3, 2, 3]

Before: [1, 2, 2, 3]
9 0 2 0
After:  [0, 2, 2, 3]

Before: [2, 1, 2, 0]
1 1 2 2
After:  [2, 1, 0, 0]

Before: [3, 1, 2, 1]
1 1 2 2
After:  [3, 1, 0, 1]

Before: [3, 1, 0, 2]
10 1 3 1
After:  [3, 0, 0, 2]

Before: [3, 0, 3, 1]
12 2 3 2
After:  [3, 0, 0, 1]

Before: [1, 0, 2, 2]
9 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 2, 2, 3]
5 3 3 1
After:  [0, 3, 2, 3]

Before: [2, 0, 2, 1]
12 2 0 2
After:  [2, 0, 1, 1]

Before: [2, 3, 1, 2]
11 0 0 3
After:  [2, 3, 1, 1]

Before: [0, 2, 2, 2]
14 0 0 0
After:  [0, 2, 2, 2]

Before: [1, 0, 3, 0]
11 2 2 2
After:  [1, 0, 1, 0]

Before: [0, 1, 2, 3]
14 0 0 0
After:  [0, 1, 2, 3]

Before: [2, 2, 3, 1]
6 3 3 3
After:  [2, 2, 3, 0]

Before: [1, 1, 2, 2]
10 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 2]
6 3 3 1
After:  [3, 0, 2, 2]

Before: [1, 2, 3, 3]
13 3 1 2
After:  [1, 2, 0, 3]

Before: [1, 2, 1, 3]
2 2 3 2
After:  [1, 2, 0, 3]

Before: [3, 1, 0, 2]
10 1 3 3
After:  [3, 1, 0, 0]

Before: [3, 1, 3, 3]
11 2 2 3
After:  [3, 1, 3, 1]

Before: [2, 2, 1, 2]
11 0 0 2
After:  [2, 2, 1, 2]

Before: [3, 1, 3, 2]
10 1 3 0
After:  [0, 1, 3, 2]

Before: [3, 0, 2, 2]
3 2 3 2
After:  [3, 0, 2, 2]

Before: [1, 1, 0, 3]
2 1 3 0
After:  [0, 1, 0, 3]

Before: [2, 1, 2, 2]
1 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 2, 2, 3]
2 2 3 2
After:  [2, 2, 0, 3]

Before: [3, 0, 2, 1]
7 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 3]
9 0 2 0
After:  [0, 1, 2, 3]

Before: [3, 2, 2, 3]
2 1 3 2
After:  [3, 2, 0, 3]

Before: [2, 1, 2, 2]
4 0 3 1
After:  [2, 1, 2, 2]

Before: [2, 0, 2, 2]
4 0 3 0
After:  [1, 0, 2, 2]

Before: [2, 3, 1, 2]
4 0 3 2
After:  [2, 3, 1, 2]

Before: [0, 2, 1, 0]
8 0 2 3
After:  [0, 2, 1, 0]

Before: [3, 0, 1, 1]
6 2 3 3
After:  [3, 0, 1, 0]

Before: [1, 2, 2, 0]
12 2 1 2
After:  [1, 2, 1, 0]

Before: [1, 3, 2, 1]
9 0 2 2
After:  [1, 3, 0, 1]

Before: [1, 1, 1, 3]
15 1 0 1
After:  [1, 1, 1, 3]

Before: [0, 0, 0, 3]
8 0 3 2
After:  [0, 0, 0, 3]

Before: [3, 1, 2, 0]
1 1 2 2
After:  [3, 1, 0, 0]

Before: [2, 1, 2, 2]
10 1 3 2
After:  [2, 1, 0, 2]

Before: [1, 1, 0, 1]
15 1 0 1
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 0]
13 2 1 0
After:  [0, 1, 3, 0]

Before: [0, 0, 2, 1]
7 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 1, 3, 0]
11 0 0 3
After:  [2, 1, 3, 1]

Before: [3, 1, 3, 0]
0 1 0 3
After:  [3, 1, 3, 1]

Before: [1, 1, 3, 3]
13 2 1 1
After:  [1, 0, 3, 3]

Before: [1, 3, 2, 3]
9 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 3, 1, 3]
8 0 3 1
After:  [0, 0, 1, 3]

Before: [2, 1, 0, 2]
4 0 3 3
After:  [2, 1, 0, 1]

Before: [2, 0, 2, 2]
3 2 3 3
After:  [2, 0, 2, 2]

Before: [2, 3, 1, 0]
11 0 0 0
After:  [1, 3, 1, 0]

Before: [3, 2, 3, 2]
11 0 0 2
After:  [3, 2, 1, 2]

Before: [2, 1, 2, 2]
4 0 3 3
After:  [2, 1, 2, 1]

Before: [3, 0, 3, 3]
5 3 3 1
After:  [3, 3, 3, 3]

Before: [2, 2, 2, 1]
7 3 2 1
After:  [2, 1, 2, 1]

Before: [2, 1, 2, 2]
3 2 3 2
After:  [2, 1, 2, 2]

Before: [1, 1, 2, 1]
7 3 2 2
After:  [1, 1, 1, 1]

Before: [2, 0, 2, 2]
5 2 2 0
After:  [2, 0, 2, 2]

Before: [2, 1, 3, 2]
4 0 3 1
After:  [2, 1, 3, 2]

Before: [0, 2, 2, 2]
3 2 3 3
After:  [0, 2, 2, 2]

Before: [0, 3, 2, 2]
14 0 0 0
After:  [0, 3, 2, 2]

Before: [2, 1, 3, 2]
10 1 3 0
After:  [0, 1, 3, 2]

Before: [3, 1, 2, 1]
7 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 2, 1, 2]
4 0 3 2
After:  [2, 2, 1, 2]

Before: [3, 2, 1, 1]
11 0 0 2
After:  [3, 2, 1, 1]

Before: [0, 3, 3, 1]
13 0 0 1
After:  [0, 1, 3, 1]

Before: [3, 0, 2, 3]
13 3 2 2
After:  [3, 0, 0, 3]

Before: [0, 0, 0, 1]
6 3 3 2
After:  [0, 0, 0, 1]

Before: [2, 3, 1, 2]
4 0 3 1
After:  [2, 1, 1, 2]

Before: [2, 3, 2, 3]
0 2 0 3
After:  [2, 3, 2, 2]

Before: [1, 3, 2, 0]
9 0 2 0
After:  [0, 3, 2, 0]

Before: [0, 1, 0, 2]
6 3 3 0
After:  [0, 1, 0, 2]

Before: [0, 1, 2, 1]
1 1 2 2
After:  [0, 1, 0, 1]

Before: [1, 3, 2, 1]
7 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 3, 2, 1]
8 0 2 1
After:  [0, 0, 2, 1]

Before: [2, 2, 0, 3]
5 3 3 1
After:  [2, 3, 0, 3]

Before: [1, 1, 2, 2]
3 2 3 3
After:  [1, 1, 2, 2]

Before: [0, 0, 3, 2]
11 2 2 1
After:  [0, 1, 3, 2]

Before: [0, 3, 1, 3]
2 2 3 3
After:  [0, 3, 1, 0]

Before: [3, 3, 3, 3]
11 2 0 0
After:  [1, 3, 3, 3]

Before: [2, 0, 0, 2]
4 0 3 0
After:  [1, 0, 0, 2]

Before: [0, 1, 2, 3]
2 2 3 1
After:  [0, 0, 2, 3]

Before: [2, 3, 2, 1]
7 3 2 2
After:  [2, 3, 1, 1]

Before: [3, 1, 2, 2]
10 1 3 0
After:  [0, 1, 2, 2]

Before: [0, 2, 3, 3]
14 0 0 3
After:  [0, 2, 3, 0]

Before: [3, 2, 2, 3]
13 3 1 1
After:  [3, 0, 2, 3]

Before: [1, 1, 2, 2]
9 0 2 3
After:  [1, 1, 2, 0]

Before: [0, 2, 1, 3]
14 0 0 2
After:  [0, 2, 0, 3]

Before: [1, 0, 2, 1]
7 3 2 3
After:  [1, 0, 2, 1]

Before: [0, 3, 2, 1]
7 3 2 3
After:  [0, 3, 2, 1]

Before: [0, 1, 3, 2]
11 2 2 0
After:  [1, 1, 3, 2]

Before: [0, 0, 2, 0]
13 0 0 2
After:  [0, 0, 1, 0]

Before: [3, 1, 1, 3]
11 0 0 2
After:  [3, 1, 1, 3]

Before: [3, 2, 1, 3]
0 3 0 3
After:  [3, 2, 1, 3]

Before: [1, 2, 2, 0]
9 0 2 0
After:  [0, 2, 2, 0]

Before: [3, 0, 0, 3]
0 3 0 0
After:  [3, 0, 0, 3]

Before: [1, 0, 1, 3]
2 2 3 0
After:  [0, 0, 1, 3]

Before: [0, 0, 2, 1]
7 3 2 3
After:  [0, 0, 2, 1]

Before: [1, 1, 2, 2]
15 1 0 3
After:  [1, 1, 2, 1]

Before: [2, 1, 1, 3]
2 1 3 0
After:  [0, 1, 1, 3]

Before: [0, 2, 0, 2]
8 0 3 0
After:  [0, 2, 0, 2]

Before: [3, 1, 0, 3]
0 3 0 0
After:  [3, 1, 0, 3]

Before: [2, 3, 2, 3]
2 2 3 1
After:  [2, 0, 2, 3]

Before: [2, 1, 2, 3]
0 2 0 0
After:  [2, 1, 2, 3]

Before: [2, 0, 2, 3]
8 1 0 3
After:  [2, 0, 2, 0]

Before: [1, 1, 2, 3]
2 2 3 1
After:  [1, 0, 2, 3]

Before: [0, 0, 2, 2]
8 0 3 1
After:  [0, 0, 2, 2]

Before: [1, 0, 2, 1]
7 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 3, 2, 3]
9 0 2 2
After:  [1, 3, 0, 3]

Before: [1, 1, 3, 3]
11 2 2 1
After:  [1, 1, 3, 3]

Before: [1, 1, 0, 3]
15 1 0 1
After:  [1, 1, 0, 3]

Before: [2, 3, 3, 2]
4 0 3 1
After:  [2, 1, 3, 2]

Before: [2, 1, 0, 1]
6 3 3 0
After:  [0, 1, 0, 1]

Before: [1, 1, 2, 2]
10 1 3 2
After:  [1, 1, 0, 2]

Before: [2, 0, 2, 1]
7 3 2 3
After:  [2, 0, 2, 1]

Before: [2, 3, 2, 2]
13 2 2 3
After:  [2, 3, 2, 1]

Before: [0, 1, 1, 0]
14 0 0 0
After:  [0, 1, 1, 0]

Before: [0, 1, 3, 2]
14 0 0 1
After:  [0, 0, 3, 2]

Before: [0, 3, 2, 3]
8 0 1 2
After:  [0, 3, 0, 3]

Before: [2, 3, 1, 3]
2 2 3 0
After:  [0, 3, 1, 3]

Before: [0, 0, 1, 1]
8 0 2 0
After:  [0, 0, 1, 1]

Before: [0, 1, 0, 2]
10 1 3 0
After:  [0, 1, 0, 2]

Before: [2, 3, 3, 3]
5 3 3 3
After:  [2, 3, 3, 3]

Before: [0, 3, 2, 1]
7 3 2 2
After:  [0, 3, 1, 1]

Before: [1, 0, 2, 3]
2 2 3 1
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 1]
7 3 2 3
After:  [2, 1, 2, 1]

Before: [3, 1, 1, 1]
0 1 0 0
After:  [1, 1, 1, 1]

Before: [2, 3, 0, 3]
5 3 3 3
After:  [2, 3, 0, 3]

Before: [2, 0, 2, 0]
13 2 2 0
After:  [1, 0, 2, 0]

Before: [3, 2, 2, 3]
13 3 2 2
After:  [3, 2, 0, 3]

Before: [2, 0, 2, 1]
0 2 0 2
After:  [2, 0, 2, 1]

Before: [3, 1, 2, 0]
1 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 2, 2, 1]
9 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 0, 1, 1]
0 3 0 0
After:  [1, 0, 1, 1]

Before: [3, 1, 3, 3]
0 1 0 2
After:  [3, 1, 1, 3]

Before: [0, 1, 1, 3]
2 1 3 1
After:  [0, 0, 1, 3]

Before: [0, 3, 3, 3]
5 3 3 1
After:  [0, 3, 3, 3]

Before: [3, 3, 2, 2]
13 2 2 3
After:  [3, 3, 2, 1]

Before: [1, 1, 2, 1]
1 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 3, 2]
15 1 0 0
After:  [1, 1, 3, 2]

Before: [1, 0, 2, 2]
5 2 2 1
After:  [1, 2, 2, 2]

Before: [2, 2, 1, 1]
11 0 1 1
After:  [2, 1, 1, 1]

Before: [0, 0, 3, 1]
14 0 0 1
After:  [0, 0, 3, 1]

Before: [2, 1, 2, 2]
10 1 3 1
After:  [2, 0, 2, 2]

Before: [0, 1, 0, 2]
10 1 3 3
After:  [0, 1, 0, 0]

Before: [3, 1, 2, 2]
1 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 0, 2, 1]
9 0 2 3
After:  [1, 0, 2, 0]

Before: [2, 1, 2, 2]
1 1 2 1
After:  [2, 0, 2, 2]

Before: [2, 3, 1, 2]
4 0 3 0
After:  [1, 3, 1, 2]

Before: [2, 1, 3, 3]
5 3 3 3
After:  [2, 1, 3, 3]

Before: [2, 2, 3, 3]
2 1 3 0
After:  [0, 2, 3, 3]

Before: [1, 1, 3, 2]
15 1 0 1
After:  [1, 1, 3, 2]

Before: [2, 3, 2, 1]
7 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 0, 2, 0]
9 0 2 2
After:  [1, 0, 0, 0]

Before: [3, 3, 2, 3]
5 2 2 1
After:  [3, 2, 2, 3]

Before: [3, 1, 2, 2]
1 1 2 1
After:  [3, 0, 2, 2]

Before: [0, 0, 2, 3]
2 2 3 3
After:  [0, 0, 2, 0]

Before: [3, 3, 1, 3]
2 2 3 0
After:  [0, 3, 1, 3]

Before: [2, 2, 2, 3]
0 2 0 1
After:  [2, 2, 2, 3]

Before: [3, 1, 2, 1]
0 1 0 2
After:  [3, 1, 1, 1]

Before: [3, 3, 2, 1]
7 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 1, 2, 0]
1 1 2 2
After:  [0, 1, 0, 0]

Before: [0, 0, 1, 0]
14 0 0 0
After:  [0, 0, 1, 0]

Before: [0, 2, 2, 1]
12 2 1 3
After:  [0, 2, 2, 1]

Before: [3, 2, 3, 1]
6 3 3 3
After:  [3, 2, 3, 0]

Before: [1, 1, 2, 1]
1 1 2 2
After:  [1, 1, 0, 1]

Before: [2, 3, 1, 2]
4 0 3 3
After:  [2, 3, 1, 1]

Before: [2, 2, 1, 2]
4 0 3 1
After:  [2, 1, 1, 2]

Before: [2, 1, 1, 2]
4 0 3 0
After:  [1, 1, 1, 2]
"""

import re

input = input.split("\n")
input = list(filter(None, input))
units = []

def do_operation(reg, op):
    out = [j for j in reg]
    if op[0] == 0:
        out[op[3]] = reg[op[1]] + reg[op[2]]
    elif op[0] == 1:
        out[op[3]] = reg[op[1]] + op[2]
    elif op[0] == 2:
        out[op[3]] = reg[op[1]] * reg[op[2]]
    elif op[0] == 3:
        out[op[3]] = reg[op[1]] * op[2]
    elif op[0] == 4:
        out[op[3]] = reg[op[1]] & reg[op[2]]
    elif op[0] == 5:
        out[op[3]] = reg[op[1]] & op[2]
    elif op[0] == 6:
        out[op[3]] = reg[op[1]] | reg[op[2]]
    elif op[0] == 7:
        out[op[3]] = reg[op[1]] | op[2]
    elif op[0] == 8:
        out[op[3]] = reg[op[1]]
    elif op[0] == 9:
        out[op[3]] = op[1]
    elif op[0] == 10:
        out[op[3]] = 1 if op[1] > reg[op[2]] else 0
    elif op[0] == 11:
        out[op[3]] = 1 if reg[op[1]] > op[2] else 0
    elif op[0] == 12:
        out[op[3]] = 1 if reg[op[1]] > reg[op[2]] else 0
    elif op[0] == 13:
        out[op[3]] = 1 if op[1] == reg[op[2]] else 0
    elif op[0] == 14:
        out[op[3]] = 1 if reg[op[1]] == op[2] else 0
    elif op[0] == 15:
        out[op[3]] = 1 if reg[op[1]] == reg[op[2]] else 0
    
    return out
"""
addr (add register) stores into register C the result of adding register A and register B.
addi (add immediate) stores into register C the result of adding register A and value B.
Multiplication:

mulr (multiply register) stores into register C the result of multiplying register A and register B.
muli (multiply immediate) stores into register C the result of multiplying register A and value B.
Bitwise AND:

banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
Bitwise OR:

borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
Assignment:

setr (set register) copies the contents of register A into register C. (Input B is ignored.)
seti (set immediate) stores value A into register C. (Input B is ignored.)
Greater-than testing:

gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
Equality testing:

eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
"""

def change_opcode(reg, op, code):
    op[0] = code
    return do_operation(reg, op)

input_ = []
for i in range(len(input))[::3]:
    i1 = [int(j) for j in re.sub(r'[^0-9,]', '', input[i]).split(",")]
    i2 = [int(j) for j in re.sub(r'[^0-9 ]', '', input[i+1]).split(" ")]
    i3 = [int(j) for j in re.sub(r'[^0-9,]', '', input[i+2]).split(",")]
    input_.append([
        i1, i2, i3
    ])
input = input_

def main():
    global input
    
    three = 0
    for i in input:
        correct = 0
        for j in range(16):
            if change_opcode(i[0], i[1], j) == i[2]:
                correct += 1
        if correct >= 3:
            three += 1
    print(three)

main()