from functools import partial
from itertools import groupby
from spitslurp import slurp
import json
import re


def parse(input):
    nodes = []
    for line in input.split('\n'):
        match = re.search(r'(?P<name>\w+) \((?P<weight>\d+)\)( -> )?(?P<children>[ \w,]+)?', line)
        if match:
            node = match.groupdict()
            node['children'] = node['children'].split(', ') if node['children'] else []
            node['weight'] = int(node['weight'])
            nodes.append(node)
    return nodes


def find_root(nodes):
    node_names = []
    for node in nodes:
        node_names.append(node['name'])
        for child_name in node['children']:
            node_names.append(child_name)

    node_count = [[key, len(list(group))] for key, group in groupby(sorted(node_names))]
    root = [name for name, count in node_count if count == 1][0]
    return root


def find_node(nodes, name):
    try:
        return [node for node in nodes if node['name'] == name][0]
    except:
        return None


def sum_branch(nodes, root):
    total = root['weight']
    for node_name in root['children']:
        node = find_node(nodes, node_name)
        if len(node['children']):
            total += sum_branch(nodes, node)
        else:
            total += node['weight']
    return total


def get(key, d):
    return dict.get(d, key)


def find_unbalanced(nodes):
    # Get sum value from dict
    get_sum = partial(get, 'sum')
    for node in nodes:
        node['sum'] = sum_branch(nodes, node)
    for node in nodes:
        child_nodes = [find_node(nodes, node_name) for node_name in node['children']]
        if len(child_nodes):
            child_nodes = sorted(child_nodes, key=get_sum)
            freq = [[name, len(list(group))] for name, group in groupby(child_nodes, key=get_sum)]
            # print freq
            unbalanced = [name for name, count in freq if count == 1]
            expected_sum = [name for name, count in freq if count > 1][0]
            if len(unbalanced):
                unbalanced = unbalanced[0]
                unbalanced_node = [node for node in child_nodes if node['sum'] == unbalanced][0]
                return (unbalanced_node, expected_sum)
    return (None, None)


nodes = parse(slurp('day07_test.txt'))

# print sum_branch(nodes, find_node(nodes, 'tknk'))

nodes = parse(slurp('day07.txt'))
# print json.dumps(nodes, indent=2)
print 'Part 1:', find_root(nodes)

(unbalanced_node, expected_sum) = find_unbalanced(nodes)
print 'unbalanced_node:', unbalanced_node
print 'expected_sum:', expected_sum
print 'Part 2:', unbalanced_node['weight'] + (expected_sum - unbalanced_node['sum'])
