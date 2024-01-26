import os 

class SubstringFunction:
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ('STRING', {"multiline": True}),
                "length": ('INT', {"default": 75, "min": 0}) 
            }
        }

    RETURN_TYPES = ('STRING',)
    FUNCTION = "exec"
    CATEGORY = "utils"
    OUTPUT_NODE = True

    def exec(self, text, length):
        if text == "undefined":
            text = ""
        
        out = text[:length]
        return {"ui": {"text": (out,)}, "result": (out,)}
        
NODE_CLASS_MAPPINGS = {
    "SubstringTheory": SubstringFunction,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SubstringTheory": "Substring Node"
}
