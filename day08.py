from collections import defaultdict
from operator import *
from spitslurp import slurp

test_script = slurp('day08_test.txt')
main_script = slurp('day08.txt')


def parse(line):
    parts = line.split()
    cond = parts[4:-1] + [int(parts[-1])]
    oper = parts[:2] + [int(parts[2])]
    return {
        'cond': cond,
        'oper': oper
    }


def execute_each(script):

    variables = defaultdict(int)
    operations = {
        'inc': add,
        'dec': sub
    }
    logic = {
        '>': gt,
        '>=': ge,
        '<': lt,
        '<=': le,
        '==': eq,
        '!=': ne
    }

    lines = script.strip().split('\n')
    for line in lines:
        # print line
        ast = parse(line)
        # print ast
        cond = ast['cond']
        oper = ast['oper']
        if logic[cond[1]](variables[cond[0]], cond[2]):
            variables[oper[0]] = operations[oper[1]](variables[oper[0]], oper[2])
            yield variables


def execute(script):
    for variables in execute_each(script):
        pass
    return variables


def largest_value(variables):
    return max([num for v, num in variables.items()])


def all_time_largest(script):
    largest = 0
    for variables in execute_each(script):
        largest = max(largest, max([num for v, num in variables.items()]))
    return largest


print 'Part 1 (test): ', largest_value(execute(test_script))
print 'Part 1: ', largest_value(execute(main_script))
print 'Part 2 (test): ', all_time_largest(test_script)
print 'Part 2: ', all_time_largest(main_script)
