# EasyWeb

EasyWeb provides a simple command line tool and a small GUI for generating the
basic files for a website. It creates several starter HTML pages along with
`style.css` and `script.js` inside a directory of your choice. You can also
specify custom pages to generate.

## Usage

Run the package using Python and pass the directory name where you want your
site generated. Optionally specify a custom title for the pages and a list of
pages to create:

```bash
python -m easyweb mysite --title "My Blog" --pages index,login,about
```

Without specifying `--pages` the generator creates several default pages such as
`index.html`, `login.html`, `register.html`, `article.html`, `chat.html` and
`admin.html`. When `--pages` is provided you control the list of pages to
generate. The title of each page uses the directory name or the value passed
with `--title`.

### GUI

You can also run a small graphical interface:

```bash
python -m easyweb.gui
```

Choose a directory, optionally set the site title and provide a comma separated
list of page names. Click **Generate** and the HTML files will be created just
like when using the command line.

## Installation

Install with pip using the included `pyproject.toml`:

```bash
pip install .
```

This installs the command `easyweb` and `easyweb-gui` so you can run the tool
from anywhere.

## License

This project is licensed under the terms of the GNU General Public License v3.0.

---

## 使用指南 (简体中文)

1. 安装：

   ```bash
   pip install .
   ```

2. 命令行生成：

   ```bash
   python -m easyweb mysite --title "我的站点" --pages index,login,about
   ```

   如果未指定 `--pages`，工具会生成默认的多页面模板。

3. 图形界面：

   ```bash
   python -m easyweb.gui
   ```

   在窗口中选择目录、输入站点标题及页面列表，点击 **Generate** 即可生成文件。
