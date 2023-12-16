from typing import Tuple, List


def menu() -> Tuple[str, List[str], List[str]]:
    """
    show client menu and retrive the params they provided, both that need to go to server and to the client
    return: string with selection, arguments for the server and for the client both string arrays
    """
    options = [
        "ask for time",
        "ask for random",
        "ask for name",
        "notify exit",
        "request DIR",
        "execute a program",
        "copy a file on the remote pc",
        "delete a file",
        "screen shot",
        "fetch a file",
        # "Sign up for the chating service",
        # "Sign in to the chating service",
        # "Get unread messages",
        # "Send a message",
        "copy(with commpression per chunk) a file",
    ]

    for index, option in enumerate(options, start=1):
        print(f"\n  {index}. {option}")

    server_args = []
    client_args = []
    request = input(f"Input 1 - {len(options)} > ")

    count_args = {
        "5": [
            [
                1,
                [
                    "Any Sub directory? (. for current, ../ OR ./ works. may also specify dir name like: .git )"
                ],
            ],
            [0, []],
        ],
        "6": [[1, ["Program name / path to the .exe "]], [0, []]],
        "7": [[2, ["File to copy", "New file name to copy to"]], [0, []]],
        "8": [[1, ["File name to delete"]], [0, []]],
        "9": [[0, ""], [1, ["What Name To grant the screenshot?(end it with .png)"]]],
        "10": [[1, ["Remote file name"]], [1, ["local file name"]]],
        # "11": [[2, ["Username? ", " Password?"]], [0, []]],
        # "12": [[2, ["Username? ", " Password?"]], [0, []]],
        "11": [[1, ["Remote file name"]], [1, ["local file name"]]],
    }
    row = count_args.get(request, [[0, [""]], [0, [""]]])

    for i, req_row in enumerate(row):
        for j in range(req_row[0]):
            (server_args if i == 0 else client_args).append(input(req_row[1][j] + " "))
    if request == "9" and not client_args[0].endswith(".png"):
        client_args[0] = client_args[0] + ".png"
    return request, server_args, client_args
