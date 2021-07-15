def queensAttack(n, k, r, c, obstacles):
    tot_path = 0
    #left_diagonal_before_q
    i_d1 = r
    j_d1 = c
    while i_d1 > 1 and j_d1 > 1:
        i_d1 -= 1
        j_d1 -= 1
        if i_d1 == obstacles[0][0] and j_d1 == obstacles[0][1]:
            break
        tot_path += 1
    #left_diagonal_after_q
    i_d2 = r
    j_d2 = c
    while n > i_d2 and n > j_d2:
        i_d2 += 1
        j_d2 += 1
        if i_d2 == obstacles[0][0] and j_d2 == obstacles[0][1]:
            break
        tot_path += 1
    #right_diagonal_before_q
    i_d3 = r
    j_d3 = c
    while i_d3 > 1 and n > j_d3:
        i_d3 -= 1
        j_d3 += 1
        if i_d3 == obstacles[0][0] and j_d3 == obstacles[0][1]:
            break
        tot_path += 1
    #right_diagonal_after_q
    i_d4 = r
    j_d4 = c
    while n > i_d4 and j_d4 > 1:
        i_d4 += 1
        j_d4 -= 1
        if i_d4 == obstacles[0][0] and j_d4 == obstacles[0][1]:
            break
        tot_path += 1
    #row_check_before_q
    cons_row = r
    i_c1 = c
    while i_c1 > 1:
        i_c1 -= 1
        if cons_row == obstacles[0][0] and i_c1 == obstacles[0][1]:
            break
        tot_path += 1
    #row_check_after_q
    i_c2 = c
    while n > i_c2:
        i_c2 += 1
        if cons_row == obstacles[0][0] and i_c2 == obstacles[0][1]:
            break
        tot_path += 1
    #column_check_before_q
    cons_col = c
    j_r1 = r
    while j_r1 > 1:
        j_r1 -= 1
        if j_r1 == obstacles[0][0] and cons_col == obstacles[0][1]:
            break
        tot_path += 1
    # column_check_before_q
    j_r2 = r
    while n > j_r2:
        j_r2 += 1
        if j_r2 == obstacles[0][0] and cons_col == obstacles[0][1]:
            break
        tot_path += 1
    return tot_path


n = 4
r = 4
c = 4
k = 0
obstacles = [[0, 0]]
result = queensAttack(n, k, r, c, obstacles)
print(result)
