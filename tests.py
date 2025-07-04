from functions.write_file import write_file

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

if __name__ == "__main__":
    main() 