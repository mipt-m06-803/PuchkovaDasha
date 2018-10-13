k = str(input())
n = str(input())
def skpr(k, n):
      k1 = k.split(" ")
      n1 = n.split(" ")
      return sum([k1[i] * n1[i] for i in range(len(k1))])


