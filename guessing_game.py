# This code is a number guessing game. 

import math
import random


def create_random_nums_list():
    rand_nums = []
    for num in range(10):
        rand_nums.append(random.randint(1, 99))
    return rand_nums


def guessing_phase(rand_nums):
    for n in range(10):
        guess = int(input("Enter an integer from 1 to 99: "))
        while rand_nums[n] != guess:
            if guess < rand_nums[n]:
                print("guess is low")
                guess = int(input("Enter an integer from 1 to 99: "))
            elif guess > rand_nums[n]:
                print("guess is high")
                guess = int(input("Enter an integer from 1 to 99: "))
            else:
                break
    print("you guessed it!")


def create_sec_rand_nums_list():
    rand_nums_2 = []
    for b in range(10):
        rand_nums_2.append(random.randint(1, 49))
    return rand_nums_2


def sec_guessing_phase(rand_nums_2):
    for i in range(10):
        guess_2 = int(input("Enter an integer from 1 to 49: "))
        while rand_nums_2[i] != guess_2:
            if guess_2 < rand_nums_2[i]:
                print("guess is low")
                guess_2 = int(input("Enter an integer from 1 to 49: "))
            elif guess_2 > rand_nums_2[i]:
                print("guess is high")
                guess_2 = int(input("Enter an integer from 1 to 49: "))
            else:
                break
        print("you guessed it!")


def main():
    first_rand_num_list = create_random_nums_list()
    guessing_phase(first_rand_num_list)
    sec_rand_num_list = create_sec_rand_nums_list()
    sec_guessing_phase(sec_rand_num_list)


if __name__ == '__main__':
    main()
