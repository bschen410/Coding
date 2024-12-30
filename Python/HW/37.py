import math


def main():
    dictionary = data_input()
    search_content = input().split()
    getEachDepartmentContent(dictionary)
    getEachClass(dictionary["classes_student"])
    getHistoryHigh(dictionary, search_content)


def addInDictionary(dictionary, key, item):
    # 如果字典沒有這個key
    if key not in dictionary:
        # 在字典中新增這個key，並將 item 放入對應的值 (以列表形式儲存)
        dictionary[key] = [item]
    # 如果item不在該列表中
    if item not in dictionary[key]:
        # 將item新增到列表中
        dictionary[key].append(item)


def classContentInput(
    class_year_dictionary,
    department_dictionary,
    department_year_dictionary,
    students_grade_dictionary,
    classes_directory,
):
    # 輸入課程資訊，用空格分割字串，存到變數class_infor
    class_infor = input().split(" ")
    # 取得課程編碼與學年度三碼(沒有上下學期)
    class_name, class_year = class_infor[0], class_infor[1][:3]
    # 將key:學年度與vlaue:課程編碼加到class_year_dictionary
    addInDictionary(class_year_dictionary, class_year, class_name)

    for i in range(int(class_infor[2])):  # class_infor[2]是學生數量
        content = input()  # 輸入學生成績資料
        temp_content = content.split(
            " "
        )  # 將輸入的資料以空格分隔，存入 temp_content 列表
        # 取得學生入學年度,科系編碼,完整學號
        student_year, student_department, student_number = (
            temp_content[0][:3],
            temp_content[0][3:6],
            temp_content[0],
        )
        student_grade = temp_content[1]  # 取得學生學期成績
        # 將key:學生科系編碼與value:學號加到department_dictionary
        addInDictionary(department_dictionary, student_department, student_number)
        # 將key:學生科系編碼與value:學生入學年度加到department_year_dictionary
        addInDictionary(department_year_dictionary, student_department, student_year)

        # 如果課程編碼中的學科編碼(前三碼)不是101跟201 或 學生學期成績是w
        # 非國文一跟英文一的課程只會有學期成績
        if (
            class_name[:3] != "101" and class_name[:3] != "201"
        ) or student_grade == "w":
            # 將key:學生學號與vlaue:[課程編碼(四碼),學期編碼的學年度(三碼),學生學期成績]加到students_grade_dictionary
            addInDictionary(
                students_grade_dictionary,
                student_number,
                [class_name, class_year, student_grade],
            )
            # 將key:課程編碼 學期編碼的學年度與vlaue:[學號,學期成績]加到classes_directory
            addInDictionary(
                classes_directory,
                class_name + " " + class_year,
                [student_number, student_grade],
            )
        else:  # 國文一及英文一的課程會多加一個會考成績
            addInDictionary(
                students_grade_dictionary,
                student_number,
                [class_name, class_year, student_grade, temp_content[2]],
            )
            addInDictionary(
                classes_directory,
                class_name + " " + class_year,
                [student_number, student_grade, temp_content[2]],
            )


def data_input():
    a = int(input())  # 輸入課程數
    department_dictionary = {}  # 存各科系學生名單
    department_year_dictionary = {}  # 存放各科系所有年級
    students_grade_dictionary = {}  # 存每位學生的各項成績
    class_year_dictionary = {}  # 存放每年課程
    classes_directory = {}  # 存每堂課學生資料
    for i in range(a):
        classContentInput(
            class_year_dictionary,
            department_dictionary,
            department_year_dictionary,
            students_grade_dictionary,
            classes_directory,
        )
    dictionary = {
        "departments_students": department_dictionary,
        "departments_years": department_year_dictionary,
        "students_grade": students_grade_dictionary,
        "years_classes": class_year_dictionary,
        "classes_student": classes_directory,
    }
    return dictionary


