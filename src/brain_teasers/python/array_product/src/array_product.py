

def array_product(arr:list[int]) -> list[int]:
    

    new_arr:list[int] = list(arr)
    size:int = len(arr)
    for i in range(size):
        product:int = 1
        for j in range(size):
            if i != j:
                product  *= arr[j]
        new_arr[i] = product

    return new_arr



input_array = [6]

print(array_product(input_array))
print(input_array)