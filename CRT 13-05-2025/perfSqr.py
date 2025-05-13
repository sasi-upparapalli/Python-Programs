'''The garments company Apparel wishes to open outlets at
various locations. The company shortlisted several plots in
these locations and wishes to select only plots that are
square- shaped. Write an algorithm to help Apparel find the
number of plots that it can select for its outlets.
Input format:
The first line of the input consists of an integer numOfMots,
representing the number of plots shortlisted by the company
for outlets (N). The second line consists of N space-separated
integers - areal, areal, ..... , areaN representing the area of the
N plots selected for outlets.
Output format:
Print an integer representing the number of plots that will be
selected for outlets.


Sample input
8
79 77 54 81 48 34 25 16
Sample output
3'''

h=int (input())
x=list(map(int, input().split()))
c=0
for i in range(len(x)):
  s=x[i]
  z=s ** 0.5
if int(z)*int(z) == s:
  c=c+1
print(c)
