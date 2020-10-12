import random


def shiduh(men_list,women_list,pref_men,pref_women):
    cur_men=men_list.copy()
    cur_pref_men=pref_men.copy()
    zivug=[]
    for i in men_list:
        zivug.append([i])
    while len(cur_men)!=0:
        m=random.choice(cur_men)
        index_m=men_list.index(m)
        cur_pref_m=cur_pref_men[index_m]
        m_choice=cur_pref_m[0]
        index_choice=women_list.index(m_choice)
        cnt=0
        for i in zivug:
            if m_choice in i:
                cnt+=1
        if cnt==0:
            zivug[index_m].append(m_choice)
            cur_men.remove(m)
            cur_pref_men[index_m].remove(m_choice)
        else:
            for i in range(len(zivug)):
                if m_choice in zivug[i]:
                    cur_zivug_index=i
            m2=zivug[cur_zivug_index][0]
            if pref_women[index_choice].index(m)<pref_women[index_choice].index(m2):
                zivug[cur_zivug_index].remove(m_choice)
                zivug[index_m].append(m_choice)
                cur_men.remove(m)
                cur_men.append(m2)
                cur_pref_men[index_m].remove(m_choice)
            else:
                cur_pref_men[index_m].remove(m_choice)
    #it's possible to return zivug, but:
    sol=''
    for i in range(len(men_list)):
        sol+=zivug[i][0]+' is matched with '+zivug[i][1]+'\n'
    print('\n*****************\n\n'+sol+'\n*****************')


shiduh(['a','b','c','d'],['w','x','y','z'],[['x','w','y','z'],['x','w','y','z'],
['y','w','z','x'],['x','z','y','w']],[['b','a','c','d'],['c','a','d','b'],
['c','b','d','a'],['a','c','b','d']])
shiduh(['Abby','Eli'],['Dina','Owen'],[['Owen','Dina'],['Dina','Owen']],[['Eli','Abby'],['Abby','Eli']])
