import random
import time

from preproccess.graph import Graph

"""
Perform random walks on a given graph.
"""


class RandomWalk():
    def __init__(self, graph):
        self.graph = graph

    def walk(self, time, length):
        self.ent_paths = []
        self.rel_paths = []
        ents = list(self.graph.ent_set)
        rel_set = set()
        for i in range(time):
            random.shuffle(ents)
            for e in ents:
                s, e_path, r_path = e, e, ''
                for _ in range(length):
                    s_ = random.choice(list(self.graph.graph_eer[s].keys()))
                    r = random.choice(self.graph.graph_eer[s][s_])
                    rel_set.add(r)
                    r_path += ' ' + r
                    e_path += ' ' + s_
                    s = s_
                self.ent_paths.append(e_path)
                self.rel_paths.append(r_path)
        return len(rel_set)

    def save(self, path):
        """Save the paths generated by random walks as csv format files, e.g., one line in the files (one path): e1 e2 e3, r1 r2"""
        with open(path, 'w') as f:
            for ep, rp in zip(self.ent_paths, self.rel_paths):
                f.write(ep + ',' + rp + '\n')