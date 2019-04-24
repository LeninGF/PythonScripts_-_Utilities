import sys

from hello import print_my_name
import hello2_arg


print_my_name('Lenin')   # This one works with from hello import print_my_name
hello2_arg.main('Gonzalo')  # This one works with import hello2_arg
hello2_arg.print_my_name('hooola') # This one works with import hello2_arg



