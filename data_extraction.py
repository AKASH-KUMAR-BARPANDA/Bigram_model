def data_extractor(file_path:str):

    with open(file_path,"r",encoding="utf-8") as F:
        text = F.read()
        return text