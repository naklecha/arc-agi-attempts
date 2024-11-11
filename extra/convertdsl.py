import ast
from typing import List

def extract_function_signatures(filename: str) -> str:
    """
    Extract function signatures and docstrings from a Python file,
    preserving type hints and docstrings.
    """
    with open(filename, 'r') as file:
        tree = ast.parse(file.read())
    
    # First collect imports and type definitions
    imports_and_types = []
    signatures = []
    
    for node in tree.body:
        # Handle imports
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports_and_types.append(ast.unparse(node))
        # Handle type assignments
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    imports_and_types.append(ast.unparse(node))
        # Handle functions
        elif isinstance(node, ast.FunctionDef):
            # Get the function signature
            returns = ast.unparse(node.returns) if node.returns else 'None'
            
            # Build arguments string with type hints
            args = []
            for arg in node.args.args:
                if arg.annotation:
                    args.append(f"{arg.arg}: {ast.unparse(arg.annotation)}")
                else:
                    args.append(arg.arg)
            
            args_str = ", ".join(args)
            
            # Get docstring if it exists
            docstring = ast.get_docstring(node) or ""
            docstring = f'\n    """ {docstring} """' if docstring else ""
            
            # Construct the function signature
            signature = f"def {node.name}({args_str}) -> {returns}:{docstring}"
            signatures.append(signature)
            
    # Combine everything
    result = "\n".join(imports_and_types) + "\n\n" + "\n\n".join(signatures)
    return result

def main():
    """Main function to process the input file and write the output."""
    input_filename = "../dsl.py"
    output_filename = "dsl_signatures.py"
    
    try:
        result = extract_function_signatures(input_filename)
        
        with open(output_filename, 'w') as file:
            file.write(result)
        
        print(f"Successfully extracted signatures to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file '{input_filename}'")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()