def is_safe(x,y,maze,N):
    return (
        0<=x<N and 0<=y<N and maze[x][y]==1
    )


def solve_maze(maze):
    N=len(maze)

    sol=[[0 for _ in range(N)] for _ in range(N)]

