import numpy
import pylab
import random
import time
class ConwayGame():
    def __init__(self, N = 100,T = 200):
        self.N = N
        self.T = T
        self.old_grid = numpy.zeros(N * N, dtype = 'int').reshape(N, N)
        self.new_grid = numpy.zeros(N * N, dtype = 'int').reshape(N, N)
        if a == 1:
            for i in range(0, self.N):
                for j in range(0, self.N):
                    if (random.randint(0,100) < 5):
                        self.old_grid[i][j] = 1
                    else:
                        self.old_grid[i][j] = 0
        elif a == 2:
             for i in range(int(self.N / 2) - 5, int(self.N / 2) + 5):
                 self.old_grid[int(self.N / 2)][i] = 1
        elif a == 3:
            self.old_grid[int(self.N / 2) - 1][int(self.N / 2) - 1] = 1
            self.old_grid[int(self.N / 2) - 1][int(self.N / 2)] = 1
            self.old_grid[int(self.N / 2) - 1][int(self.N / 2) + 1] = 1
            self.old_grid[int(self.N / 2)][int(self.N / 2) + 1] = 1
            self.old_grid[int(self.N / 2) + 1][int(self.N / 2)] = 1
        elif a == 4:
            for j in range(int(self.N / 2) - 2, int(self.N / 2) + 3):
                self.old_grid[j][int(self.N / 2) - 2] = 1
                self.old_grid[j][int(self.N / 2) + 2] = 1
            self.old_grid[int(self.N / 2) - 2][int(self.N / 2)] = 1
            self.old_grid[int(self.N / 2) + 2][int(self.N / 2)] = 1

    def live_neighbors(self, i, j):
        s = 0
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if (x == i and y == j):
                    continue
                elif(x != -1 and x != self.N and y != -1 and y != self.N):
                    s += self.old_grid[x][y]
        return s

    def state_change(self):
        pylab.pcolormesh(self.old_grid)
        pylab.colorbar()
        pylab.show()
        t = 1
        while t < self.T:
            for i in range(self.N):
                for j in range(self.N):
                    live = self.live_neighbors(i, j)
                    if (self.old_grid[i][j] == 1 and live < 2):
                        self.new_grid[i][j] = 0
                    elif (self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                        self.new_grid[i][j] = 1
                    elif (self.old_grid[i][j] == 1 and (live > 3)):
                        self.new_grid[i][j] = 0
                    elif (self.old_grid[i][j] == 0 and live == 3 ):
                        self.new_grid[i][j] = 1
            time.sleep(b)
            pylab.pcolormesh(self.new_grid)
            pylab.show()
            pylab.cla()
            self.old_grid = self.new_grid.copy()
            t += 1

if __name__ == '__main__':
    print("##########################")
    print("Select a Starting Pattern:")
    print("  1: Random Grid")
    print("  2: 10 cell Row")
    print("  3: Glider")
    print("  4: Exploder")
    choice = input("Your Choice (1-4):")
    a = 0
    if choice == "1":
        a = 1
    elif choice == "2":
        a = 2
    elif choice == "3":
        a = 3
    elif choice == "4":
        a = 4
    else:
        print("Invalid Choice!")
    print("Select a speed:")
    print("  1: Quick Speed")
    print("  2: Normal Speed")
    print("  3: Slow Speed")
    choice = input("Your Choice (1-3):")
    b = 0
    if choice == "1":
        b = 0.1
    elif choice == "2":
        b = 0.5
    elif choice == "3":
        b = 1
    else:
        print("Invalid Choice!")
    con = ConwayGame(N=int(input("请输入画布大小：")), T=int(input("请输入迭代次数：")))
    con.state_change()

