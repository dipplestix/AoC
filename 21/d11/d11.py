import sys
import numpy as np


class Octopus:
    def __init__(self, energy, adjacent_to):
        self.energy = energy
        self.adj = adjacent_to
        self.flashes = 0

    def add(self):
        if self.energy <= 9:
            self.energy += 1
            if self.energy > 9:
                self.flashes += 1
                return True
        return False

    def reset(self):
        if self.energy > 9:
            self.energy = 0


class OctopusField:
    def __init__(self, energies):
        self.octis = []
        nrows = len(energies)
        ncols = len(energies[0])
        for i, r in enumerate(energies):
            for j, e in enumerate(r):
                loc = j + i*ncols
                adj = []
                if i != 0:
                    adj.append(loc - ncols)
                    if (j % ncols) != 0:
                        adj.append(loc - ncols - 1)
                    if (j % ncols) != (ncols - 1):
                        adj.append(loc - ncols + 1)
                if i != (nrows - 1):
                    adj.append(loc + ncols)
                    if (j % ncols) != 0:
                        adj.append(loc + ncols - 1)
                    if (j % ncols) != (ncols - 1):
                        adj.append(loc + ncols + 1)
                if j != 0:
                    adj.append(loc - 1)
                if j != (ncols - 1):
                    adj.append(loc + 1)
                self.octis.append(Octopus(e, adj))

    def run(self, n_rounds):
        for r in range(n_rounds):
            round_count = 0
            activate = list(range(len(self.octis)))
            while activate:
                o = self.octis[activate.pop()]
                flash = o.add()
                if flash:
                    round_count += 1
                    activate.extend(o.adj)
            for o in self.octis:
                o.reset()
        return sum([o.flashes for o in self.octis])

    def find_round(self):
        all_flash = False
        r = 0
        while True:
            flash_count = 0
            activate = list(range(len(self.octis)))
            while activate:
                o = self.octis[activate.pop()]
                flash = o.add()
                if flash:
                    flash_count += 1
                    activate.extend(o.adj)
            for o in self.octis:
                o.reset()
            r += 1
            if not all_flash and flash_count == 100:
                return r


def count_flashes(file_name):
    energies = []
    with open(file_name, 'r') as f:
        for i, octis in enumerate(f):
            energies.append([int(n) for n in octis[:-1]])
    energies = np.array(energies)
    field = OctopusField(energies)
    flashes = field.run(100)
    return flashes


def count_simul_flashes(file_name):
    energies = []
    with open(file_name, 'r') as f:
        for i, octis in enumerate(f):
            energies.append([int(n) for n in octis[:-1]])
    energies = np.array(energies)
    field = OctopusField(energies)
    r = field.find_round()
    return r


if __name__ == "__main__":
    tot_flashes = count_flashes(sys.argv[1])
    print(tot_flashes)
    round_bright = count_simul_flashes(sys.argv[1])
    print(round_bright)
