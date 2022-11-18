import pandas as pd
import requests as re
userNames = ['anirudh-senani', 'kuldeepsdk']
listLanguages = []
for user in userNames:
    repos = re.get('https://api.github.com/users/'+user+'/repos').json()
    for repo in repos:
        repoName = (repo["name"])
        print(repoName)
        languageUrl = 'https://api.github.com/repos/'+user+'/'+repoName+'/languages'
        repoLanguages = re.get(languageUrl).json()
        for lang in repoLanguages:
            # print(lang)
            listLanguages.append(lang)


def sortandgrouplistitems(lst):
    print("inside sortandgrouplistitems")
    lst.sort()
   
    langDictionary = {"languages": lst}
    df = pd.DataFrame(langDictionary)
    df2 = df.groupby(["languages"])["languages"].count().sort_values(ascending=False)
    print(df2.aggregate)
    df3 = df2.head(5)
    print("Top % Langugaes:", df3)
    # print(df.groupby().mean()).nlargest(5)
    print("sortandgrouplistitems completed")
sortandgrouplistitems(listLanguages)