from string import ascii_letters
from datetime import datetime
import random

#1 ----------------------------------

def get_second_letters(string: str) -> list[str]:
    return string[1::2]

assert(get_second_letters('asdfasdf') == 'sfsf')

#2 ----------------------------------

def not_more_than_3_letters(string: str) -> bool:
    letters = set(ascii_letters)
    count = 0
    for letter in string:
        if letter in letters:
            count+=1
            if count > 3:
                return False
            
    return True

assert(not_more_than_3_letters('__237263b134a456634h') == True)
assert(not_more_than_3_letters('__237263b134a456634hJ') == False)

#3 ----------------------------------

def numbers_with_various_digits(numbers: list[int]) -> list[int]:
    res = []
    for number in numbers:
        string = str(number)
        if len(string) == len(set(string)):
            res.append(number)

    return res

assert(numbers_with_various_digits([12345, 5433, 110, 2851, 0]) == [12345, 2851, 0])

#4 ----------------------------------

def sort_nested_lists(lists: list[list[int]]) -> list[list[int]]:
    return [list(sorted(nested_list)) for nested_list in lists]

assert(sort_nested_lists([
    [1, 2, 3],
    [3, 2, 1],
    [2, 3, 1],
]) == [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
])

#5 ----------------------------------

def first_difference_second_date_in_days(firstDate: str, secondDate: str) -> int:
    return (datetime.fromisoformat(firstDate) - datetime.fromisoformat(secondDate)).days

assert(first_difference_second_date_in_days('2024-07-05', '2024-06-10') == 25)

#6 ----------------------------------

def get_dividers(number: int) -> list[int]:
    return [divider for divider in range(1, number//2) if (number % divider) == 0] + [number]


def is_prime_number(number: int) -> bool:
    if number == 1:
        return False
    
    for divider in range(2, number//2 + 1):
        if (number % divider) == 0:
            return False
        
    return True


def get_prime_dividers(number: int) -> list[int]:
    return [divider for divider in get_dividers(number) if is_prime_number(divider)]

assert(get_prime_dividers(88) == [2, 11])

#7 ----------------------------------

def read_file_and_scramble_words(prefixPath: str, fileName: str) -> None:
    scrambled_sentences = []
    with open(prefixPath + fileName, 'r') as file:
        text = file.read()
        sentences = [sentence for sentence in text.split('.') if sentence != '']
        for sentence in sentences:
            words = sentence.split()
            random.shuffle(words)
            scrambled_sentences.append(' '.join(words) + '.')

    with open(prefixPath + 'scrambled_' + fileName, 'w') as file:
        file.write('\n'.join(scrambled_sentences))

assert(True)

#8 ----------------------------------

# использование вспомогательной функции из 6 задачи
def check_friendly_numbers(num1: int, num2: int) -> bool:
    num1Dividers = get_dividers(num1)
    num2Dividers = get_dividers(num2)

    return True if sum(num1Dividers) == num2 or sum(num2Dividers) == num1 else False

assert(check_friendly_numbers(88, 136))

#9 ----------------------------------

def get_max_depth_list(multilist: list) -> int:
    maxDepth = 0

    def traverse_list(current_list: list, depth: int):
        for obj in current_list:
            if type(obj) is list:
                traverse_list(obj, depth + 1)

        nonlocal maxDepth
        maxDepth = max(depth, maxDepth)

    traverse_list(multilist, 0)
    return maxDepth

assert(get_max_depth_list(
[
    [
        [

        ],
        [
            [

            ]
        ]
    ],
    [

    ]
]) == 3)

#10 ----------------------------------

# использование вспомогательной функции из 6 задачи
def find_prime_numbers(end: int) -> list[int]:
    numbers = [i for i in range(2, 31)]
    deletedNumbers = set()

    for number in numbers:
        if number * number > end:
            break

        if number not in deletedNumbers and is_prime_number(number):
            for compositeNumber in range(number * 2, end + 1, number):
                deletedNumbers.add(compositeNumber)

    return [number for number in numbers if number not in deletedNumbers]


assert(find_prime_numbers(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
