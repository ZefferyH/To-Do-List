import ast
def string_to_dict(string):
    try:
        result = ast.literal_eval(string)
        if isinstance(result, dict):
            return result
        else:
            raise ValueError("The evaluated result is not a dictionary")
    except (SyntaxError, ValueError) as e:
        return None
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')