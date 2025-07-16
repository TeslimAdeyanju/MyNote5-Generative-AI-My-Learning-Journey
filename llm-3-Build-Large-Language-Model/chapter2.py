import marimo

__generated_with = "0.14.11"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Chapter 2: Working with Text Data""")
    return


@app.cell
def _():
    from importlib.metadata import version

    print("torch version:", version("torch"))
    print("tiktoken version:", version("tiktoken"))
    return


@app.cell
def _():
    import os
    import urllib.request

    if not os.path.exists("the-verdict.txt"):
        url = ("https://raw.githubusercontent.com/rasbt/"
               "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
               "the-verdict.txt")
        file_path = "the-verdict.txt"
        urllib.request.urlretrieve(url, file_path)
    return


@app.cell
def _():
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    print("Total number of character:", len(raw_text))
    print(raw_text[:99])
    return (raw_text,)


@app.cell
def _():
    import re

    text = "Hello, world. This, is a test."
    result = re.split(r'(\s)', text)

    print(result)
    return re, result, text


@app.cell
def _(re, text):
    result_split = re.split(r'([,.]|\s)', text)

    print(result_split)
    return


@app.cell
def _(result):
    # Strip whitespace from each item and then filter out any empty strings.
    result_split_ = [item for item in result if item.strip()]
    print(result_split_)
    return


@app.cell
def _(re, text):
    text2 = "Hello, world. Is this-- a test?"

    result1 = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    result2 = [item.strip() for item in result1 if item.strip()]
    print(result2)
    return


@app.cell
def _(raw_text, re):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    print(preprocessed[:30])
    return (preprocessed,)


@app.cell
def _(preprocessed):
    print(len(preprocessed))
    return


if __name__ == "__main__":
    app.run()
