#ifndef MAZE_H
#define MAZE_H
#include <vector>
#include <string>

void createMaze(int n, int m, std::vector<std::vector<int>>& maze, unsigned int seed);
void createFile(const std::vector<std::vector<int>> maze, const std::string fname);


#endif

