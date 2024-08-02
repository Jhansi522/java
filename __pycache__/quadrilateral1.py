def quadrilateral(arr):
    d12 = (arr_x[0]-arr_x[1])**2+(arr_y[0]-arr_y[1])**2
    d34 = (arr_x[2]-arr_x[3])**2+(arr_y[2]-arr_y[3])**2
    xm12 = (arr_x[0]+arr_x[1])//2
    ym12 = (arr_y[0]+arr_y[1])//2
    xm34 = (arr_x[2]+arr_x[3])//2
    ym34 = (arr_y[2]+arr_y[3])//2
    if d12 == d34 and xm12 == xm34 and ym12 and ym34:
        print("Yes")
    else:
        print("No")
t = int(input())
for _ in range(t):
    arr = input().split()
    arr_x = [int(arr[i]) for i in range(0,len(arr),2)]
    arr_y = [int(arr[i]) for i in range(1,len(arr),2)]
    quadrilateral(arr)
