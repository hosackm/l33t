def word_break_dynamic(s: str, words: list[str]) -> bool:
    """
    'leetcode', ['leet', 'code']
    dp[len(s)] = True
    dp[7] = False
    dp[6] = False
    dp[5] = False
    dp[4] = True and dp[4+len(match)]
    dp[3] = False
    dp[2] = False
    dp[1] = False
    dp[0] = True and dp[len(match)]
    """
    dp = [False] * len(s)
    dp.append(True)  # past the end of the string
    n = len(s) - 1
    while n >= 0:
        for word in words:
            if n + len(word) > len(s):
                continue
            if word == s[n : n + len(word)]:
                dp[n] = True and dp[n + len(word)]
        n -= 1

    return dp[0]


def word_break(s: str, words: list[str]) -> bool:
    """
    Return True if the string s can be created using words
    from words.
    """
    if not s:
        return True

    # if they don't contain the same characters it can't be done
    words_chars = {c for wrd in words for c in wrd}
    for ch in set(s):
        if ch not in words_chars:
            return False

    queue = [s]
    while queue:
        remaining = queue.pop()
        for word in words:
            if word == remaining:
                return True
            elif remaining.startswith(word):
                word_length = len(word)
                queue.append(remaining[word_length:])

    return False


def test_word_break():
    s = "leetcode"
    words = ["leet", "code"]
    assert word_break_dynamic(s, words) == True

    s = "applepenapple"
    words = ["apple", "pen"]
    assert word_break(s, words) == True

    s = "catsandog"
    words = ["cats", "dog", "sand", "and", "cat"]
    assert word_break(s, words) == False

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    words = [
        "a",
        "aa",
        "aaa",
        "aaaa",
        "aaaaa",
        "aaaaaa",
        "aaaaaaa",
        "aaaaaaaa",
        "aaaaaaaaa",
        "aaaaaaaaaa",
    ]
    assert word_break(s, words) == False
    s = "bb"
    words = ["a", "b", "bbb", "bbbb"]
    assert word_break(s, words) == True


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
