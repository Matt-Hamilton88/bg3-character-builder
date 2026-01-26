from rich import print
from rich.panel import Panel
class Build:
    def __init__(self, cls, subclass, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.cls = cls
        self.subclass = subclass
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma

    def summary(self):
        return (
            f"{self.cls} ({self.subclass}) — "
            f"STR {self.str}, DEX {self.dex}, CON {self.con}, "
            f"INT {self.int}, WIS {self.wis}, CHA {self.cha}"
        )
    def ability_modifiers(self):
        def mod(score):
            return (score - 10) // 2

        return {
            "STR": mod(self.str),
            "DEX": mod(self.dex),
            "CON": mod(self.con),
            "INT": mod(self.int),
            "WIS": mod(self.wis),
            "CHA": mod(self.cha)
        }
    def armor_class(self):
        mods = self.ability_modifiers()
        return 10 + mods["DEX"] + mods["WIS"]
# Temporary test
if __name__ == "__main__":
    test_build = Build("Monk", "Way of Four Elements", 16, 16, 14, 10, 14, 8)

    summary_text = test_build.summary()
    mods = test_build.ability_modifiers()
    ac = test_build.armor_class()

    print(
        Panel(
            f"[bold cyan]{summary_text}[/bold cyan]\n"
            f"[yellow]Modifiers:[/yellow] {mods}\n"
            f"[green]AC:[/green] {ac}",
            title="Build Summary",
            border_style="bright_magenta"
        )
    )