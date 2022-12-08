from FileNode import FileNode


class DirectoryNode:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child_directories = []
        self.files = []

    def add_child_dir(self, child_dir):
        for child in self.child_directories:
            if child.name == child_dir:
                # dir already in the children
                return

        self.child_directories.append(DirectoryNode(child_dir, self))

    def add_file(self, file_name, file_size):
        for file in self.files:
            if file.name == file_name:
                # file already in dir
                return

        self.files.append(FileNode(file_size, file_name))

    def find_child_directory(self, dir_name):
        for child in self.child_directories:
            if dir_name == child.name:
                return child

        print("No child found!")
        return None

    def sum_file_sizes(self):
        total = 0

        for file in self.files:
            total += file.size

        return total

    def sum_child_file_sizes(self):

        total = self.sum_file_sizes()

        for child in self.child_directories:
            total += child.sum_child_file_sizes()

        return total