import json
with open("C://Users//dasari.anirudh//Downloads//words.json","r",encoding="utf-8") as file:
    json_data=file.read()
data=json.loads(json_data)
dict={}
dict_1={}
for i in data:
    key=i["word"]
    #print(key)
    nul=i["meanings"]
    for j in nul:
        key_1=j["partOfSpeech"]
        val_1=j["definitions"]
        #print(val_1)
        list= []
        for m in val_1:
            list.append(m["definition"])
            print(list)
            dict[key_1]=list
            print(dict)
        
        dict_1[key]=dict
        print(dict_1)
with open("C://Users//dasari.anirudh//Downloads//ws.json","w") as file:
    val2=file.write(json.dumps(dict_1,indent=2))
    print(val2)     



       
