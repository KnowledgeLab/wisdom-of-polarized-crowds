# This parser uses wikiclass to assess the quality of each page.
import wikiclass
from revscoring.scorer_models import MLScorerModel

columns=['title','quality']

scorer_model = MLScorerModel.load(open("models/enwiki.nettrom_wp10.gradient_boosting.model", "rb"))

def parse(page):
    res=[]
    empty=True
    for rev in page:
        empty=False
        pass
    if empty:
        return res
    res.append(page.title)
    res.append(wikiclass.score(scorer_model, rev.text)['prediction'])
    return [res]
