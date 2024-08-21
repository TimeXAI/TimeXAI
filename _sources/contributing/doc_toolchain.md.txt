(doc_toolchain)=
# Documentation toolchain

TimeXAI documentation is built using a Python documentation tool, [Sphinx](https://www.sphinx-doc.org/en/master/).
Sphinx converts `rst`(restructured text) files into HTML websites.
There are different extensions available for converting other types of files
like markdown, jupyter notebooks, etc. into HTML websites.

TimeXAI [docs](https://github.com/TimeXAI-devs/TimeXAI/tree/main/docs/source) consist of `.rst`, `.md` and `.ipynb` files.
It uses `myst-parser` and `myst-nb` for `.md` and `.ipynb` files.
Apart from the content in the `/docs/source` folder, TimeXAI documentation also consists of docstrings.
Docstrings are used in the `.py` files to explain the Python objects parameters and return values.

TimeXAI docs also uses sphinx extensions for style, layout, navbar and putting code in the documentation.

A more detailed overview of the sphinx toolchain used at TimeXAI is available at
{doc}`sphinx-primer:index`
