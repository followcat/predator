# encoding: utf-8
import jieba

from sources.yingcai_industry import industry_list as yingcai_industry
from sources.liepin_wq_dict import industry_list as liepin_industry
from sources.jingying_industry import industry_list as jingying_industry
from sources.zhilian_industry import industry_list as zhilian_industry

def InitIndustry(industry_dict = None):
    industry_list=[]
    for index in industry_dict.keys():
        cn = industry_dict[index].strip()
        industry_list.append(cn)
    return industry_list

def CompeleteMatch(industry_list, industry_dict):
    matchdict={}
    for value in industry_list:
        for key in industry_dict.keys():
            if value == industry_dict[key].strip():
                matchdict[value] = key
    return matchdict

def DeleteMatchItem(industry_dict, matchdict):
    for key in matchdict.keys():
        industry_dict.pop(matchdict[key])
    return industry_dict

def JiebaFenci(string):
    fenci_list=jieba.cut_for_search(string)
    return fenci_list

def FenciMatch(industry_list, industry_dict):
    fenci_match = {}
    for key in industry_dict.keys():
        fenci_match[key]={}
        fenci_match[key][industry_dict[key]]={}
        for value in industry_list:
            tmp_dict={value:0}
            for word in jieba.cut_for_search(industry_dict[key]):
                word = word.strip().encode('utf-8')
                if word !='/' and value.find(word)!=-1:
                    #import ipdb;ipdb.set_trace()
                    tmp_dict[value]+=1
                    fenci_match[key][industry_dict[key]][value]=tmp_dict[value]
                else:
                    continue
    return fenci_match

def FenciMatch2(fenci_match):
    partialmatch_dict={}
    for key in fenci_match.keys():
        #import ipdb;ipdb.set_trace()
        for key_key in fenci_match[key].keys():
            maxnum = -1
            max_index = []
            for key_key_key in fenci_match[key][key_key].keys():
                if fenci_match[key][key_key][key_key_key] >= maxnum:
                    if fenci_match[key][key_key][key_key_key] > maxnum:
                        maxnum = fenci_match[key][key_key][key_key_key]
                        max_index = []
                        max_index.append(key_key_key)
                    else:
                        max_index.append(key_key_key)
            for index in range(len(max_index)):
                partialmatch_dict[max_index[index]]={}
                partialmatch_dict[max_index[index]][key_key]=key
    return partialmatch_dict

def NoneMatch(industry_dict, matchdict, partialmatch,rematchdict):
    nonmatch={}
    tmplist=[]
    tmplist2=[]
    for key2 in partialmatch.keys():
        for key21 in partialmatch[key2].keys():
            tmplist.append(key21)
    for key3 in rematchdict.keys():
        for key31 in rematchdict[key3].keys():
            tmplist2.append(key31)
    for key in industry_dict.keys():
        temp = industry_dict[key]
        if (temp in matchdict.keys()) or (temp in tmplist) or (temp in tmplist2):
            continue
        else:
            nonmatch[key]=temp
            print temp
    return nonmatch

def Match(tags,industrylist, input_industry):
    matchdict = {}
    fencidict = {}
    partialmatchdict = {}
    nonmatch = {}

    renfencidict ={}
    rematchdict = {}
    final_nonmatch = {}
    industry = input_industry

    for key in industry.keys():
        industry[key] = industry[key].encode('utf-8')

    origin_dict = industry

    matchdict = CompeleteMatch(industrylist, origin_dict)
    DeleteMatchItem(origin_dict, matchdict)
    fencidict = FenciMatch(industrylist, origin_dict)
    partialmatchdict = FenciMatch2(fencidict)
    nonmatch = NoneMatch(industry, matchdict, partialmatchdict,rematchdict)
    refencidict = FenciMatch(industrylist, nonmatch)
    rematchdict = FenciMatch2(refencidict)
    final_nonmatch = NoneMatch(industry, matchdict, partialmatchdict,rematchdict)
    final_nonmatch = {v:k for k, v in final_nonmatch.items()}

    return matchdict, partialmatchdict, rematchdict, final_nonmatch
    

