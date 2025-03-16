# ComfyUI-PythonNode
A custom ComfyUI node that allows users to execute arbitrary Python code with a single input (value) and output (result), enabling flexible processing of the input value using any Python code before assigning the final result to result. It also captures print() output and exceptions for debugging.

# Features
* Dynamic Input/Output Type: The node accepts any type (ANY_TYPE) as input (value) and ensures the output (result) matches the upstream/downstream type.
* Python Code Execution: Write and execute Python code in a multiline text box (code).
* Debug Output: Captures print() statements and exceptions, outputting them to debug_output as a string.
* Menu Integration: Appears in the right-click "Add Node" menu under the python_node category as "Execute Python Code".
* Type Safety: Enforces that result must be explicitly assigned in the code to maintain type consistency.

# Installation
Clone or Download:
Place the ComfyUI-PythonNode folder into your ComfyUI custom_nodes directory:
```
ComfyUI/custom_nodes/ComfyUI-PythonNode/
```

# Usage
## Node Inputs
value: Any type (ANY_TYPE) input, connected from upstream nodes.
code: A multiline string field where you write Python code. Default value:
```python
# Write Python code here
# 'value' is ANY_TYPE, assign 'result' (must match upstream/downstream type)
print("value=", value)
result = value
```

## Node Outputs
result: The result of the executed code, matching the type of value. Must be assigned in the code.

debug_output: A string containing print() output or error messages from exceptions.

# Safety
The node uses exec() to run user-provided code, which can execute arbitrary Python statements. Use with caution in untrusted environments.

# License
This project is released under the MIT License.
