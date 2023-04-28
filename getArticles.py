import json
import time
import copy
from scholarly import scholarly

SLEEP = 1
START = 0   # BURASI DEGISECEK
END = 10    # BURASI DEGISECEK

with open("universitiesWithIds.json", "r", encoding="utf-8") as f:
    data = json.load(f)

total = 1
uniCount = 1

for uni in data[START:END]:
    name = uni['name']

    print(f'\n{name} ({uniCount}/{END-START})')

    with open(f"./data/{name}.json", "r", encoding="utf-8") as f:
        universityData = json.load(f)

    uniData = copy.deepcopy(universityData)

    for index, author in enumerate(uniData):
        authorId = author.get('scholar_id', None)
        if not authorId:
            continue

        isAuthorFilled = "publications" in author.get('filled', [])
        if isAuthorFilled:
            continue

        time.sleep(SLEEP)

        time1 = time.time()

        authorUnfilled = scholarly.search_author_id(authorId)
        authorFilled = scholarly.fill(
            authorUnfilled, sections=['publications'])

        time2 = time.time()

        articleCount = len(authorFilled.get('publications', []))
        timeSpent = round(time2 - time1, 2)

        print(
            f"found author with {articleCount} articles in {timeSpent} seconds ({total})")

        universityData[index] = authorFilled

        with open(f'./data/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(universityData, f, ensure_ascii=False, indent=4)

        total += 1

    with open(f'./data/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(universityData, f, ensure_ascii=False, indent=4)

    uniCount += 1
