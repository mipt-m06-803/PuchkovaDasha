k = str(input())
n = str(input())
k1 = k.split(" ")
n1 = n.split(" ")
def skpr(k, n):
      return sum([k1[i] * n1[i] for i in range(len(k1))])


