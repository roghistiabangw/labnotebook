# === Stage 16: Массовое обновление ===
# Project: LabNotebook
from datetime import date


class ChangePreview:
    """Просмотр запланированных изменений для массового обновления опытов."""

    def __init__(self, experiments, field, old_value, new_value):
        self.experiments = experiments
        self.field = field
        self.old_value = old_value
        self.new_value = new_value

    def affected(self):
        return [e for e in self.experiments if getattr(e, self.field) != self.old_value]

    def count(self):
        return len(self.affected())

    def preview(self):
        items = []
        for e in self.affected():
            items.append((getattr(e, self.field), getattr(e, "title")))
        return items


def bulk_update(experiments, field, new_value, preview=True):
    """Массовое обновление поля у опытов, совпадающих по условию.

    При preview=True изменения применяются только к тем опытам,
    которые действительно соответствуют условию, а результат
    возвращается в виде ChangePreview для проверки перед сохранением.
    """
    if preview:
        return ChangePreview(experiments, field, getattr(experiments[0], field), new_value)

    for e in experiments:
        if getattr(e, field) == getattr(experiments[0], field):
            setattr(e, field, new_value)
    return None


if __name__ == "__main__":
    class Experiment:
        def __init__(self, title, sample, date, responsible):
            self.title = title
            self.sample = sample
            self.date = date
            self.responsible = responsible

    samples = ["A", "B", "C"]
    experiments = [
        Experiment("t1", "A", date(2024, 1, 1), "user1"),
        Experiment("t2", "B", date(2024, 1, 2), "user2"),
        Experiment("t3", "A", date(2024, 1, 3), "user3"),
    ]

    preview = bulk_update(experiments, "sample", "A", preview=True)
    print("affected:", preview.count())
    for old, title in preview.preview():
        print("change sample %s -> %s in %s" % (old, preview.new_value, title))

    bulk_update(experiments, "sample", "A")
    for e in experiments:
        print("updated:", e.title, e.sample)
