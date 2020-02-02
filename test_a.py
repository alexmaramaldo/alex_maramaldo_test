from my_libraries.overlap import Overlap

true_result = Overlap((1, 5), (2, 6))

false_result = Overlap((1, 5), (6, 8))


print(f"""True example result is: {true_result}""")
print(f"""False example result is: {false_result}""")
