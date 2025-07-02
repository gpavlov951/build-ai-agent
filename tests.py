from functions.get_files_info import get_files_info


def main():
    """Test the get_files_info function with various scenarios."""
    
    print("Testing get_files_info function...")
    print("=" * 60)
    
    # Test 1: List contents of calculator directory
    print("Test 1: get_files_info('calculator', '.')")
    print("Result for current directory:")
    result1 = get_files_info("calculator", ".")
    print(result1)
    print()
    
    # Test 2: List contents of calculator/pkg directory
    print("Test 2: get_files_info('calculator', 'pkg')")
    print("Result for 'pkg' directory:")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print()
    
    # Test 3: Try to access /bin directory (should fail)
    print("Test 3: get_files_info('calculator', '/bin')")
    print("Result for '/bin' directory:")
    result3 = get_files_info("calculator", "/bin")
    print("    " + result3)
    print()
    
    # Test 4: Try to access parent directory (should fail)
    print("Test 4: get_files_info('calculator', '../')")
    print("Result for '../' directory:")
    result4 = get_files_info("calculator", "../")
    print("    " + result4)
    print()


if __name__ == "__main__":
    main() 