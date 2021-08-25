
class Tree(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return 'Tree(%s, %s)' % (self.value, self.children)

    def depth_first_search(self, value):
        if self.value == value:
            return self
        for child in self.children:
            result = child.depth_first_search(value)
            if result:
                return result
        return None

    def breadth_first_search(self, value):
        nodes = [self]
        while nodes:
            node = nodes.pop(0)
            if node.value == value:
                return node
            nodes.extend(node.children)
        return None

    def insert(self, new_value):
        node = self.depth_first_search(new_value)
        if node:
            return node
        node = Tree(new_value)
        parent = self.breadth_first_search(new_value)
        if not parent:
            parent = self
        parent.children.append(node)
        return node

    def remove(self, value_to_remove):
        node = self.depth_first_search(value_to_remove)
        if not node:
            return
        parent = self.breadth_first_search(value_to_remove)
        if not parent:
            parent = self
        parent.children.remove(node)
        