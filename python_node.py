# ComfyUI-PythonNode/python_node.py

import io
import sys

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

def register_node(c):
    # Ensure RETURN_TYPES is a tuple, not a string
    assert not isinstance(c.RETURN_TYPES, str), "Error: string found instead of tuple."
    # Ensure RETURN_NAMES is a tuple, not a string
    assert not isinstance(c.RETURN_NAMES, str), "Error: string found instead of tuple."
    NODE_CLASS_MAPPINGS[c.__name__] = c
    NODE_DISPLAY_NAME_MAPPINGS[c.__name__] = "Execute Python Code"  # Display name in the right-click menu
    return c

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        # Allow matching with any type
        return False

ANY_TYPE = AnyType("*")

@register_node
class ExecPythonNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (ANY_TYPE,),  # Accept any type
                "code": ("STRING", {
                    "multiline": True,
                    "default": "# Write Python code here\n# 'value' is ANY_TYPE, assign 'result' (must match upstream/downstream type)\nprint(\"value=\", value)\nresult = value"
                }),
            }
        }

    RETURN_TYPES = (ANY_TYPE, "STRING",)  # Outputs: result and debug_output
    RETURN_NAMES = ("result", "debug_output",)  # Renamed to debug_output
    FUNCTION = "execute"
    CATEGORY = "python_node"  # Category name in the right-click menu

    def execute(self, value, code):
        local_vars = {"value": value}
        
        # Redirect stdout to capture print() output
        output_capture = io.StringIO()
        sys.stdout = output_capture
        
        try:
            # Execute the code
            exec(code, {}, local_vars)
            # Restore stdout
            sys.stdout = sys.__stdout__
            # Get result, raise error if not assigned
            if "result" not in local_vars:
                raise ValueError("Result must be assigned in the code")
            result = local_vars["result"]
            captured_output = output_capture.getvalue()
            # Return result and captured output (or "No output" if empty)
            return (result, captured_output if captured_output else "No output")
        except Exception as e:
            # Restore stdout on error
            sys.stdout = sys.__stdout__
            error_msg = f"Error: {str(e)}"
            # Return None and error message on exception
            return (None, error_msg)