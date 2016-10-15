import BinarySearchTree;
bst = BinarySearchTree.BST();
bst.insert(11);
bst.insert(3);
bst.insert(-5);
bst.insert(0);

bst.traverseInOrder();

bst.remove(3);

bst.traverseInOrder();

print(bst.getMin());
print(bst.getMax());
