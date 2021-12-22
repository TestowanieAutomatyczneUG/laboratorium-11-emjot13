import os


class SuperProfessionalFilesHandler3000:

    def raise_error_path_not_string(self, path):
        if type(path) is not str:
            raise TypeError

    def open_file(self, path):
        self.raise_error_path_not_string(path)
        with open(path) as f:
            return f.read()

    def delete_file(self, path):
        self.raise_error_path_not_string(path)
        os.remove(path)
        return True

    def edit_file(self, path, **kwargs):
        self.raise_error_path_not_string(path)
        for key, value in kwargs.items():
            if key[0:4] != "line":
                raise ValueError
            elif type(value) is not str:
                raise TypeError
        with open(path) as f:
            lines = f.readlines()
            for key, value in kwargs.items():
                line_to_edit = int(key[key.index("e") + 1::]) - 1
                lines[line_to_edit] = value + "\n"
            my_file = open(path, "w")
            for line in lines:
                my_file.write(line)
        return True

# obj = SuperProfessionalFilesHandler3000()
# obj.open_file("./toOpekkn")
# obj.edit_file("./toOpkken", line1="ok", line2="very good")