def getEachDepartmentContent(dictionary):
    # 由小到大排序科系編碼
    department_year_list = sorted(dictionary["departments_years"])
    for i in department_year_list:
        # 排序每個科系學生入學年度
        dictionary["departments_years"][i] = sorted(dictionary["departments_years"][i])
    for i in department_year_list:
        # 在dictionary新增一個key是"department_name"，對應的value是i
        # 代表當前處理的科系編碼
        dictionary["department_name"] = i

        # 在dictionary新增一個key是"department_years"， 對應的value是dictionary["departments_years"][i]的value
        # 代表該科系的所有學生入學年度列表
        dictionary["department_years"] = dictionary["departments_years"][i]
        # 處理科系與學生入學年度
        getEachDepartmentYear(dictionary)


def getEachDepartmentYear(dictionary):
    # 遍歷該科系的所有學生入學年度
    for i in dictionary["department_years"]:

        # 新增一個key是"department_year"，對應的value是i
        # 代表當前處理的學生入學年度
        dictionary["department_year"] = i
        # 處理課程年度
        getEachYear(dictionary)


def getEachYear(dictionary):
    # 排序課程學年度
    class_year_list = sorted(dictionary["years_classes"])
    for i in class_year_list:  # 遍歷課程學年度
        # 新增一個key是"class_year"
        # 代表當前處理的課程學年度
        dictionary["class_year"] = i
        # 新增一個key是"classes"，對應的value是dictionary["years_classes"][i]的value
        # 代表該課程學年度的課程編碼
        dictionary["classes"] = dictionary["years_classes"][i]
        getEachContent(dictionary)


def getEachContent(dictionary):
    # 從dictionary["departments_students"][dictionary["department_name"]](也就是該科系每個學生的學號)篩選出符合條件的學生
    # 學生學號的前三碼跟dictionary["department_year"]的value(當前處理的學生入學年度)是相同的
    # 符合該學生入學年度
    all_student = list(
        filter(
            lambda x: True if (x[:3] == dictionary["department_year"]) else False,
            dictionary["departments_students"][dictionary["department_name"]],
        )
    )

    all_student_computed_infor = []  # 存計算後的學生徹選百分比、學年成績
    for i in all_student:  # 遍歷所有符合該學生入學年度的學號
        temp = [i]  # 先將當前的學生學號暫存在temp列表中
        # getEachGrade()傳入的變數(dictionary["students_grade"][當前學生學號]的value, 當前處理的課程學年度, 該課程學年度的課程編碼, 符合條件的學生人數)
        # 回傳的結果-have_grade:True or False, content=[學生撤選百分比,學年成績]
        have_grade, content = getEachGrade(
            dictionary["students_grade"][i],
            dictionary["class_year"],
            dictionary["classes"],
            len(all_student),
        )
        # 如果have_grade是True
        if have_grade:
            temp.append(content)
            # all_student_computed_infor的結構:[['11153001', ['0%', 61]], ['11153002', ['0%', 70]], ['11153003', ['0%', 47]], ['11153005', ['0%', 73]]]
            all_student_computed_infor.append(temp)
    # 將學生的學年成績由高到低排序
    # sorted_grade: [['11153005', ['0%', 73]], ['11153002', ['0%', 70]], ['11153001', ['0%', 61]], ['11153003', ['0%', 47]]]
    sorted_grade = sorted(
        all_student_computed_infor, key=lambda x: x[1][1], reverse=True
    )
    if len(sorted_grade) != 0:
        # 印出 科系,當前處理的學生入學年度,當前處理的課程學年度
        print(
            dictionary["department_name"],
            dictionary["department_year"],
            dictionary["class_year"],
        )
        for i in range(3 if (len(sorted_grade) >= 3) else len(sorted_grade)):
            # 利用for迴圈只印出前三名的(學號,學年成績,名次百分比,學生撤選百分比)
            print(
                sorted_grade[i][0],
                sorted_grade[i][1][1],
                getPercentage(i + 1, len(all_student)),
                sorted_grade[i][1][0],
            )


