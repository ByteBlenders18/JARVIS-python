import assist_fuction


if __name__ == "__main__":

    lang_file = open("text/lang.txt", "r")
    lang = lang_file.read()
    print(lang, type(lang))
    lang_file.close()

    if lang == "en":

        assist_fuction.english_assistant()

    elif lang == "hi":
        assist_fuction.hindi_assistant()
