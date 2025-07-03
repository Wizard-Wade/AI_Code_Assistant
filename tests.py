import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
        
if __name__ == "__main__":
    test = TestGetFilesInfo()
    test.test_get_info_main()
    test.test_get_info_calculator()
    test.test_get_info_error()