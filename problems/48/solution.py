from collections import defaultdict


def merge_accounts(accounts: list[list[str]]) -> list[list[str]]:
    # build graph/vertices
    visited = {}
    links = defaultdict(list)
    for i, acct in enumerate(accounts):
        emails = acct[1:]
        for email in emails:
            if email in visited:
                existing = visited[email]
                links[existing].append(i)
                links[i].append(existing)
            visited[email] = i

    # for each account, traverse graph and aggregate emails
    merged = {}
    visited = set()
    for i in range(len(accounts)):
        user = []
        if i in visited:
            continue

        queue = [i]
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue

            visited.add(node)
            user.extend(accounts[node][1:])

            for link in links[node]:
                if link not in visited:
                    queue.append(link)

        merged[i] = [accounts[i][0]] + sorted(set(user))

    # convert to list
    return [[v[0]] + v[1:] for v in merged.values()]


def test_accounts_merge():
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    output = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]

    result = merge_accounts(accounts)
    assert result == output

    accounts = [
        ["David", "David0@m.co", "David4@m.co", "David3@m.co"],
        ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
        ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
        ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
        ["David", "David4@m.co", "David1@m.co", "David3@m.co"],
    ]
    output = [
        [
            "David",
            "David0@m.co",
            "David1@m.co",
            "David3@m.co",
            "David4@m.co",
            "David5@m.co",
        ]
    ]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
