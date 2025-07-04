import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    def get_calculator(self):
        result = get_files_info("calculator", ".")
        print(result)
    
    def get_calculator_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(result)
    
    def get_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        
    def get_calculator_parent(self):
        result = get_files_info("calculator", "../")
        print(result)
        
    def test_get_info_max(self):
        result = get_file_content("calculator", "lorem.txt")
        print(result)
        
    def test_get_info_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)
    
    def test_get_info_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        
    def test_get_info_error(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        
    def write_over_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
    
    def write_new_file(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
    def write_out_of_scope(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        
    def run_calculator(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        
    def run_calculator_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
        
    def run_out_of_scope(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        
    def run_non_existent(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        
if __name__ == "__main__":
    test = TestGetFilesInfo()
    test.run_calculator()
    test.run_calculator_tests()
    test.run_out_of_scope()
    test.run_non_existent()