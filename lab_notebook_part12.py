# === Stage 12: Постраничный вывод ===
# Project: LabNotebook
from typing import List, Tuple


def paginate(items, page, size):
    if size <= 0:
        raise ValueError("page size must be a positive integer")
    if page <= 0:
        raise ValueError("page number must be a positive integer")
    total_pages = (len(items) + size - 1) // size
    if page > total_pages:
        return [], total_pages
    start = (page - 1) * size
    return items[start:start + size], total_pages


class LabNotebookPaginator:
    def __init__(self, experiments):
        self.experiments = experiments

    def page(self, page, size):
        items, total_pages = paginate(self.experiments, page, size)
        return items, total_pages

    def page_count(self, size):
        if size <= 0:
            return 0
        return (len(self.experiments) + size - 1) // size
