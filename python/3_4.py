class ProgrammingLanguage:
    paradigm: str = "Multi-paradigm"
    typing: str = "Static"

    def __init__(
        self,
        name: str,
        creator: str,
        year: int,
        is_compiled: bool,
        popularity: float
    ) -> None:
        self.name: str = name
        self.creator: str = creator
        self.year: int = year
        self.is_compiled: bool = is_compiled
        self.popularity: float = popularity

    def __str__(self) -> str:
        return f"{self.name} ({self.year}), создатель: {self.creator}"

    def get_age(self, current_year: int) -> int:
        return current_year - self.year

    def update_popularity(self, new_popularity: float) -> None:
        self.popularity = new_popularity

    def is_old(self, current_year: int) -> bool:
        return self.get_age(current_year) > 30

    def change_paradigm(self, new_paradigm: str) -> None:
        ProgrammingLanguage.paradigm = new_paradigm


lang1 = ProgrammingLanguage("Python", "Guido van Rossum", 1991, False, 9.8)
lang2 = ProgrammingLanguage("C++", "Bjarne Stroustrup", 1985, True, 8.7)

print(lang1)
print(lang1.get_age(2025))
print(lang2.is_old(2025))

lang1.update_popularity(10.0)
lang2.change_paradigm("Object-Oriented")

print(lang1.popularity)
print(ProgrammingLanguage.paradigm)