def getEachGrade(scores, class_year, classes, student_nums):
    count1 = 0  # 用來計算總成績
    count2 = 0  # 紀錄課程學分數
    back = 0  # 紀錄該學年退選科目數量
    class_count = 0  # 紀錄該學年選修科目數量
    recorded_num = 0  # 紀錄有無成績資訊
    for i in classes:  # 遍歷該課程學年度的課程編碼
        # 從scores篩選出符合該課程學年度的課程編碼跟課程學年度
        # scores會是dictionary["students_grade"][當前學生學號]的value
        # 假如 scores = [['1013', '112', '59', '63'], ['1214', '113', '63']]
        # 當前課程學年度的課程編碼:1013、當前課程學年度:112
        # 就會篩選出 temp = [['1013', '112', '59', '63']]
        temp = list(
            filter(
                lambda x: True if (x[0] == i and x[1] == class_year) else False, scores
            )
        )
        if len(temp) == 0:
            continue  # 跳過本次迴圈
        if temp[0][2] == "w":
            back += 1
            continue  # 跳過本次迴圈
        recorded_num += 1
        # 代表不是國文一跟英文一，成績直接乘上學分數
        if len(temp[0]) == 3:
            count1 += int(temp[0][2]) * int(i[-1])
        elif len(temp[0]) == 4:
            # 計算課程學期成績和會考成績，分別占比70%、30%，總分為無條件進位至整數
            count1 += compute101and201(temp[0][2], temp[0][3]) * int(i[-1])

        count2 += int(i[-1])
        class_count += 1
    if recorded_num == 0:
        return False, 0
    # 計算學年成績
    result = math.floor(count1 / count2) if (count2 != 0) else 0
    return True, [
        str(math.floor(back / (class_count + back) * 100) if (class_count != 0) else 0)
        + "%",
        result,
    ]


def compute101and201(grades1, grades2):
    temp = int(grades1) * 70 + int(grades2) * 30
    result = temp // 100
    return result if (temp % 100 == 0) else result + 1


def getPercentage(rank, total_num):
    school_rank = rank
    percentage = 1
    # 算出percentage要多少才會讓school_rank*100 <= total_num*percentage+99
    for i in range(100):
        if school_rank * 100 <= total_num * percentage + 99:
            return str(percentage) + "%"

        percentage += 1
    return str(percentage) + "%"


