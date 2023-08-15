# 1 Validate the opening and closing brackets are balanced?
# "dj{qsqs(sqs)[qq{wdwdw}]sqsq}" --- Valid
# "sa{sq{q[qjgsq(s)s]s}" --- Invalid
# "{sqs[sq)sqs]sqs}" --- Invalid
# "{jgj[jhj(jgjg)kh)]}" --- Invalid

# My Logic
"""
Simple Logic can be use list and if its opening bracket add in starting point of list and
as soon as closing bracket is found it should match corresponding closing bracket at the first item of list
if its not return False
"""


def bracket_sequence_check(seq):
    my_list = []
    opening = '({['
    closing = ')}]'
    pair = {')': '(', '}': '{', ']': '['}
    for char in seq:
        if char in opening:
            my_list.insert(0, char)
        elif char in closing:
            if pair[char] == my_list[0]:
                my_list.remove(pair[char])
            else:
                return False

    return not bool(my_list)


print(bracket_sequence_check("{jgj[jhj(jgjg)kh)]}"))

# Online Logic
"""
This code uses a stack to keep track of opening brackets encountered in the input string.
When a closing bracket is encountered, the code checks if the corresponding opening bracket
is at the top of the stack. If not, the brackets are not balanced. After processing the entire
input string, if the stack is empty, the brackets are balanced; otherwise, they are not.
"""


# need to understand this
def is_balanced(input_string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False

    return not stack


# print(is_balanced('{jgj[jhj(jgjg)kh)]}'))

# 2 Create Palindrome equivalant for a given string.
# Given : abacedbce == > Required abcedecba
# xxxxzzy == > xxzyzxx
# abab == > abba
# aaa == > aaa
# baa == > aba
# gg == > gg

# Online Logic
"""
This code first counts the occurrences of each character in the input string.
Then, it constructs the left and right halves of the palindrome using the characters
with even occurrences. If there's a character with an odd occurrence, it becomes the
middle character of the palindrome. If there are multiple characters with odd occurrences,
it's not possible to create a palindrome, and the code returns an appropriate message.
"""


def create_palindrome(input_string):
    # Count the occurrences of each character
    char_count = {a: input_string.count(a) for a in input_string}

    # Build the left and right halves of the palindrome
    left_half = ""
    right_half = ""
    middle_char = ""
    for char, count in char_count.items():
        if count % 2 == 0:
            left_half += char * (count // 2)
            right_half = char * (count // 2) + right_half
        else:
            if middle_char == "":
                middle_char = char
                left_half += char * (count // 2)
                right_half = char * (count // 2) + right_half
            else:
                return "Cannot create palindrome"
    palindrome = left_half + middle_char + right_half
    return palindrome

# print(create_palindrome('malayalam'))
