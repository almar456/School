def lang_genoeg(int):
    if int >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

print(lang_genoeg(203))
print(lang_genoeg(85))