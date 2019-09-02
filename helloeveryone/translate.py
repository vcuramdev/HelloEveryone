#!/usr/bin/env python3

from random import choice
from time import sleep
from google.cloud import translate_v3beta1 as translate


def main():


    # Instantiates a client
    client = translate.TranslationServiceClient()

    project_id = "hello-everyone-240322"
    location = "global"

    parent = client.location_path(project_id, location)

    # The text to translate
    text = "Hello, everyone"

    # The target language
    target = choice(client.get_supported_languages(parent).languages).language_code

    # Translation
    resp = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type='text/plain',  # mime types: text/plain, text/html
        source_language_code='en-US',
        target_language_code=target
    )

    for translation in resp.translations:
        print(f"'{target}' -> '{translation.translated_text}'")

    # ----------------------------------------


if __name__ == "__main__":
    main()