def Merge(tags,industrylist,final_dict,process_industry):
    matchdict = {}
    partialmatchdict ={}
    rematchdict = {}
    final_nonmatch = {}
    matchdict, partialmatchdict, rematchdict, final_nonmatch = Match(tags,industrylist, process_industry)
    for value in industrylist:
        final_dict[value][tags]=[]
        if value in matchdict.keys():
            tmp_item = [matchdict[value],value]
            final_dict[value][tags].append(tmp_item)

        if value in partialmatchdict.keys():
            for key_tmp in partialmatchdict[value].keys():
                value_tmp = partialmatchdict[value][key_tmp]
                tmp_item2 = [value_tmp,key_tmp]
                final_dict[value][tags].append(tmp_item2)

        if value in rematchdict.keys():
            for key_tmp1 in rematchdict[value].keys():
                value_tmp1 = rematchdict[value][key_tmp1]
                tmp_item3 = [value_tmp1,key_tmp1]
                final_dict[value][tags].append(tmp_item3)
    for key in final_nonmatch.keys():
        tmp_item4 = [final_nonmatch[key],key]
        final_dict['其他'][tags].append(tmp_item4)

    return final_dict

industrylist = []
final_dict = {}
init_dict = {}
for key in yingcai_industry.keys():
    init_dict[key] = yingcai_industry[key].encode('utf-8')
industrylist = InitIndustry(init_dict)

final_dict = {}
for value in industrylist:
    final_dict[value]={}

industry_list = [
                ['yingcai', yingcai_industry],
                ['liepin', liepin_industry],
                ['jingying', jingying_industry],
                ['zhilian', zhilian_industry]
                ]
for process_industry in industry_list:
    print process_industry[0]
    final_dict = Merge(process_industry[0],industrylist,final_dict,process_industry[1])
print final_dict

filepath = '/home/winky/predator/sources/source.py'
sources=open(filepath,'w')
sources.write('#encoding: utf-8\n')
sources.write('industry_dict = {\n')
for key1 in final_dict.keys():
    sources.write('\t\'{0}\':{1}\n'.format(key1,'{'))
    sources.write('\t\t\'yingcai\': [')
    for index in range(len(final_dict[key1]['yingcai'])):
        if index != (len(final_dict[key1]['yingcai'])-1):
            sources.write('[\'{0}\',\'{1}\'],'.format(final_dict[key1]['yingcai'][index][0], 
                                                    final_dict[key1]['yingcai'][index][1]))
        else:
            sources.write('[\'{0}\',\'{1}\']'.format(final_dict[key1]['yingcai'][index][0], 
                                                    final_dict[key1]['yingcai'][index][1]))
    sources.write('],\n')

    sources.write('\t\t\'liepin\': [')
    for index in range(len(final_dict[key1]['liepin'])):
        if index != (len(final_dict[key1]['liepin'])-1):
            sources.write('[\'{0}\',\'{1}\'],'.format(final_dict[key1]['liepin'][index][0], 
                                                    final_dict[key1]['liepin'][index][1]))
        else:
            sources.write('[\'{0}\',\'{1}\']'.format(final_dict[key1]['liepin'][index][0], 
                                                    final_dict[key1]['liepin'][index][1]))
    sources.write('],\n')

    sources.write('\t\t\'jingying\': [')
    for index in range(len(final_dict[key1]['jingying'])):
        if index != (len(final_dict[key1]['jingying'])-1):
            sources.write('[\'{0}\',\'{1}\'],'.format(final_dict[key1]['jingying'][index][0], 
                                                    final_dict[key1]['jingying'][index][1]))
        else:
            sources.write('[\'{0}\',\'{1}\']'.format(final_dict[key1]['jingying'][index][0], 
                                                    final_dict[key1]['jingying'][index][1]))
    sources.write('],\n')

    sources.write('\t\t\'zhilian\': [')
    for index in range(len(final_dict[key1]['zhilian'])):
        if index != (len(final_dict[key1]['zhilian'])-1):
            sources.write('[\'{0}\',\'{1}\'],'.format(final_dict[key1]['zhilian'][index][0], 
                                                    final_dict[key1]['zhilian'][index][1]))
        else:
            sources.write('[\'{0}\',\'{1}\']'.format(final_dict[key1]['zhilian'][index][0], 
                                                    final_dict[key1]['zhilian'][index][1]))
    sources.write(']\n')
    sources.write('\t\t},\n')
sources.write('\t}\n')

sources.close()
