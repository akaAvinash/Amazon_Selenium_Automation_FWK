import sys
import pytest

def main():
    # If a specific test file is passed as an argument, run only that
    if len(sys.argv) > 1:
        test_target = sys.argv[1]
    else:
        test_target = "Amazon/Tests"  # default to full suite

    pytest.main([test_target, "--html=", "--self-contained-html"])

if __name__ == "__main__":
    main()
