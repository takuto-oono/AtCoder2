import numpy as np


class ABC266C:
    def __init__(self) -> None:
        self.coordinates = [tuple(map(int, input().split())) for _ in range(4)]
        self.angles = [self.calc_angle(i) for i in range(4)]

    def calc_angle(self, vertex_index: int) -> float:
        o = np.array(list(self.coordinates[vertex_index]))
        p = np.array(list(self.coordinates[(vertex_index + 1) % 4]))
        q = np.array(list(self.coordinates[(vertex_index - 1) % 4]))

        vec_p = p - o
        vec_q = q - o

        cos_poq = np.inner(vec_p, vec_q) / \
            (np.linalg.norm(vec_p) * np.linalg.norm(vec_q))
        return np.rad2deg(np.arccos(cos_poq))

    def is_convex(self) -> bool:
        for i in range(4):
            sum_3_angles = 0
            for j in range(i, i + 3):
                sum_3_angles += self.angles[j % 4]
            if sum_3_angles <= 180:
                return False

        return True


if __name__ == '__main__':
    if ABC266C().is_convex():
        print('Yes')
    else:
        print('No')
