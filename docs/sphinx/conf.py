import re
import shutil
from cgitb import html
from datetime import date
from glob import glob
from walkmate import tree

project = "Miniscons"
version = "0.9.0"

package = "miniscons"
primary = "#4165FF"
secondary = "#914FF5"

project_copyright = f"{date.today().year} Joel Lefkowitz"

extensions = [
    "autoapi.extension",
    "myst_parser",
    "sphinxext.opengraph",
]

autoapi_dirs = ["../../src"]
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "show-inheritance",
]

myst_all_links_external = True

html_theme = "furo"
html_title = project
html_static_path = [""]
html_js_files = ["scripts.js"]
html_css_files = ["styles.css"]
html_theme_options = {
    "font-stack": "Space Grotesk, sans-serif",
    "font-stack--monospace": "CQ Mono, monospace",
    "light_css_variables": {
        "color-brand-content": primary,
        "color-problematic": primary,
        "color-brand-primary": secondary,
        "color-highlight-on-target": "#E0E0E0",
    },
    "dark_css_variables": {
        "color-problematic": primary,
        "color-brand-content": primary,
        "color-brand-primary": secondary,
        "color-highlight-on-target": "#202020",
    },
}


def build(app, build):

    shutil.copytree("docs/images", "docs/dist/docs/images", dirs_exist_ok=True)
    shutil.move("docs/dist/autoapi/src", f"docs/dist/autoapi/{package}")

    pattern = re.compile(r"src(?!\=)")

    for file in tree("docs/dist", r"\.html") + ["docs/dist/searchindex.js"]:
        with open(file, "r") as stream:
            text = pattern.sub(package, stream.read())

        with open(file, "w") as stream:
            stream.write(text)

    for path in glob(f"*.md"):
        shutil.copyfile(path, f"docs/dist/{path}")


def setup(app):
    app.connect("build-finished", build)
