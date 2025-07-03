from functions.get_file_content import get_file_content

def main():
    """Test the get_file_content function with various scenarios."""
    
    print("Testing get_file_content function...")
    print("=" * 60)
    
    print("Test 1: get_file_content('calculator', 'lorem.txt')")
    print("Testing truncation with large file:")
    result1 = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(result1)} characters")
    if len(result1) > 10000:
        print("✓ File was truncated as expected")
        print("Last 100 characters:", result1[-100:])
    else:
        print("✗ File was not truncated")
    print()
    
    print("Test 2: get_file_content('calculator', 'main.py')")
    print("Result for main.py:")
    result2 = get_file_content("calculator", "main.py")
    print(result2)
    print()
    
    print("Test 3: get_file_content('calculator', 'pkg/calculator.py')")
    print("Result for pkg/calculator.py:")
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(result3)
    print()
    
    print("Test 4: get_file_content('calculator', '/bin/cat')")
    print("Result for '/bin/cat' (should be error):")
    result4 = get_file_content("calculator", "/bin/cat")
    print("    " + result4)
    print()

if __name__ == "__main__":
    main() 