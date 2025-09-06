def generate_pascals_triangle(n):
    result = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(1, i):
            temp.append(result[i-1][j-1] + result[i-1][j])
        temp.append(1)
        result.append(temp)
    return result

# Example usage
num_rows = 5
pascals_triangle = generate_pascals_triangle(num_rows)
for row in pascals_triangle:
    print(row)
