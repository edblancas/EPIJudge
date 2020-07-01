import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    def possible(p: Coordinate):
        rows = len(maze)
        # the nex was wrong because p.y is the col, but also is wrong
        # p.x, because this test if it is possible to go to that coordinate
        # so invalid coordinates can be passed, hence, can be a index
        # out of range, that's why we need to put a 0
        # cols = len(maze[p.y])
        cols = len(maze[0])
        # print(rows, cols)
        if 0 <= p.y < cols and 0 <= p.x < rows and maze[p.x][p.y] == WHITE:
            # print(True)
            return True
        # print(False)
        return False

    v = set()
    # up, right, down, left
    go = [Coordinate(-1, 0), Coordinate(0, 1), Coordinate(1, 0), Coordinate(0, -1), ]

    r = collections.deque()
    q = collections.deque()
    q.append(s)
    # WRONG: We are tempted to doit as a dict with a list
    # because most possible than a node have more than one
    # parent, but as is BFS any node give us the shortest path.
    # paths = collections.defaultdict(list)
    paths = collections.defaultdict(list)

    def bfs():
        found = False
        while q:
            curr = q.popleft()
            # add this check
            if curr in v:
                continue
            v.add(curr)
            # there maybe coordinates printed repeated, that is
            # because we added to the queue before it was in the
            # set v (visited), but the next time when we try to
            # add its neighbors, it is gonna be in v, so the neighbors
            # are not gonna be added double.
            # print(curr)
            if curr == e:
                found = True
                break
            for p in go:
                next_p = Coordinate(curr.x + p.x, curr.y + p.y)
                if possible(next_p) and next_p not in v:
                    q.append(next_p)
                    # here we can see that a next_p can have more than
                    # one parent curr, but we can take anyone, so we
                    # only keep track of one parent
                    # paths[next_p].append(curr)
                    # print('-->', len(paths[next_p]))
                    paths[next_p] = curr
        return found

    if bfs():
        r.append(e)
        curr = e
        while curr != s:
            curr = paths[curr]
            r.appendleft(curr)
    else:
        return []
    return list(r)


def search_maze_dfs(maze: List[List[int]], s: Coordinate,
                    e: Coordinate) -> List[Coordinate]:
    """
    This approach takes
    space O(|E|), E being the total of edges, as the call stack
    time O(|V| + |E|), V being the total of edges, as we traverse all
        the edges and all the vertices

    :param maze:
    :param s:
    :param e:
    :return:
    """

    def possible(p: Coordinate):
        rows = len(maze)
        # the nex was wrong because p.y is the col, but also is wrong
        # p.x, because this test if it is possible to go to that coordinate
        # so invalid coordinates can be passed, hence, can be a index
        # out of range, that's why we need to put a 0
        # cols = len(maze[p.y])
        cols = len(maze[0])
        # print(rows, cols)
        if 0 <= p.y < cols and 0 <= p.x < rows and maze[p.x][p.y] == WHITE:
            # print(True)
            return True
        # print(False)
        return False

    v = set()
    # left, right, down, up
    go = (Coordinate(0, -1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1, 0))
    r = []

    def solve(c):
        # print(c)
        if c == e:
            return True
        v.add(c)
        for p in go:
            new_c = Coordinate(c.x + p.x, c.y + p.y)
            # print(new_c)
            if possible(new_c) and new_c not in v:
                if solve(new_c):
                    # we are adding the coordinate where we came from
                    # hence, we need the s coordinate at the end of the
                    # list, then reverse it
                    r.append(Coordinate(new_c.x, new_c.y))
                    return True
        return False

    if not solve(s):
        return []
    # we need to put it here before reverse it
    r.append(s)
    r.reverse()
    # print(r)
    return r


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
