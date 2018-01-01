# TranslateSRT
Have you a film that you always wanted to watch but couldn't because it was in a foreign language?
Fear not, TranslateSRT to the rescue! TranslateSRT is a subtitle translator that uses the [DeepL](https://www.deepl.com/)
translation service to perform its translations.

## Prerequisites
* [Python 3.6](https://www.python.org/) : Serpentine, but not pearly
* [pydeepl](https://github.com/EmilioK97/pydeepl) : a Python API wrapper for DeepL translation services
* [pysrt](https://pypi.python.org/pypi/pysrt) : a Python library to edit and create SubRip files
## Usage
`python3 main.py [-h] [-d [IN_LANG]] [infile] [outfile] [translateto]`


Example:


`python3 main.py -d EN sample.srt out.srt FR`


You can find both `sample.srt` and `out.srt` in this repo.

## License
This project is licensed under the [MIT License](LICENSE).