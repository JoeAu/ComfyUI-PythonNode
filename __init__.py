# ComfyUI-PythonNode/__init__.py

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

from .python_node import NODE_CLASS_MAPPINGS as mappings, NODE_DISPLAY_NAME_MAPPINGS as display_mappings

NODE_CLASS_MAPPINGS.update(mappings)
NODE_DISPLAY_NAME_MAPPINGS.update(display_mappings)