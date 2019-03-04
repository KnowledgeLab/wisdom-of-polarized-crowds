# This parser will extract the following information for every edit.

columns=['title','time','user','page_len']

def parse(page):
    res=[]
    for revision in page:
        tmp=[]
        tmp.append(page.title)
        tmp.append(revision.timestamp)
        if (revision.user is not None):
            tmp.append(revision.user.text)
        else:
            tmp.append('')
        if (revision.text is not None):
            tmp.append(len(revision.text))
        else:
            tmp.append(0)
        res.append(tmp)

    return res
