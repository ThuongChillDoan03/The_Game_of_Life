import numpy as np

def numRows():
    n_rows = int(input("Nhập số hàng của lưới(>=2): "))
    return n_rows

def numCols():
    n_Cols = int(input("Nhập số cột của lưới(>=2): "))
    return n_Cols

def LifeGrid(nrows, ncols):
    Life_Grid = np.zeros((nrows, ncols))
    return Life_Grid.astype(np.int64)

def Alive():
    n_alive = int(input("Nhập số thằng còn sống: "))
    return n_alive

def coordList(n_alive):
    Arr_alive_coordList = np.zeros((n_alive,2))
    for idx in range(n_alive):
        for place in range(2):
            Arr_alive_coordList[idx][place] = int(input("Phần tử thứ [%2d][%2d]:" % (idx+1, place+1)))
    return Arr_alive_coordList.astype(np.int64)

def configure(Arr_alive_coordList,Life_Grid):
    for quant in range(len(Arr_alive_coordList)):
        Life_Grid[Arr_alive_coordList[quant][0]][Arr_alive_coordList[quant][1]] = 1
    return Life_Grid

# Check còn bao nhiêu hàng xóm còn sống\\
def numLiveNeighbors(nrows,ncols,arr_Life_Grid_return):
    Life_Grid_Negh = np.zeros((nrows,ncols)).astype(np.int64)
    if nrows == 1:
        for cols in range(len(arr_Life_Grid_return[0])):
            Pres_Location = arr_Life_Grid_return[0]
            place_pres = np.where(Pres_Location == 1)[0]
            count = 0
            if (cols - 1) in place_pres:
                count += 1
            if (cols + 1) in place_pres:
                count += 1
            Life_Grid_Negh[0][cols] = count
            
    if nrows >= 2:
        for rows in range(len(arr_Life_Grid_return)):
            for cols in range(len(arr_Life_Grid_return[0])):
                count = 0
                if rows == 0:
                    Pres_Location = arr_Life_Grid_return[0]
                    After_Location = arr_Life_Grid_return[1]
                    place_pres = np.where(Pres_Location == 1)[0]
                    place_after = np.where(After_Location == 1)[0]
                    if (cols - 1) in place_pres:
                        count += 1
                    if (cols + 1) in place_pres:
                        count += 1
                    if (cols + 1) in place_after:
                        count += 1
                    if cols in place_after:
                        count += 1
                    if (cols - 1) in place_after:
                        count += 1
                    Life_Grid_Negh[rows][cols] = count
                    # print(Life_Grid_Negh)
                if (rows == len(arr_Life_Grid_return) - 1):
                    Pres_Location_1 = arr_Life_Grid_return[len(arr_Life_Grid_return) - 1]
                    Before_Location_1 = arr_Life_Grid_return[len(arr_Life_Grid_return) - 2]
                    place_pres_1 = np.where(Pres_Location_1 == 1)[0]
                    place_before_1 = np.where(Before_Location_1 == 1)[0]
                    if (cols - 1) in place_pres_1:
                        count += 1
                    if (cols + 1) in place_pres_1:
                        count += 1
                    if (cols + 1) in place_before_1:
                        count += 1
                    if cols in place_before_1:
                        count += 1
                    if (cols - 1) in place_before_1:
                        count += 1
                    Life_Grid_Negh[rows][cols] = count
                if (0 < rows) and (rows < len(arr_Life_Grid_return) - 1):
                    Pres_Location_2 = arr_Life_Grid_return[rows]
                    Before_Location_2 = arr_Life_Grid_return[rows - 1]
                    After_Location_2 = arr_Life_Grid_return[rows + 1]
                    place_pres_2 = np.where(Pres_Location_2 == 1)[0]
                    place_before_2 = np.where(Before_Location_2 == 1)[0]
                    place_after_2 = np.where(After_Location_2 == 1)[0]
                    if (cols - 1) in place_pres_2:
                        count += 1
                    if (cols + 1) in place_pres_2:
                        count += 1
                    if (cols + 1) in place_before_2:
                        count += 1
                    if cols in place_before_2:
                        count += 1
                    if (cols - 1) in place_before_2:
                        count += 1
                    if (cols + 1) in place_after_2:
                        count += 1
                    if cols in place_after_2:
                        count += 1
                    if (cols - 1) in place_after_2:
                        count += 1
                    Life_Grid_Negh[rows][cols] = count

    return Life_Grid_Negh

def next_generation(nrows,ncols,Life_Grid_Negh,arr_Life_Grid_return):
    Grid_next_generation = np.zeros((nrows,ncols)).astype(np.int64)
    for row in range(len(Life_Grid_Negh)):
        for col in range(len(Life_Grid_Negh[0])):
            if (arr_Life_Grid_return[row][col]==0) and (Life_Grid_Negh[row][col] == 3): #hồi sinh
                Grid_next_generation[row][col] = 1
            if (arr_Life_Grid_return[row][col]==1) and (1<Life_Grid_Negh[row][col]<4): #duy trì
                Grid_next_generation[row][col] = 1
            if (arr_Life_Grid_return[row][col]==1) and ((Life_Grid_Negh[row][col]<=1) or (Life_Grid_Negh[row][col]>=4)):
                Grid_next_generation[row][col] = 0

    return Grid_next_generation


###______________________________________Main_Print___________________________###
nrows = numRows()
ncols = numCols()
Life_Grid = LifeGrid(nrows, ncols)
print("Lưới khởi tạo:")
print(Life_Grid)
n_alive = Alive()
Arr_alive_coordList = coordList(n_alive)
print("Tọa độ các điểm có người sống:")
print(Arr_alive_coordList)
arr_Life_Grid_return = configure(Arr_alive_coordList,Life_Grid)
print("Lưới sinh vật thế hệ hiện tại:")
print(arr_Life_Grid_return)
Life_Grid_Negh = numLiveNeighbors(nrows,ncols,arr_Life_Grid_return)
print("Ma trận số lượng hàng xóm:")
print(Life_Grid_Negh)
Grid_next_generation = next_generation(nrows,ncols,Life_Grid_Negh,arr_Life_Grid_return)
print("Lưới sinh vật của thế hệ tiếp theo:")
print(Grid_next_generation)

###___________________________________________________________________________###

