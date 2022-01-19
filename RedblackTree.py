# Learn more about how this code works: https://drive.google.com/file/d/1IX8c8r4-qF5FUlMJmB4n_gyO2ziRt3XO/view?usp=sharing
"""
Package RedblackTree provides a tree data structure to implement associative arrays.

A red-black tree is a special typ of binary search tree with better worst time than other binary trees. Each node of it
stores a colour, red or black, to ensure that the tree remains balanced during insertion and deletion.

Compared with other binary trees, red-black trees guarantee the worst time. The time complexity of all its operations
(i.e. find, insert and delete) is the worst O(log n). In addition to the attributes of the binary search tree, each node
 of the red-black tree has the colour red or black, and its root and nil-nodes must be black. If the node is red, then
 it must have two black child nodes. In addition, the number of black nodes on all simple paths from any node to its
 leaves on the tree is the same. Therefore, the longest possible path from the root to leaf is no more than twice as
 long as the shortest possible path.
"""


class _Node:
    """Private class, used to define nodes."""
    def __init__(self, data):
        self.data = data
        self.color = 'red'  # define color of new node is red.
        self.parent = None
        self.left = None
        self.right = None


class RbTree:
    """classes contains all red-black tree operations.
    In the Red-black tree each node has a value and color.
    'red' means color red. 'black' means color black.
    Node.left means left child of the node. Node.right means right child of the node.
    Node.parent means the parent of the node."""

    def __init__(self):
        self._root = None
        self._size = 0  # the number of elements in the root
        self._list = []  # the elements in the root

    def _rotation(self, direction, parent, child):
        """Private function. Rotation operation, use to balance the tree.
        Input the pivot node.
        'lR'- rotation to the left (counterclockwise).
        'rR'- rotation to the right (clockwise)."""

        if direction == 'lR':  # Left rotation
            parent.right = child.left
            if child.left is not None:
                child.left.parent = parent
            child.left = parent
            child.parent = parent.parent
            if parent.parent is None:
                self._root = child
            elif parent.parent.left == parent:
                parent.parent.left = child
            else:
                parent.parent.right = child
            parent.parent = child

        elif direction == 'rR':  # Right rotation
            parent.left = child.right
            if child.right is not None:
                child.right.parent = parent
            child.right = parent
            child.parent = parent.parent
            if parent.parent is None:
                self._root = child
            elif parent.parent.left == parent:
                parent.parent.left = child
            else:
                parent.parent.right = child
            parent.parent = child

        else:
            return KeyError('The rotation command does not exist.')

        parent.color, child.color = child.color, parent.color  # change color

    def _get_min(self, node):
        """Find the smallest node in the node."""
        if node.left is None:
            return node
        else:  # Node has left child. Continue to the left subtree of the node until find the leftmost child.
            node = self._get_min(node.left)
            return node

    def _search(self, node, data):
        """Privat function. Find if a specific value exists in the tree. If the existing return node, otherwise the
        output is None."""
        if node is not None:
            if node.data > data:
                node = self._search(node.left, data)
                return node
            elif node.data < data:
                node = self._search(node.right, data)
                return node
            else:  # if node.data == data
                return node
        else:  # node is none
            return None

    def find(self, data):
        """Find if a specific value exists in the tree. If the existing the output is True, otherwise the output is
        False."""
        answer = self._search(self._root, data)
        if answer is None:
            return False
        else:
            return True

    def _inorder(self, node):
        """private function. Be used to inorder traversal and count the number of elements in the tree."""
        if node is not None:
            self._inorder(node.left)
            self._list.append(node.data)
            self._size += 1
            self._inorder(node.right)

    def count(self):
        """Count the number of elements in the tree."""
        self._size = 0
        self._inorder(self._root)
        return self._size

    def write(self):
        """Returns a string with all elements in ascending order."""
        self._list = []
        self._inorder(self._root)
        return self._list

    def _insert(self, root, node1):
        """Privat insert operation. Used in insert function to add the specified value to the tree."""
        if root is None:
            root = node1
        elif node1.data < root.data:
            root.left = self._insert(root.left, node1)
            root.left.parent = root
        elif node1.data > root.data:
            root.right = self._insert(root.right, node1)
            root.right.parent = root
        return root

    def insert(self, data):
        """Insert operation. Add the specified value to the tree."""
        node = _Node(data)
        check = self._search(self._root, node.data)
        if check is not None:
            return
        else:
            if self._root is None:
                node.color = 'black'
                self._root = node
                return

            self._insert(self._root, node)
            pin = node
            while True:
                if pin.parent.color == 'red':
                    if pin.parent == pin.parent.parent.left:
                        pb = pin.parent.parent.right
                    else:
                        pb = pin.parent.parent.left

                    #  If pin.parent is red and pin.parents brother is black
                    if pb is None or pb.color == 'black':
                        if pin.parent == pin.parent.parent.left:  # pin.parent is left child
                            if pin == pin.parent.right:  # left right
                                self._rotation('lR', pin.parent, pin)
                                self._rotation('rR', pin.parent, pin)
                            else:  # left left
                                self._rotation('rR', pin.parent.parent, pin.parent)

                        elif pin.parent == pin.parent.parent.right:  # pin.parent is right child
                            if pin == pin.parent.left:  # right left
                                self._rotation('rR', pin.parent, pin)
                                self._rotation('lR', pin.parent, pin)
                            else:  # right right
                                self._rotation('lR', pin.parent.parent, pin.parent)
                        break

                    #  If pin.parent is red and pin.parents brother is red
                    elif pb.color == 'red':
                        pin.parent.color = 'black'
                        pb.color = 'black'
                        if pin.parent.parent != self._root:
                            pin.parent.parent.color = 'red'
                            pin = pin.parent.parent
                else:
                    break

    def _delete_nochild(self, node):
        """Private function. Be used to delete the node with no child."""
        if node == self._root:
            self._root = None
            # self._root.color = 'black'
            return
        pin = node
        if pin.color == 'black':
            while True:
                if pin is pin.parent.left:
                    b = pin.parent.right
                else:
                    b = pin.parent.left
                if pin == pin.parent.left:
                    if b.color == 'black':  # parents brother is black
                        if b.left is None and b.right is None:  # if parents brother has no child
                            b.color = 'red'
                            if pin.parent.color == 'red':
                                pin.parent.color = 'black'
                                break
                            else:
                                if pin.parent == self._root:
                                    break
                                pin = pin.parent
                        elif b.left.color == 'black' and b.right.color == 'black':  # two child of parents brother is black
                            b.color = 'red'
                            if pin.parent.color == 'red':
                                pin.parent.color = 'black'
                                break
                            else:
                                if pin.parent == self._root:
                                    break
                                pin = pin.parent

                        elif b.right is not None and b.right.color == 'red':
                            b.right.color = 'black'
                            self._rotation('lr', pin.parent, b)
                            break

                        else:
                            self._rotation('rR', b, b.left)

                    elif b.color == 'red':
                        self._rotation('lr', pin.parent, b)

                if pin == pin.parent.right:
                    if b.color == 'black':
                        if b.left is None and b.right is None:
                            b.color = 'red'
                            if pin.parent.color == 'red':
                                pin.parent.color = 'black'
                                break
                            else:
                                if pin.parent == self._root:
                                    break
                                pin = pin.parent
                        elif b.left.color == 'black' or b.right.color == 'black':
                            b.color = 'red'
                            if pin.parent.color == 'red':
                                pin.parent.color = 'black'
                                break
                            else:
                                if pin.parent == self._root:
                                    break
                                pin = pin.parent
                        elif b.left is not None and b.left.color == 'red':
                            b.left.color = 'black'
                            self._rotation('rR', pin.parent, b)
                            break
                        else:
                            self._rotation('lR', b, b.right)

                    elif b.color == 'red':
                        self._rotation('rR', pin.parent, b)

        if node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None
        node.parent = None

    def _delet_onechild(self, node):
        """Private function. Be used to delete the node with only one child."""
        if node.left is not None:
            node.left.color = 'black'
            if node.parent is not None and node == node.parent.left:
                node.left.parent, node.parent.left = node.parent, node.left
            elif node.parent is not None and node == node.parent.right:
                node.left.parent, node.parent.right = node.parent, node.left
            else:
                self._root = node.left
                node.left.parent, node.left = None, None
        elif node.right:
            node.right.color = 'black'
            if node.parent is not None and node == node.parent.left:
                node.right.parent, node.parent.left = node.parent, node.right
            elif node.parent is not None and node == node.parent.right:
                node.right.parent, node.parent.right = node.parent, node.right
            else:
                self._root = node.right
                node.right.parent, node.right = None, None

        node.parent = None

    def _delete(self, node):
        """Private function. Be used in the function deletData to delete the specific node."""
        # node has no child
        if node.left is None and node.right is None:
            self._delete_nochild(node)

        # node has only left child
        elif node.left is not None and node.right is None:
            self._delet_onechild(node)

        # node has only right child
        elif node.right is not None and node.left is None:
            self._delet_onechild(node)

        # node has two child
        else:  # Find tne inorder successor of the node. It must be in the left subtree of the node if it exist.
            replace = self._get_min(node.right)
            node.data = replace.data
            self._delete(replace)

    def deletData(self, data):
        """Delete the specific node from the tree."""
        if self._root is not None:
            node = self._search(self._root, data)
            if node is None:
                return KeyError('Input data is not in the tree.')
            else:
                self._delete(node)
        else:
            return KeyError('The tree is empty')

    def healthy(self):
        """Determine whether the tree meets the attributes of the red-black tree.
        If the tree is not healthy, return Error."""
        if self._root is None:
            print("This tree is empty.")
            return
        else:
            l = []
            l.insert(0, self._root)
            height = 0
            while len(l):
                node = l.pop()
                if node.color != 'red' and node.color != 'black':
                    raise Exception('Node{} does not meet the color characteristics'.format(node.data))
                if node is self._root and node.color != 'black':
                    raise Exception('node{} does not meet the characteristic of the root'.format(node.data))
                if node.color == 'red':
                    if node.left is not None and node.left.color == 'red':
                        raise Exception(
                            'node{} does not meet that red nodes left child must be black'.format(node.data))
                if node.color == 'red':
                    if node.right is not None and node.right.color == 'red':
                        raise Exception(
                            'node{} does not meet that red nodes right child must be black'.format(node.data))
                if node.left is None and node.right is None:
                    number = 0
                    pointer = node
                    while pointer:
                        if pointer.color == 'black':
                            number += 1
                            # print(pointer.data)
                        pointer = pointer.parent
                    if height and number != height:
                        raise Exception(
                            'node{} does not meet the characteristic of the number of blacks on the path'.format(
                                node.data))
                    else:
                        height = number
                if node.left is not None:
                    l.insert(0, node.left)
                if node.right is not None:
                    l.insert(0, node.right)
        print(height)


# Example of usage
def main():
    tree = RbTree()
    # Insert a new value in the tree
    data1 = 55
    data2 = 77
    tree.insert(data1)
    tree.insert(data2)

    # Delete one value in the tree
    tree.deletData(data1)

    # Print all values in the tree as a list
    valuelist = tree.write()
    print(valuelist)

    # Find if the value is in the book
    tree.find(data2)

    # Calculate how many node are in the tree
    number = tree.count()
    print(number)

    # Check if the tree is healthy
    tree.healthy()


if __name__ == '__main__':
    main()