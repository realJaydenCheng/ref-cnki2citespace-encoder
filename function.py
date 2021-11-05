from io import DEFAULT_BUFFER_SIZE
import re
DEFAULT = ""


def main(file_name):
    es_dict = read_info(file_name)  # 输入文件，解析文件，转换为字典{文章标题：引用文章，引用书籍}
    for key in es_dict:
        es_dict[key] = clear_info(es_dict[key])  # 输入文章字典，返回新文章字典，{文章标题：引用}
    result_name = "download_1-307.txt"
    print(write_file(result_name, es_dict))  # 将引用的部分写入目标文件


def read_info(file_name):
    infos = open(file_name, 'r', encoding="utf-8")
    infos = infos.read()
    es_dict = {}
    infos = re.findall(r"<p>.*?</p>", infos, re.S)
    for es in infos:
        title = re.findall(r"<title>.*?</title>", es, re.S)
        if title == []:
            continue
        title = title[0].replace("<title>", "").replace("</title>", "")
        ref_e = re.findall(r"<ref>.*?</ref>", es, re.S)[0]
        ref_e = ref_e.replace("<ref>", "").replace("</ref>", "").split('\n')
        ref_b = re.findall(r"<book>.*?</book>", es, re.S)[0]
        ref_b = ref_b.replace("<book>", "").replace("</book>", "").split('\n')
        es_dict[title] = (ref_e, ref_b)
    return es_dict


def clear_info(essay):
    ref = tran_ref(essay[0])  # 获取参考文献列表，返回相应格式的字符串列表
    book = tran_book(essay[-1])  # 获取参考图书列表，同上
    ref.extend(book)
    return ref


'''
def default_assignment(arr ,index):
    try :
        return arr[index]
    except : 
        return DEFAULT
'''


def tran_ref(ref_tp):
    # eg: [2]艺术感觉与美育. 滕守尧译,[美]拉尔夫.史密斯著. 四川人民出版社 . 1998
    result = []
    for ref in ref_tp:
        ref = ref.replace(",", '.').strip()
        if ref == "":
            continue
        ref = re.sub(r"\[\d+?\]", "", ref)
        # 艺术感觉与美育. 滕守尧译.[美]拉尔夫.史密斯著. 四川人民出版社 . 1998
        ref = ref.split('.')
        try:
            ref = [ref[1], ref[-1], ref[-2]]
        except:
            continue
        #ref = [default_assignment(ref ,1),default_assignment(ref ,-1),default_assignment(ref ,-2)]
        if '' in ref:
            continue
        # 滕守尧译,1998,四川人民出版社
        result.append(','.join(ref))
    return result


def tran_book(book_tp):
    # eg: [1]中心的丧失[M]. 译林出版社 , 汉斯·赛德尔迈尔, 2021
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


def write_file(original_file, essays):
    file = open(original_file, 'r', encoding="utf-8")
    file = file.read()
    file = re.findall(r"PT.*?ER", file, re.S)
    result = ""
    error = set()
    for essay_in_origin in file:
        title = re.findall(r"TI.*?SO", essay_in_origin, re.S)
        title = title[0].replace("TI", "").replace(
            "SO", "").replace(" ", '').replace("\n", '')
        author = re.findall(r"AU.*?AF", essay_in_origin, re.S)
        author = author[0].replace(',', '').replace(
            '\n', '').replace("AU", '').replace("AF", "").strip()
        for t in essays:
            isFound = 0
            if t == title:
                ref_list = []
                #ref = '\n'.join(essays[t])
                for ref in essays[t]:  # 比对作者 剔除自引数据
                    if author in ref[0]:
                        continue
                    else:
                        ref_list.append(ref)
                ref = '\n'.join(ref_list)
                #essay_in_file = re.sub(r"CR .*?NR","CR "+ref+"\nNR",essay_in_file ,re.S)
                sub = re.findall(r"CR .*?NR", essay_in_origin, re.S)
                essay_in_origin = essay_in_origin.replace(
                    sub[0], "CR "+ref+"\nNR")
                #del essays[t]
                result = result + '\n' + essay_in_origin + '\n'
                isFound = 1
                if isFound:
                    break
        else:
            error.add(title)
    file = open("reslt.txt", 'w', encoding="utf-8")
    file.write(result)
    file.close()
    return error, len(error)


main("./ref_info.html")


# read_info("./ref_info.html")
#tran_book(("[1]中心的丧失[M]. 译林出版社 , 汉斯·赛德尔迈尔, 2021","[1]中心的丧失[M]. 译林出版社 , 汉斯·赛德尔迈尔, 2021"))
