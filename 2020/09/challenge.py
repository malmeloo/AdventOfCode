import aoc

input_data = aoc.get_input(data_type=int)

last_numbers = input_data[:25]
check_nums = input_data[25:]


def is_valid(target_sum):
    for i, num1 in enumerate(last_numbers):
        to_check = last_numbers[i:]
        for num2 in to_check:
            if num1 + num2 == target_sum and num1 != num2:
                return True

    return False


def challenge1():
    """
    Challenge 1
    """
    while check_nums:
        check_num = check_nums.pop(0)
        if not is_valid(check_num):
            return check_num

        del last_numbers[0]
        last_numbers.append(check_num)


def challenge2(invalid_num):
    for subset_size in range(2, len(input_data)+1):
        subset_count = len(input_data) - subset_size + 1

        for offset in range(subset_count):
            subset = input_data[offset:offset+subset_size]

            if sum(subset) == invalid_num:  # found our contiguous set!
                max_num = max(subset)
                min_num = min(subset)
                return max_num + min_num


res = aoc.run(challenge1)
aoc.run(challenge2, res)

