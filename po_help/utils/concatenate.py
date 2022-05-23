import os
import re


def concatenate_strings(
        file_path: str,
        prefix: str
) -> None:
    """Concatenate multi-line strings with the given prefix."""

    old_file_path = file_path
    old_file = open(file_path, 'r')
    new_file_path = f'{file_path}_'
    new_file = open(new_file_path, 'a')

    text = None

    while True:
        line = old_file.readline()
        if line == '':
            break
        line_strip = line.strip()

        match_intro = re.fullmatch(r'^"(.*?)(\\n)"$', line_strip)
        match_prefix = re.fullmatch(rf'^{prefix} "(.*)"$', line_strip)
        match_text = re.fullmatch(r'^"(.*)"$', line_strip)

        if match_intro:
            continue
        if match_prefix:
            text = match_prefix.group(1)
        elif match_text and text is not None:
            text += match_text.group(1)
        else:
            if text is not None:
                new_file.write(f'{prefix} "{text}"\n')
            new_file.write(f'{line_strip}\n')
            text = None

    os.remove(old_file_path)
    os.rename(new_file_path, old_file_path)
