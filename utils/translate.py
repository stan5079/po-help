import os
import re

from googletrans import Translator


def translate_po(
        file_path: str,
        dest_lang_code: str,
        src_lang_code: str = 'en'
) -> None:
    """Translate .po files with the given language. Concatenated text is required."""

    old_file_path = file_path
    old_file = open(file_path, 'r')
    new_file_path = f'{file_path}_'
    new_file = open(new_file_path, 'a')

    translator = Translator()
    text = None

    while True:
        line = old_file.readline()
        if line == '':
            break
        line_strip = line.strip()

        match_msgid = re.fullmatch(r'^msgid "(.*)"$', line_strip)
        match_msgstr = re.fullmatch(r'^msgstr "(.*)"$', line_strip)

        if match_msgid:
            text = match_msgid.group(1)
            line_text = match_msgid.string
        elif match_msgstr:
            if text:
                translation = translator.translate(text, dest=dest_lang_code, src=src_lang_code)
                translation_text = translation.text
                line_text = f'msgstr "{translation_text}"'
            else:
                line_text = match_msgstr.string
            text = None
        else:
            line_text = line_strip

        new_file.write(f'{line_text}\n')

    os.remove(old_file_path)
    os.rename(new_file_path, old_file_path)
