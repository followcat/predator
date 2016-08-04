# -*- coding: utf-8 -*-
import jieba


tags = {
    u'医疗': 'Medicine',
    u'器械': 'Equipment',
    u'生物': 'Biotechnology',
    u'制药': 'Pharmaceuticals',
    u'研发': 'R&D',
    u'药品': 'drug',
    u'生产': 'Manufacturing',
    u'质量': 'Quality',
    u'管理': 'Management',
    u'市场': 'Marketing',
    u'总监': 'Director',
    u'销售': 'Sales',
    u'项目': 'Project',
    u'经理': 'Manager',
    u'主管': 'Supervisor',
    u'专员': 'Specialist',
    u'助理': 'Assistant',
    u'质量管理': 'QA',
    u'质量测试': 'QC',
    u'体系': 'Systems',
    u'工程师': 'Engineer',
    u'审核员': 'Auditor',
    u'医药': 'Pharmaceutical',
    u'药品': 'Pharmaceutical',
    u'推广': 'Promotion',
    u'硬件': 'Hardware',
    u'开发': 'Development',
    u'IT' : 'IT',
    u'运维': 'Operation',
    u'技术': 'Technical',
    u'支持': 'Support',
}


def tags_generator(string):
    results = set()
    for word in jieba.cut_for_search(string):
        try:
            results.add(tags[word])
        except KeyError:
            continue
    assert results
    return results
