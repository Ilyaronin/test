meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное",
    "РОФЛ": "- шутка",
    "ЩИЩ": "- одобрение или восторг",
    "КРИПОВЫЙ": "- страшный, пугающий",
    "АГРИТЬСЯ": "- злиться"
}

word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict:
    print(f"{word}: {meme_dict[word]}")
else:
    print("Этого слова нету в словаре")
