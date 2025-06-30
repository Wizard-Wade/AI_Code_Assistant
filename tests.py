import unittest
from functions.get_files_info import get_files_info

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
        
if __name__ == "__main__":
    test = TestGetFilesInfo()
    test.get_calculator()
    test.get_calculator_pkg()
    test.get_calculator_bin()
    test.get_calculator_parent()