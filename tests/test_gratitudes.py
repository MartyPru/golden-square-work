from lib.gratitudes import *

def tests_gratitudes_class():
    grateful = Gratitudes()
    grateful.add("Good health")
    grateful.add("Friends")
    grateful.add("Opportunities")
    list_of_gratitudes = grateful.format()
    assert list_of_gratitudes == "Be grateful for: Good health, Friends, Opportunities"