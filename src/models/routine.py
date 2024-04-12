from .script import Script
from dataclasses import dataclass
from SCons.Environment import Environment


@dataclass
class Routine:
    name: str
    scripts: list[Script]

    def __repr__(self) -> str:
        return f"{self.name} -> {self.scripts}"

    def register(self, env: Environment) -> None:
        alias = env.Alias(self.name, [script.name for script in self.scripts])
        env.AlwaysBuild(alias)
