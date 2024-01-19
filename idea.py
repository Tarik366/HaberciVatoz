ideas = {
    # STUB - "@idea_name": [{"@pname", "@pp", "@pgame", "@pdescription", "@ocm"}]
    "haberci": [{
        "pname": "Shinkansha",
        "pp": "logo.svg",
        "pgame": "Vatozu rakıyla yiyor",
        "pdescription": "",
        "ocm": "Vatozu yedim",
    }],
    # ...
}

#TODO - ideas dict'inden @pname üzerinden verileri çek ve bir class içerisinde bu bilgiyi döndür.
# The function that gather the idea
def get_idea(idea):
    mainIdeaDict = ideas
    try:
        ideaDict = mainIdeaDict.get(idea)[0]
        class ideaClass:
            name = ideaDict.get("pname")
            pp = ideaDict.get("pp")
            game = ideaDict.get("pgame")
            description = ideaDict.get("pdescription")
            ocm = ideaDict.get("ocm")
        return ideaClass
    except:
        e = "Bir hata oluştu"
        return e

# a = get_idea("haberci")
