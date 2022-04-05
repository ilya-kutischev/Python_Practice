def sting_tally(text: str, *words) -> dict:
    return {word: text.lower().split().count(word) for word in words}


if __name__ == '__main__':
    test_string = """
    roma roma
    alina sasha
    """
    print(sting_tally(test_string, 'roma', 'sasha'))