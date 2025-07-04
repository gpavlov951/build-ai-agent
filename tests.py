from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    """Test the write_file function with various scenarios."""
    
    print("Testing write_file function...")
    print("=" * 60)
    
    print("Test 1: write_file('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum')")
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)
    print()
    
    print("Test 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)
    print()
    
    print("Test 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)
    print()
    
    print("Testing run_python_file function...")
    print("=" * 60)
    
    print("Test 4: run_python_file('calculator', 'main.py')")
    result4 = run_python_file("calculator", "main.py")
    print(result4)
    print()
    
    print("Test 5: run_python_file('calculator', 'tests.py')")
    result5 = run_python_file("calculator", "tests.py")
    print(result5)
    print()
    
    print("Test 6: run_python_file('calculator', '../main.py') (this should return an error)")
    result6 = run_python_file("calculator", "../main.py")
    print(result6)
    print()
    
    print("Test 7: run_python_file('calculator', 'nonexistent.py') (this should return an error)")
    result7 = run_python_file("calculator", "nonexistent.py")
    print(result7)
    print()

if __name__ == "__main__":
    main() 