def getEachClass(class_dictionary):
    # 由小到大排序dictionary["classes_student"]的value(也就是'課程編碼 課程學年度')
    class_dictionary_list = sorted(class_dictionary, key=lambda x: x.split(" ")[1])
    class_dictionary_list = sorted(class_dictionary_list, key=lambda x: x.split(" ")[0])
    for i in class_dictionary_list:  # 遍歷class_dictionary_list
        print(i)
        # getGrade()傳入的變數(包含學生學號、成績的二維list, 如果課程編碼前三碼是101或202，就回傳2，否則回傳1)
        # 會回傳w_count:退選人數、student_score:[[學期成績,學號],...]、pure_score:[學期成績1,...]
        w_count, student_score, pure_score = getGrade(
            class_dictionary[i], 2 if (i[:3] == "101" or i[:3] == "201") else 1
        )
        # 將student_score的學期成績由高到低排序
        student_score = sorted(student_score, key=lambda x: x[0], reverse=True)
        # 印出(最高學期成績,平均學期成績,最低學期成績,課程撤選百分比)
        print(
            max(pure_score),
            getMean(pure_score),
            min(pure_score),
            str(w_count * 100 // (w_count + len(pure_score))) + "%",
        )
        # 呼叫印出前三名的函式
        printFirst3(student_score, w_count)


def getGrade(list, num):
    w_count = 0  # 計算有退選的數量
    result = []
    pure_grade_result = []
    list = sorted(list, key=lambda x: x[0])  # 將list裡的學號由小到大排序
    for i in list:
        # 如果沒有退選
        if i[1] != "w":
            # [如果num是1(代表非國文一跟英文一)，直接回傳學期成績，否則呼叫compute101and201()計算學期與會考成績,
            # 學號]
            # result的結構: [[61, '11153001'], [70, '11153002'], [47, '11153003'], [73, '11153005'], [75, '11253001'], [83, '11253002'], [71, '11253003'], [87, '11253004']]
            result.append(
                [int(i[1]) if (num == 1) else compute101and201(i[1], i[2]), i[0]]
            )
            # 放純成績的list
            # pure_grade_result的結構:[61, 70, 47, 73, 75, 83, 71, 87]
            pure_grade_result.append(
                int(i[1]) if (num == 1) else compute101and201(i[1], i[2])
            )
        else:  # 有退選
            w_count += 1
    return w_count, result, pure_grade_result


def getMean(lst):
    result = 0
    for i in lst:
        # 累加lst的學期成績
        result += i
    return result // len(lst)


def printFirst3(student_score, w_count):
    for i in range(3 if (len(student_score) >= 3) else len(student_score)):
        # 印出前三名的(學號,學期成績,名次百分比)
        print(
            student_score[i][1],
            student_score[i][0],
            getPercentage(i + 1, len(student_score) + w_count),
        )


def getHistoryHigh(dictionary, search_content):
    # 篩選出dictionary["classes_student"]的value -> 是一個字典 -> 它的key(課程編碼 課程學年度)
    # x.split(" ")[0]:課程編碼 等於 搜尋課程編碼
    classes = list(
        filter(
            lambda x: True if (x.split(" ")[0] == search_content[0]) else False,
            dictionary["classes_student"],
        )
    )
    students = []
    # print(classes)
    for i in classes:
        # 取得篩選出符合條件的key(課程編碼 課程學年度)的value
        # students的結構:[['11153001', '59', '63'], ['11153002', '68', '72'], ['11153003', '39', '64'], ['11153004', 'w'], ['11153005', '68', '82'], ['11253001', '67', '91'], ['11253002', '78', '92'], ['11253003', '72', '68'], ['11253004', '91', '76']]
        students += dictionary["classes_student"][i]
    # students的學號由小到大排序
    students = sorted(students, key=lambda x: x[0])

    # 篩選出沒有退選的學生
    # lambda x會代表students列表中的每個子列表
    students = list(filter(lambda x: True if (x[1] != "w") else False, students))
    # 若搜尋課程編碼的前三位是101或201(國文一或英文一，有學期成績跟會考成績)，則每個子列表的倒數第二個(課程學期成績)與倒數第一個(課程會考成績)元素放入compute101and201()執行
    # 根據compute101and201()回傳的結果由高到低排序
    # else:取每個子列表的倒數第一個元素(只有學期成績)由高到低排序
    students = sorted(
        students,
        key=lambda x: (
            compute101and201(x[-2], x[-1])
            if (search_content[0][:3] == "101" or search_content[0][:3] == "201")
            else int(x[-1])
        ),
        reverse=True,
    )
    count = {}
    for i in students:
        # i[0][3:6]會得到學號中的科系編碼
        # if(count.get(i[0][3:6],0)!=0)是用來檢查count中的key有沒有包含key:i[0][3:6](科系編碼)，若沒有包含會傳回0，
        # 當!=0時代表count{}有包含該key，則在count[i[0][3:6]]對應的value結尾累加1，用來計數每個科系的學生人數
        # count的結構:{'530': [1, 2, 3, 4, 5, 6, 7, 8]}，代表有8位學生
        addInDictionary(
            count,
            i[0][3:6],
            count[i[0][3:6]][-1] + 1 if (count.get(i[0][3:6], 0) != 0) else 1,
        )
    # list(count)會得到由字典count的key(科系編碼)組成的list
    # key=lambda x:count[x][-1]代表會由大到小排序這些key對應value的倒數第一個元素(每個科系的最大學生人數)
    # 最後排序完成得到的max_num是用count的key組成的，但排序方式是依據key對應value的最後一個元素
    max_num = sorted(list(count), key=lambda x: count[x][-1], reverse=True)
    if len(max_num) == 1:
        print(students[0][0], students[1][0], max_num[0])
    else:
        print(students[0][0], students[1][0], max_num[0], max_num[1])


if __name__ == "__main__":
    main()
