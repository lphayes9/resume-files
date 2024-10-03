#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <ostream>

void createMaze(int n, int m, std::vector<std::vector<int>>& maze, unsigned int seed) {
    maze.assign(n, std::vector<int>(m, 15));
    std::srand(seed);

    std::vector<int> current = {0, 0};
    std::vector<std::vector<int>> visited {{0,0}};

    while(!visited.empty()) {
        int y = current[0];
        int x = current[1];
        std::vector<std::vector<int>> neighbors;
        if (y-1 >= 0) {
            if (maze[y-1][x] == 15) {
                neighbors.push_back({y-1, x});
            }
        }
        if (y+1 < n) {
            if (maze[y+1][x] == 15) {
                neighbors.push_back({y+1, x});
            }
        }
        if (x+1 < m) {
            if (maze[y][x+1] == 15) {
                neighbors.push_back({y, x+1});
            }
        }
        if (x-1 >= 0) {
            if (maze[y][x-1] == 15) {
                neighbors.push_back({y, x-1});
            }
        }

        if (neighbors.empty()) {
            current = visited[visited.size()-1];
            visited.pop_back();
        }

        else {
            int idx = std::rand() / ((RAND_MAX + 1u) / neighbors.size());

            if (neighbors[idx][0] == y-1) {
                maze[y][x] -= 8;
                maze[neighbors[idx][0]][neighbors[idx][1]] -= 4;
            }
            if (neighbors[idx][0] == y+1) {
                maze[y][x] -= 4;
                maze[neighbors[idx][0]][neighbors[idx][1]] -= 8;
            }
            if (neighbors[idx][1] == x+1) {
                maze[y][x] -= 2;
                maze[neighbors[idx][0]][neighbors[idx][1]] -= 1;
            }
            if (neighbors[idx][1] == x-1) {
                maze[y][x] -= 1;
                maze[neighbors[idx][0]][neighbors[idx][1]] -= 2;
            }

            visited.push_back(current);
            current = neighbors[idx];
        }
    }
    maze[0][0] -= 8;
    maze[n-1][m-1] -= 4;
}   
void createFile(const std::vector<std::vector<int>> maze, const std::string fname) {
    std::ofstream outFile(fname);
    if (outFile.is_open()) {
        for (std::vector<int> row : maze) {
            for (int cell : row) {
                outFile << cell << " ";
            }
            outFile << std::endl;
        }
        outFile.close();
    } 
}



