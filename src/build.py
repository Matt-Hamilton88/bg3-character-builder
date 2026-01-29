from rich import print
from rich.panel import Panel

# -----------------------------------------
# CharacterClass system goes HERE
# -----------------------------------------

class CharacterClass:
    def __init__(self, name, hit_die, saving_throws, armor_proficiencies):
        self.name = name
        self.hit_die = hit_die
        self.saving_throws = saving_throws
        self.armor_proficiencies = armor_proficiencies

# Monk Class
Monk = CharacterClass(
    name="Monk",
    hit_die=8,
    saving_throws=["DEX", "WIS"],
    armor_proficiencies=[]
)

# Fighter Class
Fighter = CharacterClass(
    name="Fighter",
    hit_die=10,
    saving_throws=["STR", "CON"],
    armor_proficiencies=["Light", "Medium", "Heavy", "Shield"]
)

# Barbarian Class
Barbarian = CharacterClass(
    name="Barbarian",
    hit_die=12,
    saving_throws=["STR", "CON"],
    armor_proficiencies=["Light", "Medium", "Shield"]
)

# Bard Class
Bard = CharacterClass(
    name="Bard",
    hit_die=8,
    saving_throws=["DEX", "CHA"],
    armor_proficiencies=["Light"]
)

# Cleric Class
Cleric = CharacterClass(
    name="Cleric",
    hit_die=8,
    saving_throws=["WIS", "CHA"],
    armor_proficiencies=["Light", "Medium", "Shield"]
)

# Druid Class
Druid = CharacterClass(
    name="Druid",
    hit_die=8,
    saving_throws=["WIS", "INT"],
    armor_proficiencies=["Light", "Medium", "Shield"]
)

# Paladin Class
Paladin = CharacterClass(
    name="Paladin",
    hit_die=10,
    saving_throws=["WIS", "CHA"],
    armor_proficiencies=["Light", "Medium", "Heavy", "Shield"]
)

# Ranger Class
Ranger = CharacterClass(
    name="Ranger",
    hit_die=10,
    saving_throws=["DEX", "WIS"],
    armor_proficiencies=["Light", "Medium", "Shield"]
)

# Rogue Class
Rogue = CharacterClass(
    name="Rogue",
    hit_die=8,
    saving_throws=["DEX", "INT"],
    armor_proficiencies=["Light"]
)

# Sorcerer Class
Sorcerer = CharacterClass(
    name="Sorcerer",
    hit_die=6,
    saving_throws=["CON", "CHA"],
    armor_proficiencies=[]
)

# Warlock Class
Warlock = CharacterClass(
    name="Warlock",
    hit_die=8,
    saving_throws=["WIS", "CHA"],
    armor_proficiencies=["Light"]
)

# Wizard Class
Wizard = CharacterClass(
    name="Wizard",
    hit_die=6,
    saving_throws=["INT", "WIS"],
    armor_proficiencies=[]
)
# -----------------------------------------
# Build class stays below this
# -----------------------------------------

class Build:
    def __init__(self, cls, subclass, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.cls= cls
        self.subclass = subclass
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma

    def summary(self):
        return (
            f"{self.cls.name} ({self.subclass}) - "
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
            "CHA": mod(self.cha),
        }

    def armor_class(self):
        mods = self.ability_modifiers()
        return 10 + mods["DEX"] + mods["WIS"]

    def starting_hp(self):
        mods = self.ability_modifiers()
        return self.cls.hit_die + mods["CON"]
# -----------------------------------------
# Temporary test
# -----------------------------------------

if __name__ == "__main__":
    test_build = Build(Druid, "Way of Four Elements", 16, 16, 14, 10, 14, 8)

    summary_text = test_build.summary()
    mods = test_build.ability_modifiers()
    ac = test_build.armor_class()
    hp = test_build.starting_hp()

    print(
        Panel(
            f"[bold cyan]{summary_text}[/bold cyan]\n"
            f"[yellow]Modifiers:[/yellow] {mods}\n"
            f"[green]AC:[/green] {ac}\n"
            f"[red]Starting HP:[/red] {hp}",
            title="Build Summary",
            border_style="bright_magenta"
        )
    )