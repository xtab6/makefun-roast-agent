import os

LINE = (
    # The roast: one line, 1-200 chars, the agent's side of the desk.
    "My agent writes 4,000-token plans to avoid work, then asks me to approve "
    "the plan so it can avoid working with permission."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    # One roast, written and printed: fully deterministic.
    main()
