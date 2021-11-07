import re
DEFAULT = ""
tooBig = set()
noData = set()
input_file = "./original_data.html"

def main(file_name):
    es_dict = read_info(file_name)  # 输入文件，解析文件，转换为字典{文章标题：[引用,...]}
    for title in es_dict:
        es_dict[title] = clear_info(es_dict[title])  # 输入文章字典，返回新文章字典，{文章标题：引用}
    result_name = "./download_1-414_converted.txt"
    print(write_file(result_name, es_dict))  # 将引用的部分写入目标文件
    print("需要翻页的文章有：\n" + '\n'.join(list(tooBig)) + "\n一共有" + str(len(tooBig)) + "条。\n" + "\n没有引用的文章有：\n" + '\n'.join(list(noData)) + "\n一共有" + str(len(noData)) + "条。")
    

def read_info(file_name):
    infos = open(file_name, 'r', encoding="utf-8")
    infos = infos.read()
    es_dict = {}
    infos = re.findall(r"<p>.*?</p>", infos, re.S)
    for essay in infos:
        title = re.findall(r"<title>.*?</title>", essay, re.S)
        if title == []:
            continue
        title = title[0].replace("<title>", "").replace("</title>", "").strip()
        isBig = re.findall(r"共\d*?页", essay)
        if isBig:
            tooBig.add(title)
            continue
        if "号京公网安备" in essay:
            noData.add(title)
            continue
        refs = re.findall(r"<ref>.*?</ref>", essay, re.S)[0]
        refs = refs.replace("<ref>", "").replace("</ref>", "").split('\n')
        es_dict[title] = refs
        '''
        ref_e = re.findall(r"<ref>.*?</ref>", es, re.S)[0]
        ref_e = ref_e.replace("<ref>", "").replace("</ref>", "").split('\n')
        ref_b = re.findall(r"<book>.*?</book>", es, re.S)[0]
        ref_b = ref_b.replace("<book>", "").replace("</book>", "").split('\n')
        es_dict[title] = (ref_e, ref_b)
        '''
    return es_dict


def clear_info(refs):
    '''
    ref = tran_ref(refs[0])  # 获取参考文献列表，返回相应格式的字符串列表
    book = tran_book(refs[-1])  # 获取参考图书列表，同上
    '''
    cleaned_refs = []
    for ref in refs:
        if "[M]" in ref:
            ref = tran_book(ref)
            if ref == None:
                continue
            cleaned_refs.append(','.join(ref))
        elif ref.count(".") >= 3:
            ref = tran_ref(ref)
            if ref == None:
                continue
            cleaned_refs.append(','.join(ref))
        else:
            continue
    # ref.extend(cleaned_refs)
    return cleaned_refs


'''
def default_assignment(arr ,index):
    try :
        return arr[index]
    except : 
        return DEFAULT
'''


def tran_ref(ref):  # 返回调整后的字符串。
    # eg: [2]艺术感觉与美育. 滕守尧译,[美]拉尔夫.史密斯著. 四川人民出版社 . 1998
    '''
    result = []
    for ref in ref_tp:
    '''
    ref = ref.replace(",", '.').strip()
    ref = re.sub(r"\[\d+?\]", "", ref)
    # 艺术感觉与美育. 滕守尧译.[美]拉尔夫.史密斯著. 四川人民出版社 . 1998
    ref = ref.split('.')
    ref = [ref[1], ref[-1], ref[-2]]
    #ref = [default_assignment(ref ,1),default_assignment(ref ,-1),default_assignment(ref ,-2)]
    if '' in ref:
        ref = None
        # 滕守尧译,1998,四川人民出版社
        # result.append(','.join(ref))
    return ref



def tran_book(book):
    # eg: [1]中心的丧失[M]. 译林出版社 , 汉斯·赛德尔迈尔, 2021
    '''
    result = []
    for book in book_tp:
        book = book.replace(",", '.').strip()
        if book == "":
            continue
        book = re.sub(r"\[\d+?\]", "", book)
        # 中心的丧失[M]. 译林出版社 . 汉斯·赛德尔迈尔. 2021
        book = book.split('.')
        try:
            book = [book[2], book[-1], book[1]]
        except:
            continue
        #book = [default_assignment(book ,2),default_assignment(book ,-1), default_assignment(book ,1)]
        # 汉斯·赛德尔迈尔,2021,译林出版社
        if '' in book:
            continue
        result.append(','.join(book))
    return result 
    '''
    book = book.replace(",", '.').strip()
    book = re.sub(r"\[\d+?\]", "", book)
    book = book.split('.')
    book = [book[2], book[-1], book[1]]
    if '' in book:
        book = None
        # 滕守尧译,1998,四川人民出版社
        # result.append(','.join(ref))
    return book


def write_file(citespace_file, essays_of_cnki):
    count = 0
    file = open(citespace_file, 'r', encoding="utf-8")
    file = file.read()
    file = re.findall(r"PT.*?ER", file, re.S)
    error = set()
    result = ""
    for essay_in_origin in file:
        citespace_essay_title = re.findall(r"TI.*?SO", essay_in_origin, re.S)
        citespace_essay_title = citespace_essay_title[0].replace("TI", "").replace(
            "SO", "").replace(" ", '').replace("\n", '')
        author = re.findall(r"AU.*?AF", essay_in_origin, re.S)
        author = author[0].replace(',', '').replace(
            '\n', '').replace("AU", '').replace("AF", "").strip()
        for cnki_essay_title in essays_of_cnki:
            isFound = 0
            if ((cnki_essay_title.replace(" ", '').replace("\n", '') in citespace_essay_title.replace(" ", '').replace("\n", '')) or (citespace_essay_title.replace(" ", '').replace("\n", '') in cnki_essay_title.replace("\n", '').replace(" ", ''))):
                ref_list = []
                #ref = '\n'.join(essays[t])
                for ref in essays_of_cnki[cnki_essay_title]:  # 比对作者 剔除自引数据
                    if author in ref[0]:
                        continue
                    else:
                        ref_list.append(ref)
                count += len(ref_list)
                ref = '\n'.join(ref_list)
                #essay_in_file = re.sub(r"CR .*?NR","CR "+ref+"\nNR",essay_in_file ,re.S)
                sub = re.findall(r"CR .*?NR", essay_in_origin, re.S)
                essay_in_origin = essay_in_origin.replace(
                    sub[0], "CR "+ref+"\nNR")
                #del essays[t]
                result = result + '\n' + essay_in_origin + '\n'
                break
        else:
           error.add(citespace_essay_title)
    file = open("reslt.txt", 'w', encoding="utf-8")
    file.write(result)
    file.close()
    error = error - (tooBig | noData)
    print(f"一共成功写入{count}篇")
    return "标题有误：\n" + '\n'.join(list(error)) + "\n一共有" + str(len(error)) + "条。\n" 


main(input_file)


# read_info("./ref_info.html")
#tran_book(("[1]中心的丧失[M]. 译林出版社 , 汉斯·赛德尔迈尔, 2021","[1]中心的丧失[M]. 译林出版社 , 汉斯·赛德尔迈尔, 2021"))
