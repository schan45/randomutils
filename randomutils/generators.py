import random
import string

def generate_password(length: int = 12) -> str:
    """
    Generate a random password consisting of letters, digits, and punctuation.

    Parameters
    ----------
    length : int, optional
        Length of the password. Default is 12.

    Returns
    -------
    str
        Randomly generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def random_word(word_list: list[str]) -> str:
    """
    Select a random word from a list.

    Parameters
    ----------
    word_list : list of str
        List of candidate words.

    Returns
    -------
    str
        Randomly chosen word.
    """
    import random
    if not word_list:
        raise ValueError("word_list cannot be empty.")
    return random.choice(word_list)


def random_matrix(rows: int, cols: int, min_val: int = 0, max_val: int = 10) -> list[list[int]]:
    """
    Generate a matrix of random integers.

    Parameters
    ----------
    rows : int
        Number of rows.
    cols : int
        Number of columns.
    min_val : int
        Minimum integer value.
    max_val : int
        Maximum integer value.

    Returns
    -------
    list[list[int]]
        Random integer matrix.
    """
    import random
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def random_dates(start: str, end: str, n: int = 5) -> list[str]:
    """
    Generate random dates between two date strings.

    Parameters
    ----------
    start : str
        Start date in YYYY-MM-DD format.
    end : str
        End date in YYYY-MM-DD format.
    n : int
        Number of dates to generate.

    Returns
    -------
    list[str]
        Random date strings in ISO format.
    """
    from datetime import datetime, timedelta
    import random

    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    delta = (end_date - start_date).days
    if delta < 0:
        raise ValueError("end date must be after start date")
    return [(start_date + timedelta(days=random.randint(0, delta))).date().isoformat() for _ in range(n)]

def generate_pseudoword(length: int = 6) -> str:
    """
    Generate a pseudoword that mimics natural language structure using consonant-vowel alternation.

    Parameters
    ----------
    length : int
        Length of the generated pseudoword.

    Returns
    -------
    str
        A pseudoword (not necessarily meaningful).
    """
    import random

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)

    return word.capitalize()


def random_float_list(n: int, min_val: float = 0.0, max_val: float = 1.0) -> list[float]:
    """
    Generate a list of random float numbers in a range.

    Parameters
    ----------
    n : int
        Number of floats.
    min_val : float
        Minimum value.
    max_val : float
        Maximum value.

    Returns
    -------
    list[float]
        List of random floats.
    """
    import random
    return [random.uniform(min_val, max_val) for _ in range(n)]

def shuffle_list(input_list: list) -> list:
    """
    Return a shuffled version of the input list.

    Parameters
    ----------
    input_list : list
        Original list.

    Returns
    -------
    list
        Shuffled list.
    """
    import random
    new_list = input_list[:]
    random.shuffle(new_list)
    return new_list

def random_int_in_range(start: int, end: int) -> int:
    """
    Generate a random integer between start and end (inclusive).

    Parameters
    ----------
    start : int
        Lower bound of the range.
    end : int
        Upper bound of the range.

    Returns
    -------
    int
        Random integer in the range.
    """
    import random
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    return random.randint(start, end)

def group_random_names(names: list[str], num_groups: int) -> list[list[str]]:
    """
    Véletlenszerűen csoportokra oszt egy névlistát, közel egyenlő létszámú csoportokra.

    Parameters
    ----------
    names : list of str
        A nevek listája.
    num_groups : int
        A csoportok száma.

    Returns
    -------
    list of list of str
        A véletlenszerűen elosztott csoportok.
    """
    import random
    if num_groups <= 0:
        raise ValueError("A csoportok száma legyen pozitív egész szám.")
    if not names:
        raise ValueError("A névlista nem lehet üres.")
    if num_groups > len(names):
        raise ValueError("Több csoport van, mint név.")

    shuffled = names[:]
    random.shuffle(shuffled)
    avg = len(names) // num_groups
    rem = len(names) % num_groups

    groups = []
    i = 0
    for group_index in range(num_groups):
        group_size = avg + (1 if group_index < rem else 0)
        groups.append(shuffled[i:i+group_size])
        i += group_size

    return groups

