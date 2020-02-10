from repo import checkRepo


def making_dict():

    list_repo = checkRepo()

    L= [None]*15


    L.insert(0,list_repo[0][0]) # projectName
    L.insert(1,list_repo[0][9]) # commiterdate / Creation date?
    L.insert(2,list_repo[0][1]) # commit_hash


    L.insert(5,list_repo[0][2]) # component

    L.insert(11,list_repo[0][4]) # Message
    L.insert(14,list_repo[0][3]) # author



    list_keys = ["projectName", "creationDate", "creationCommitHash", "type", "squid", "component", "severity"
                                                                                                    "startLine",
                 "endLine", "resolution", "status", "message", "effort", "debt", "author"]

    # Create a zip object from two lists
    zipbObj = zip(list_keys, L)
    # Create a dictionary from zip object
    dictOfWords = dict(zipbObj)
    # Create a zip object from two lists
    zipbObj = zip(list_keys, L)

    # Create a dictionary from zip object
    dictOfWords = dict(zipbObj)
    
    return dictOfWords



