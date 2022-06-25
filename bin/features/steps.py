from lettuce import *

from main import add

@step('numbers (\d+) and (\d+)')
def the_number(step, num1, num2):
    world.num1 = int(num1)
    world.num2 = int(num2)

@step('I call add')
def call_to_function(step):
    world.result = add(world.num1, world.num2)

@step('I see (\d+)')
def compare_result(step, result):
    x = int(result)
    assert world.result == x, "Got %d" % x
