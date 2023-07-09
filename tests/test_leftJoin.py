from hashmap_leftJoin.hashmap_leftjoin import left_join

def test_left_join():
    synonyms = {"diligent": "employed", "fond": "enamored", "guide": "usher", "outfit": "garb", "wrath": "anger"}
    antonyms = {"diligent": "idle", "fond": "averse", "guide": "follow", "outfit": None, "wrath": "delight"}
    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"],
    ]
    assert left_join(synonyms, antonyms) == expected