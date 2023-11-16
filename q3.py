# def LOP(string):
#     def reflection(pivot, point):
#         return 2 * pivot - point
#     n = len(string)
#     longest = [1]
#     centre_FARTHEST_RIGHT_PALINDROME = 0
#     right_FARTHEST_RIGHT_PALINDROME = 0
#     left_FARTHEST_RIGHT_PALINDROME = 0
#     for pointer in range(1, n):
#         if pointer > right_FARTHEST_RIGHT_PALINDROME:
#             right_pointer = pointer
#             left_pointer = pointer
#             longest += [1]
#         else:
#             pointer_reflection = reflection(centre_FARTHEST_RIGHT_PALINDROME, pointer)
#             PALINDROME_LEFT_size = longest[pointer_reflection]
#             left_SUBPALINDROME_LEFT = max(left_FARTHEST_RIGHT_PALINDROME,
#                                           pointer_reflection - PALINDROME_LEFT_size + 1)
#             right_pointer = reflection(centre_FARTHEST_RIGHT_PALINDROME, left_SUBPALINDROME_LEFT)
#             left_pointer = reflection(pointer, right_pointer)
#             longest += [(right_pointer - pointer) * 2 + 1]
#         if right_pointer >= right_FARTHEST_RIGHT_PALINDROME:
#             centre_FARTHEST_RIGHT_PALINDROME = pointer
#             right_FARTHEST_RIGHT_PALINDROME = right_pointer
#             left_FARTHEST_RIGHT_PALINDROME = left_pointer
#             while True:
#                 if left_pointer == 0 or right_pointer == n - 1:
#                     break
#                 left_pointer -= 1
#                 right_pointer += 1
#                 if string[left_pointer] == string[right_pointer]:
#                     longest[pointer] += 2
#                     right_FARTHEST_RIGHT_PALINDROME += 1
#                     left_FARTHEST_RIGHT_PALINDROME -= 1
#                 else:
#                     break
#     return max(longest)


def LP(string):
    longest_palindromes = [LOP(string)] #already given longest odd palindrome
    for i in range(len(string)): #iterates through characters in string
        length = 0
        while True:
            if i-length >= 0 and i+1+length < len(string): #ensures palindrome not outside of string length
                if string[i-length] == string[i+1+length]: #compares characters either side of current position
                    length += 1
                else:
                    longest_palindromes.append(2*length) #calculates length of palindrome if not equal
                    break
            else:
                longest_palindromes.append(2*length) #calculates length of palindrome if it spans outside of string
                break
    return max(longest_palindromes)


def LP2(string):
    longest_palindromes = []
    for i in range(len(string)):
        new_string = string[i:] + string[:i] #creates new string by shifting start position
        longest_palindromes.append(LP(new_string))
    return max(longest_palindromes)