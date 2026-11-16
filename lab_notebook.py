# === Stage 1: Каркас модуля ===
# Project: LabNotebook
from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class Experiment:
    name: str
    sample: str
    date: date
    responsible: str


def make_demo_experiments() -> List[Experiment]:
    return [
        Experiment("pH of tap water", "water_sample_01", date(2024, 1, 15), "A. Petrov"),
        Experiment("Melting point of ice", "ice_sample_01", date(2024, 1, 16), "B. Ivanova"),
        Experiment("Conductivity of salt solution", "salt_solution_01", date(2024, 1, 17), "A. Petrov"),
        Experiment("Titration of acetic acid", "vinegar_sample_01", date(2024, 1, 18), "C. Sidorov"),
        Experiment("Density of aluminum", "aluminum_sample_01", date(2024, 1, 19), "B. Ivanova"),
        Experiment("Reaction rate of sodium thiosulfate", "thiosulfate_sample_01", date(2024, 1, 20), "D. Kozlov"),
        Experiment("Absorbance of copper sulfate", "copper_sulfate_sample_01", date(2024, 1, 21), "C. Sidorov"),
        Experiment("Boiling point of ethanol", "ethanol_sample_01", date(2024, 1, 22), "A. Petrov"),
        Experiment("Viscosity of glycerin", "glycerin_sample_01", date(2024, 1, 23), "E. Novikova"),
        Experiment("Osmotic pressure of sucrose solution", "sucrose_sample_01", date(2024, 1, 24), "D. Kozlov"),
    ]


def main() -> None:
    experiments = make_demo_experiments()
    print("LabNotebook")
    print("Lab notebook framework initialized.")
    print(f"Loaded {len(experiments)} demonstration experiments:")
    for exp in experiments:
        print(f"  - {exp.name} (sample: {exp.sample}, date: {exp.date}, responsible: {exp.responsible})")
    print("End of demo.")


if __name__ == "__main__":
    main()
