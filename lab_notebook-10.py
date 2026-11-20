# === Stage 10: Текстовый поиск ===
# Project: LabNotebook
def highlight_lines(text, needle):
    """Return lines of `text` with every occurrence of `needle` (case-insensitive)
    wrapped in ANSI escape sequences: \x1b[31m (red) ... \x1b[0m (reset)."""
    needle = needle.strip()
    if not needle:
        return list(text)

    pattern = re.compile(re.escape(needle), re.IGNORECASE)
    markers = []
    for index, line in enumerate(text):
        if pattern.search(line):
            markers.append(index)

    result = []
    cursor = 0
    for marker in markers:
        result.append(text[cursor:marker])
        result.append(re.sub(pattern, r"\x1b[31m\1\x1b[0m", text[marker:marker + 1]))
        cursor = marker + 1
    result.append(text[cursor:])
    return result


def search_experiments(experiments, query):
    """Search experiments by their textual fields (name, sample, date, owner).
    Returns a list of (line_number, matched_text) tuples where matched_text is
    the experiment rendered as a single string with highlights applied."""
    def render(experiment):
        return "\t".join(str(getattr(experiment, field, "")) for field in
                         ("name", "sample", "date", "owner"))

    matches = []
    for number, experiment in enumerate(experiments, start=1):
        rendered = render(experiment)
        for line in highlight_lines(rendered, query):
            matches.append((number, line))
    return matches


if __name__ == "__main__":
    import json

    data = json.loads(
        json.dumps([
            {"name": "Spectrophotometry of copper sulfate", "sample": "CuSO4 solution",
             "date": "2024-05-12", "owner": "Alice"},
            {"name": "Titration of sodium hydroxide", "sample": "NaOH pellets",
             "date": "2024-05-13", "owner": "Bob"},
            {"name": "pH measurement of vinegar", "sample": "vinegar",
             "date": "2024-05-14", "owner": "Carol"},
        ], ensure_ascii=False)
    )

    query = "SOLUTION"
    print(f"Search for: {query!r}")
    print("-" * 60)
    for line_number, line in search_experiments(data, query):
        print(f"Experiment #{line_number}:\n{line}\n")
