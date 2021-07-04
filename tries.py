def decimal_to_binary(A):
    # creating an empty list for the binary values of the numbers
    A_bin = []
    # transforming the int to binary strings with no trailing 0s and appending them to A_bin
    for num in A:
        binary_num = format(num, 'b')
        A_bin.append(binary_num)
    return A_bin


def check_count_for_specific_bit(A_bin, A_bin_copy, bit_pos, max_count):
    # initiating count for specific bit
    bit_count = 0
    # iterating over each number in the list
    for num in A_bin:
        # if the current bit we are checking is not needed to represent the number, just move on to the next number
        if bit_pos < -len(num):
            A_bin_copy.remove(num)
        elif num[bit_pos] == '1':
            bit_count += 1
    if bit_count > max_count:
        max_count = bit_count
    A_bin = A_bin_copy.copy()
    return A_bin, max_count


def solution(A):
    # sorting the list in des order
    A.sort(reverse=True)
    # count initiation
    max_count = 0
    A_bin = decimal_to_binary(A)
    # determining the max bit number needed to be checked
    longest_bin = len(max(A_bin, key=len))
    # make a hard copy of A_bin
    A_bin_copy = A_bin.copy()
    # iterating over individual bits
    for bit_pos in range(-1, -longest_bin-1, -1):
        A_bin, max_count = check_count_for_specific_bit(A_bin, A_bin_copy, bit_pos, max_count)
    return max_count


# a = ["111", "2", "44"]
# print(len(max(a, key=len)))
print(solution([55, 90, 11, 33333, 4405, 702650, 13, 7, 2, 8, 3]))
print(solution([16, 16]))
print(solution([1, 2, 4, 8]))

# a = (1, 4)
# print("a = ", a)
# a = (3, 6)
# print("a = ", a)