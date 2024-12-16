from collections import deque

# 找到從起點到終點的最短路徑，使用廣度優先搜索 (BFS)
def find_shortest_path(graph, start, end):
    visited = set()  # 記錄已訪問的node
    queue = deque([[start, [start]]])  # 初始化queue，包含起點和路徑

    while queue:
        node, path = queue.popleft()  # 從queue左端彈出一個node和其路徑
        if node not in visited:
            visited.add(node)  # 標記當前node為已訪問
            neighbors = graph[node]  # 獲取當前node的所有鄰居
            for neighbor, weight in neighbors:
                if neighbor == end:
                    return path + [neighbor]  # 找到終點，返回完整路徑
                else:
                    queue.append([neighbor, path + [neighbor]])  # 將鄰居加入queue，繼續搜索

# 使用深度優先搜索 (DFS) 找到從node到終點的最大熟悉度路徑
def dfs(node, end, graph, path, familiarity):
    if node == end:
        return familiarity, path[:]  # 到達終點，返回當前熟悉度和路徑

    max_familiarity = 0  # 初始化最大熟悉度
    max_familiar_path = []  # 初始化最大熟悉度的路徑

    for neighbor, weight in graph[node]:
        if neighbor not in path:  # 避免環路
            # 遞歸搜索鄰居node
            new_familiarity, new_path = dfs(neighbor, end, graph, path + [neighbor], familiarity + weight)
            if new_familiarity > max_familiarity:
                max_familiarity = new_familiarity  # 更新最大熟悉度
                max_familiar_path = new_path  # 更新最大熟悉度的路徑

    return max_familiarity, max_familiar_path  # 返回最大熟悉度和相應路徑

# 尋找從起點到終點的最大熟悉度路徑
def find_max_familiar_path(graph, start, end):
    max_familiarity, max_familiar_path = dfs(start, end, graph, [start], 0)
    return max_familiarity, max_familiar_path

# 主函數，處理關係圖並輸出結果
def func(relationships):
    start_user = 'A'  # 設定起始用戶
    end_user = 'B'    # 設定終點用戶
    shortest_path = find_shortest_path(relationships, start_user, end_user)  # 找到最短路徑
    max_familiarity, max_familiar_path = find_max_familiar_path(relationships, start_user, end_user)  # 找到最大熟悉度路徑

    print(len(shortest_path)-1)            # 輸出最短路徑的邊數
    print(' '.join(shortest_path))         # 輸出最短路徑的node序列
    print(max_familiarity)                 # 輸出最大熟悉度
    print(' '.join(max_familiar_path))     # 輸出最大熟悉度路徑的node序列

# 檢查目標node是否存在於項目列表中
def inDic(target, itemList):
    for item in itemList:
        if item[0] == target:
            return True
    return False

# 更新關係圖中兩個node之間的熟悉度
def update(relationships, start, target, familiarity):
    for item in relationships[start]:
        if item[0] == target:
            if item[1] > familiarity:
                item[1] = familiarity  # 更新為較低的熟悉度
                return

# 讀取輸入並構建關係圖
def setInput():
    N = int(input())  # 讀取關係數量
    relationships = {}  # 初始化關係圖

    while True:
        content = input()
        if content == '-1':  # 結束輸入的標誌
            return relationships
        list = [str(i) for i in content.split()]
        start = list[0]            # 起點node
        end = list[1]              # 終點node
        familiarity = int(list[2])  # 熟悉度

        if start not in relationships:
            relationships[start] = []  # 初始化起點的鄰居列表

        if end not in relationships:
            relationships[end] = []    # 初始化終點的鄰居列表

        # 如果關係已存在，則更新熟悉度
        if inDic(end, relationships[start]) and inDic(start, relationships[end]):
            update(relationships, start, end, familiarity)
            update(relationships, end, start, familiarity)
        else:
            # 添加新的關係
            relationships[start].append([end, familiarity])
            relationships[end].append([start, familiarity])

# 程式進入點
if __name__ == "__main__":
    relationships = setInput()  # 構建關係圖
    print(relationships)
    func(relationships)          # 執行主功能
