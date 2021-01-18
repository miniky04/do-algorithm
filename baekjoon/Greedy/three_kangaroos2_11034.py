while True:
    try:
        one, two, three = map(int, input().split())
        movement_count = 0
        if (three - two) - 1 >= 1:
            movement_count = (three - two) - 1
        if (two - one) - 1 >= 1:
            if movement_count < (two - one) - 1:
                movement_count = (two - one) - 1
        print(movement_count)
    except EOFError:
        break
# if one < three:  # 양수일 때
#     two_plus = two + 1
#     if two_plus < three:
#         movement_count += 1
#         print(movement_count)
#     else:
#         print(movement_count)
# elif one > three:  # 음수일 때
#     two_plus2 = two + 1
#     if two_plus2 < one:
#         movement_count += 1
#         print(movement_count)
#     else:
#         print(movement_count)

# if two - one >= 1:
#     movement_count = (two - one) - 1
#     if three - two > 1:
#         if movement_count < three - two:
#             movement_count = (three - two) - 1
#             print(movement_count)
# else:
#     print(movement_count)
