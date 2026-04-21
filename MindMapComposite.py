import os

class MindMapComposite:
    def __init__(self, name:str, shape:str):
        self.name = name
        self.shape = shape
        self.children = list()

    def __str__(self):
        return MindMapComposite.get_shape_representation(self.shape).format(self.name)

    def display(self, indent:int=0):
        if indent == 0:
            indent += 2
            print('mindmap' + os.linesep + ' ' * indent + 'root' + str(self))
        else:
            print(' ' * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def add(self, child:MindMapComposite|MindMapLeaf):
        self.children.append(child)

    def remove(self, child:MindMapComposite|MindMapLeaf):
        self.children.remove(child)

    @staticmethod
    def get_shape_representation(key:str) -> str:
        shapes = {
            'circle': '(({}))',
            'oval': '({})',
            'square': '[{}]',
            'cloud': '){}(',
            'hexagon': '{{{{{}}}}}',
            'bang': ')){}(('
        }
        return shapes.get(key, '{}')

if __name__ == '__main__':
    from MindMapLeaf import MindMapLeaf

    # Step 6: Create MindMapComposite and MindMapLeaf objects to test
    root = MindMapComposite("Root", "circle")
    leaf1 = MindMapLeaf("Child 1", "square")
    leaf2 = MindMapLeaf("Child 2", "cloud")
    root.add(leaf1)
    root.add(leaf2)

    print(str(root))  # Should display "((Root))"
    root.display()  # Should display root and its children

    print("MindMapComposite tests completed!")