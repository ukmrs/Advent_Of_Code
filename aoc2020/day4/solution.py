#!/usr/bin/env python3
from validate_funcs import airport_scanner


def parse_documents(file_name):
    all_docs = []
    current_doc = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                current_doc += line.split(" ")
            else:
                all_docs.append(current_doc.copy())
                current_doc.clear()
        if current_doc:
            all_docs.append(current_doc.copy())

    return all_docs


def part1_validation(docs):
    for doc in docs:
        if len(doc) == 8:
            yield doc
        elif len(doc) == 7:
            for field in doc:
                if field[:3] == "cid":
                    break
            else:
                yield doc


def part1(docs):
    valid = 0
    for _ in part1_validation(docs):
        valid += 1
    return valid


def part2(docs):
    valid = 0
    for doc in part1_validation(docs):
        for field in doc:
            k, v = field.split(":")
            if not airport_scanner[k](v):
                break
        else:
            valid += 1

    return valid


def main():
    parsed = parse_documents("input")
    print(f"part1: {part1(parsed)}")  # 233
    print(f"part2: {part2(parsed)}")  # 111


if __name__ == "__main__":
    main()
