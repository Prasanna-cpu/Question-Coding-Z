def is_safe(x,y,maze,N):
    return (
        0<=x<N and 0<=y<N and maze[x][y]==1
    )


def solve_maze(maze):
    N=len(maze)

    sol=[[0 for _ in range(N)] for _ in range(N)]

    def solve(x,y):
        if x==N-1 and y==N-1:
            sol[x][y]="_"
            return True

        if is_safe(x,y,maze,N):
            sol[x][y]="_"

            if solve(x,y+1):
                return True

            if solve(x+1,y):
                return True

            if solve(x,y-1):
                return True

            if solve(x-1,y):
                return False


            sol[x][y]=0
            return False

        return False

    if solve(0,0):
        for row in sol:
            print(' '.join(str(cell) for cell in row))

    else:
        print("No solution exists")