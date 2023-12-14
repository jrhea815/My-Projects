class FakeInput:
    """Context manager to allow input mocking.
    Developed for use with doctests, but works elsewhere.
    Original concept from https://pyquestions.com/doctesting-functions-that-receive-and-display-user-input-python-tearing-my-hair-out
    Wrapped in a context manager so sys.stdin gets reset automatically
    Converts all values passed to it to str, so FakeInput(2, 4, 6, 8) is OK
    You can either:
    - paste this class directly into your code, or
    - put this code into fakeinput.py in the same folder as your script,
      and add the following line to your script:
        from fakeinput import FakeInput
    >>> with FakeInput(""): input()
    ''
    >>> with FakeInput("Doc"): print("What's up, " + input("Your name? ") + "?")
    Your name? What's up, Doc?
    >>> with FakeInput(2, "bla", None): [input() for _ in range(3)]
    ['2', 'bla', 'None']
    """
    def __init__(self, *values):
        self.values = values
    def __enter__(self):
        import io, sys
        self.old_stdin = sys.stdin
        sys.stdin = io.StringIO("\n".join(map(str, self.values)) + "\n")
    def __exit__(self, *rest):
        import sys
        sys.stdin = self.old_stdin

if __name__ == "__main__":
    import doctest
    doctest.testmod()