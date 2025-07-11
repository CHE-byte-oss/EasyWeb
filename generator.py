import os
import argparse
from typing import Mapping, MutableMapping

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{title}</title>
    <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
    <h1>{heading}</h1>
    <script src=\"script.js\"></script>
</body>
</html>
"""

CSS_CONTENT = "body {\n    font-family: Arial, sans-serif;\n    margin: 0;\n    padding: 0;\n}\n"

JS_CONTENT = "console.log('Hello from {title}');\n"

DEFAULT_PAGES: Mapping[str, str] = {
    "index.html": "Welcome to {title}",
    "login.html": "Login Page",
    "register.html": "Register Page",
    "article.html": "Article Page",
    "chat.html": "Chat Room",
    "admin.html": "Admin Dashboard",
}

def generate_site(
    path: str,
    title: str | None = None,
    pages: Mapping[str, str] | None = None,
) -> None:
    """Generate basic website files in the given directory.

    Parameters
    ----------
    path:
        Target directory where files should be created.
    title:
        Optional title for the generated pages. If omitted, the directory name
        is used.
    pages:
        Mapping of file names to heading text. When ``None`` the default set of
        pages is created.
    """
    os.makedirs(path, exist_ok=True)
    project_name = title or os.path.basename(os.path.abspath(path))
    page_map: Mapping[str, str] = pages or DEFAULT_PAGES

    for filename, heading in page_map.items():
        with open(os.path.join(path, filename), "w", encoding="utf-8") as f:
            f.write(
                HTML_TEMPLATE.format(
                    title=project_name, heading=heading.format(title=project_name)
                )
            )

    with open(os.path.join(path, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS_CONTENT)

    with open(os.path.join(path, "script.js"), "w", encoding="utf-8") as f:
        f.write(JS_CONTENT.format(title=project_name))


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Generate a simple website skeleton")
    parser.add_argument("directory", help="Directory where files will be created")
    parser.add_argument("--title", help="Custom title for pages", default=None)
    parser.add_argument(
        "--pages",
        help="Comma separated list of page names, e.g. index,login,about",
        default=None,
    )
    args = parser.parse_args(argv)
    page_map = None
    if args.pages:
        names = [n.strip() for n in args.pages.split(",") if n.strip()]
        if names:
            page_map = {f"{n}.html": n.title() for n in names}

    generate_site(args.directory, title=args.title, pages=page_map)

if __name__ == "__main__":
    main()
