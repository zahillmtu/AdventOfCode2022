

class DirectoryTree:

    total_size = 0
    size_to_delete = 208860
    current_min = 70000000

    def __init__(self, root):
        self.root_node = root
        self.current_node = root

    def change_directory(self, dir_name):
        if dir_name == "..":
            self.current_node = self.current_node.parent
            return

        if dir_name == "/":
            self.current_node = self.root_node
            return

        self.current_node = self.current_node.find_child_directory(dir_name)

    def add_directory(self, dir_name):
        self.current_node.add_child_dir(dir_name)

    def add_file(self, file_name, file_size):
        self.current_node.add_file(file_name, file_size)

    def sum_total_file_size_from_root(self):
        return self.sum_total_file_size(self.root_node)

    def sum_total_file_size(self, node):

        current_total = node.sum_file_sizes()

        for child in node.child_directories:
            current_total += self.sum_total_file_size(child)

        # for part 1
        # if current_total <= 100000:
        #    self.total_size += current_total

        if self.size_to_delete <= current_total < self.current_min:
            self.current_min = current_total

        return current_total
