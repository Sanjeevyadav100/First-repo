vec1 = list(map(int, input("enter first vector :").split()))
vec2 = list(map(int, input("enter second vector: ").split()))

dot_product = sum(x*y for x,y in zip(vec1,vec2))

print("dot product --> ",dot_product)
