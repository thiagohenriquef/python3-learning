def first_sum(a):
    def second_sum(b):
        return a + b
    return second_sum


print(first_sum(2))
print(first_sum(2)(2))
print(first_sum)