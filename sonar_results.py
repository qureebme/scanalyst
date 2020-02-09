list1 = []


#f= open("text.txt,"r")



def making_dict(list1):
    list1 = ["commons-daemon", "2020-09", "d3421394", "CODE_SMELL", "etc", "etc", "etc..."]
    something_more = ["CODE_SMELL", "41414", "NOT IMPORTANT", "HEHE"]
    list_keys = ["projectName", "creationDate", "creationCommitHash", "type", "squid", "component", "severity"
                                                                                                    "startLine",
                 "endLine", "resolution", "status", "message", "effort", "debt", "author"]
    something_str = ["number", "age", "id", "something"]
    # Create a zip object from two lists
    zipbObj = zip(list_keys, list1)
    # Create a dictionary from zip object
    dictOfWords = dict(zipbObj)
    # Create a zip object from two lists
    zipbObj = zip(list_keys, list1)

    # Create a dictionary from zip object
    dictOfWords = dict(zipbObj)
    #print(dictOfWords)
    return dictOfWords

making_dict(list1)