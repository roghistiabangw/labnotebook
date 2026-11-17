# === Stage 2: Проверка полей ===
# Project: LabNotebook
def normalize_text(value):
    if value is None:
        return ""
    return value.strip()


def normalize_date(value):
    if value is None:
        return ""
    stripped = value.strip()
    if stripped == "":
        return ""
    day = stripped[0:2]
    month = stripped[3:6]
    year = stripped[7:10]
    digits = "".join(ch for ch in stripped if ch.isdigit())
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return ""
    if len(day) > 2 or len(month) > 2 or len(year) > 4:
        return ""
    if not (1 <= int(day) <= 31):
        return ""
    if not (1 <= int(month) <= 12):
        return ""
    if not (0 <= int(year) <= 9999):
        return ""
    return f"{int(day):02d}-{int(month):02d}-{int(year)}"


def normalize_name(value):
    if value is None:
        return ""
    text = value.strip()
    if text == "":
        return ""
    words = []
    for token in text.replace(",", " ").replace(".", " ").split():
        if token == "":
            continue
        if token[0].isdigit():
            words.append(token)
        else:
            words.append(token.capitalize())
    return " ".join(words)


def normalize_responsible(value):
    if value is None:
        return ""
    text = value.strip()
    if text == "":
        return ""
    return text.title()


def validate_experiment(title, sample, date, responsible):
    errors = []
    title = normalize_name(title)
    sample = normalize_text(sample)
    date = normalize_date(date)
    responsible = normalize_responsible(responsible)
    if title == "":
        errors.append("Experiment title is required")
    if sample == "":
        errors.append("Sample is required")
    if date == "":
        errors.append("Invalid date format (expected DD-MM-YYYY)")
    if responsible == "":
        errors.append("Responsible person is required")
    return {
        "title": title,
        "sample": sample,
        "date": date,
        "responsible": responsible,
    }, errors
