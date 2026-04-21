import os

class MindMapLeaf:
    def __init__(self, name:str, shape:str):
        self.name = name
        self.shape = shape

    def __str__(self):
        return MindMapLeaf.get_shape_representation(self.shape).format(self.name)

    def display(self, indent:int=0) -> str:
        if indent == 0:
            indent += 2
            print('mindmap' + os.linesep + ' ' * indent + 'root' + str(self))
        else:
            print(' ' * indent + str(self))

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
    # Step 5: Create a MindMapLeaf object and test the __str__ and display methods.
    leaf = MindMapLeaf("Jean-Luc Picard", "circle")
    print(str(leaf))  # Should display "((Jean-Luc Picard))"
    leaf.display(2)  # Should display "  ((Jean-Luc Picard))" with two spaces

    print("MindMapLeaf tests completed!")