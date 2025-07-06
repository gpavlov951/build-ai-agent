# Calculator

A command-line calculator application that evaluates mathematical expressions using infix notation with proper operator precedence. The calculator features a beautiful ASCII box rendering for results and robust error handling.

## Features

- **Infix Notation**: Natural mathematical expression input (e.g., "3 + 5 \* 2")
- **Operator Precedence**: Correctly handles order of operations
- **ASCII Box Rendering**: Beautiful formatted output with Unicode box characters
- **Error Handling**: Comprehensive error messages for invalid expressions
- **Float Support**: Handles both integer and floating-point numbers
- **Multiple Operators**: Supports addition (+), subtraction (-), multiplication (\*), and division (/)

## Usage

### Basic Usage

```bash
python main.py "<expression>"
```

### Examples

```bash
# Simple addition
python main.py "3 + 5"

# Order of operations
python main.py "3 + 5 * 2"

# Division with floating-point result
python main.py "10 / 3"

# Complex expression
python main.py "2 + 3 * 4 - 1"
```

### Example Output

```
┌─────────────┐
│  3 + 5 * 2  │
│             │
│  =          │
│             │
│  13         │
└─────────────┘
```

## Project Structure

```
calculator/
├── main.py              # Entry point and command-line interface
├── pkg/                 # Calculator package
│   ├── __init__.py         # Package initialization
│   ├── calculator.py       # Core calculator logic
│   └── render.py          # ASCII box rendering
├── tests.py            # Test suite
└── README.md           # This file
```

## Implementation Details

### Calculator Class (`pkg/calculator.py`)

The core calculator uses a stack-based algorithm to evaluate infix expressions:

- **Operator Precedence**: Multiplication and division have higher precedence than addition and subtraction
- **Token Parsing**: Splits expressions on whitespace and processes each token
- **Stack-Based Evaluation**: Uses two stacks (values and operators) for proper precedence handling
- **Error Handling**: Validates tokens and ensures proper expression structure

### Rendering (`pkg/render.py`)

The render function creates beautiful ASCII box output:

- **Dynamic Sizing**: Box width adapts to the longest line (expression or result)
- **Integer Formatting**: Displays integers without decimal points
- **Unicode Box Characters**: Uses ┌┐└┘─│ for clean box rendering

### Supported Operations

| Operator | Description    | Precedence |
| -------- | -------------- | ---------- |
| `+`      | Addition       | 1          |
| `-`      | Subtraction    | 1          |
| `*`      | Multiplication | 2          |
| `/`      | Division       | 2          |

## Error Handling

The calculator provides clear error messages for various scenarios:

- **Invalid Tokens**: Non-numeric values that aren't operators
- **Invalid Expressions**: Malformed expressions with incorrect operator/operand ratios
- **Division by Zero**: Handled by Python's built-in float division
- **Missing Operands**: Insufficient operands for operators

## Testing

Run the test suite to verify functionality:

```bash
python tests.py
```

## Integration with AI Agent

This calculator serves as a working example for the main AI agent project. The AI can:

- Analyze the calculator code
- Run tests to verify functionality
- Execute calculator operations
- Modify and improve the implementation
- Debug issues and suggest optimizations

## Future Enhancements

Potential improvements could include:

- **Parentheses Support**: Add support for grouped expressions
- **Additional Operators**: Power, modulo, etc.
- **Mathematical Functions**: sin, cos, sqrt, etc.
- **Variable Support**: Store and use variables
- **History**: Keep track of previous calculations
- **Interactive Mode**: REPL-style interface

## Contributing

Feel free to contribute improvements, additional operators, or enhanced rendering features.
