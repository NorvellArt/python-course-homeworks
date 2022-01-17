class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def print_info(self):
        print(f'{self.name} => {self.note.print_notebook_info()}')

    class Notebook:
        def __init__(self):
            self.model = 'HP'
            self.processor = 'i7'
            self.RAM = 16

        def print_notebook_info(self):
            return f'{self.model}, {self.processor}, {self.RAM}'


roman = Student('Roman')
vladimir = Student('Vladimir')
roman.print_info()
vladimir.print_info()
