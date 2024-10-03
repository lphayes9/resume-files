#include "maze.h"
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <vector>
#include <string>

int main(int argc, char* argv[]) {
    std::vector<std::vector<int>> maze;
    unsigned int seed = std::atoi(argv[1]);
    int n = std::atoi(argv[2]);
    int m = std::atoi(argv[3]);
    std::string fname = argv[4];
    createMaze(n, m, maze, seed);
    createFile(maze, fname);

    return 0;
}
