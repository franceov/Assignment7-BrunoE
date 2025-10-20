class DoctorNode:
    def __init__(self, name: str):
        self.name = name
        self.left = None   # type: DoctorNode | None
        self.right = None  # type: DoctorNode | None

    def __repr__(self) -> str:
        return f"DoctorNode({self.name!r})"


class DoctorTree:
    def __init__(self):
        self.root = None  # type: DoctorNode | None

    # ----- Internal helpers -----
    def _find(self, node: 'DoctorNode | None', target: str) -> 'DoctorNode | None':
        if node is None:
            return None
        if node.name == target:
            return node
        # search left then right
        found_left = self._find(node.left, target)
        if found_left:
            return found_left
        return self._find(node.right, target)

    # ----- Public API -----
    def insert(self, parent_name: str, child_name: str, side: str) -> None:
        """Insert a doctor named `child_name` under `parent_name` on `side` ('left' or 'right').
        Raises ValueError if parent isn't found, side is invalid, or the spot is already occupied.
        """
        if self.root is None:
            raise ValueError("Cannot insert into an empty tree. Set tree.root first (DoctorNode).")

        side = side.lower().strip()
        if side not in {"left", "right"}:
            raise ValueError("side must be 'left' or 'right'")

        parent = self._find(self.root, parent_name)
        if parent is None:
            raise ValueError(f"Parent '{parent_name}' not found in the tree.")

        if side == "left":
            if parent.left is not None:
                raise ValueError(f"Parent '{parent_name}' already has a left report.")
            parent.left = DoctorNode(child_name)
        else:
            if parent.right is not None:
                raise ValueError(f"Parent '{parent_name}' already has a right report.")
            parent.right = DoctorNode(child_name)

    def preorder(self, node: 'DoctorNode | None') -> list[str]:
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node: 'DoctorNode | None') -> list[str]:
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node: 'DoctorNode | None') -> list[str]:
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


if __name__ == "__main__":
    # Example usage matching the assignment
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
