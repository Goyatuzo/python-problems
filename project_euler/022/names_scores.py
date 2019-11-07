
def quantify_name(name: str, idx: int) -> int:
    # Since a is 1
    a_code = ord('A') - 1

    name_total = 0
    for letter in name:
        name_total += ord(letter) - a_code

    return name_total * idx

if __name__ == '__main__':
    with open('./names.txt', 'r') as c_file:
        content = c_file.read()
