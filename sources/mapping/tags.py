# -*- coding: utf-8 -*-
import jieba


def tags_generator(string):
    results = set()
    for word in jieba.cut_for_search(string):
        if len(word) > 0:
            results.add(word)
        else:
            continue
    assert results
    return results
