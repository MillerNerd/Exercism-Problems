def saddle_points(matrix):
    print(matrix)
    for row in matrix:
        for col in row:
            if col == max(row):
                print(col)
    pass
