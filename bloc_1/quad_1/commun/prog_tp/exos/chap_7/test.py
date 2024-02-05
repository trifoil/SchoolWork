from year import Year


print("""
#=======================================#
#                 TEST 1                #
#=======================================#
""")
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    val = test_data[i]
    yr = Year(val)
    print(yr, "-> ", end="")

    if yr.bissextile == test_results[i]:
        print(yr.bissextile, "OK")
    else:
        print(yr.bissextile, "KO")

# =======================================
# TEST 2 
# =======================================
print("""
#=======================================#
#                 TEST 2                #
#=======================================#
""")

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    val = test_years[i]
    yr = Year(val)
    test_month= test_months[i]
    
    print(yr, test_month, "-> ", end="")

    if yr.days_in_month(test_month) == test_results[i]:
        print(yr.days_in_month(test_month), "OK")
    else:
        print(yr.days_in_month(test_month), "KO")

# =======================================
# TEST 3
# =======================================
print("""
#=======================================#
#                  TEST 3               #
#=======================================#
""")
yr = Year(2000)
print(yr, "31/12", "-> ", end="")
if yr.day_of_year(12, 31) == "Dimanche":
    print(yr.day_of_year(12, 31), "OK", "\n")
else:
    print(yr.day_of_year(12, 31), "KO", "\n")
