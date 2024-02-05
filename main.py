import regex as re
class SegregationError(Exception):
    pass
def read_source_file(file_path=""):
    """Function reading source .txt file.
    Returns list of lines inside the file."""

    try:
        with open(file_path, "r", encoding="utf8") as file:
            file_content = file.readlines()
            return file_content
    except UnicodeError:
        print("UnicodeError encountered. Check the file contents.")


def sort_line(line=""):

    try:
        assert line
        ord_line = [ord(c) for c in line]
        if 10 in ord_line: ord_line.remove(10)
        if ord_line.count(12288) == 2:
            index_1 = ord_line.index(12288)
            index_2 = ord_line[index_1+1:].index(12288) + index_1 + 1
        else:
            raise SegregationError

        chr_list = lambda x: ('').join(list(map(chr, x)))
        line_part_1 = chr_list(ord_line[:index_1])
        line_part_2 = chr_list(ord_line[index_1+1:index_2])
        line_part_3 = chr_list(ord_line[index_2+1:])

        result = [line_part_1, line_part_2, line_part_3]

        return result

    except AssertionError:
        print("Empty line encountered at line sorting.")
        return -1


if __name__ == "__main__":
    sample = read_source_file(r"samples\vocab_26.txt")
    sorted_sample = sort_line(sample[0])
    # print(sorted_sample)
    ord_sample = [ord(c) for c in sample[0]]
    char_sample = list(map(chr, ord_sample))
    # print(ord_sample)
    # print(char_sample)
    print(sort_line(sample[0])[2])
    print(sort_line(sample[1]))
