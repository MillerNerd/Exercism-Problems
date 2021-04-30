class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    records.sort(key=lambda x: x.record_id)
    if records:
        if records[-1].record_id != len(records) - 1:
            raise ValueError('Tree must be continuous')
        if records[0].record_id != 0:
            raise ValueError('Tree must start with id 0')
    trees = []
    if records[0].parent_id != 0:
        raise ValueError('Root node cannot have a parent')
    # create Nodes, store in trees list
    for j in records:
        if j.record_id < j.parent_id:
            raise ValueError('Parent id must be lower than child id')
        if j.record_id == j.parent_id:
            if j.record_id != 0:
                raise ValueError('Tree is a cycle')
        trees.append(Node(j.record_id))
    # add children to each node
    for j in records:
        if j.record_id == 0:
            continue
        trees[j.parent_id].children.append(trees[j.record_id])
    return trees[0]
