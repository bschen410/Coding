dic = {
    "vocabulary": [
        {
            "word": "accommodation",
            "phonetic": "ˌæk.ə.moʊˈdeɪ.ʃən",
            "translation": "n. 住宿，住處",
            "questions_asked": 0,
            "mistakes_made": 0,
        },
        {
            "word": "delegate",
            "phonetic": "ˈdel.ɪ.ɡət",
            "translation": "n. 代表；v. 委託",
            "questions_asked": 0,
            "mistakes_made": 0,
        },
        {
            "word": "convention",
            "phonetic": "kənˈven.ʃən",
            "translation": "n. 會議，大會",
            "questions_asked": 0,
            "mistakes_made": 0,
        },
        {
            "word": "emphasize",
            "phonetic": "ˈem.fə.saɪz",
            "translation": "v. 強調，使突出",
            "questions_asked": 0,
            "mistakes_made": 0,
        },
        {
            "word": "submit",
            "phonetic": "səbˈmɪt",
            "translation": "v. 提交，繳交",
            "questions_asked": 0,
            "mistakes_made": 0,
        },
    ]
}

for i in range(len(dic["vocabulary"])):
    del dic["vocabulary"][i]["phonetic"]
    str = dic["vocabulary"][i]["translation"].split("；")
    if len(str) > 1:
        dic["vocabulary"].append(dic["vocabulary"][i].copy())
        dic["vocabulary"][i]["translation"] = str[0]
        dic["vocabulary"][len(dic["vocabulary"]) - 1]["translation"] = str[1]

for i in range(len(dic["vocabulary"])):
    tmp = dic["vocabulary"][i]["translation"].split()
    dic["vocabulary"][i]["translation"] = tmp[1]
    dic["vocabulary"][i]["speech"] = tmp[0]

print(dic)
