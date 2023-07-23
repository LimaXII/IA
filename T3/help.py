def swap_string(string: str, index_x: int, index_y: int) -> str:
    string_list = list(string)
    string_list[index_x], string_list[index_y] = string_list[index_y], string_list[index_x]
    return ''.join(string_list)