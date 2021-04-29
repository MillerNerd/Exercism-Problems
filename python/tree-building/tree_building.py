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
    ordered_id = [i.record_id for i in records]
    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('Tree must be continuous')
        if ordered_id[0] != 0:
            raise ValueError('Tree must start with id 0')
    trees = []
    parent = {}
    if records[0].parent_id != 0:
        raise ValueError('Root node cannot have a parent')
    for j in records:
        if j.record_id < j.parent_id:
            raise ValueError('Parent id must be lower than child id')
        if j.record_id == j.parent_id:
            if j.record_id != 0:
                raise ValueError('Tree is a cycle')
        trees.append(Node(j.record_id))
    for i in ordered_id:
        parent = trees[i]
        # for j in trees:
        #     if i == j.node_id:
        #         parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    return trees[0]
