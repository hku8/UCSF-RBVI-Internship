# vim: set expandtab shiftwidth=4 softtabstop=4:


def open_mol2(session, stream, name):
    structures = []
    atoms = 0
    bonds = 0
    while True:
        s = _read_block(session, stream)
        if not s:
            break
        structures.append(s)
        atoms += s.num_atoms
        bonds += s.num_bonds
    status = ("Opened mol2 file containing {} structures ({} atoms, {} bonds)".format
              (len(structures), atoms, bonds))
    return structures, status


def _read_block(session, stream):

    # First section should be commented out
    # Second section: "@<TRIPOS>MOLECULE"
    # Third section: "@<TRIPOS>ATOM"
    # Fourth section: "@<TRIPOS>BOND"
    # Fifth section: "@<TRIPOS>SUBSTRUCTURE"

    # count_line = stream.readline()
    # if not count_line:
    #     return None
    # try:
    #     count = int(count_line)
    # except ValueError:
    #     # XXX: Should emit an error message
    #     return None
    # from chimerax.core.atomic import AtomicStructure
    # s = AtomicStructure(session)

    comment = stream.readline()

    first_sec = []
    property_dic = {}

    while comment[0] == "#":
        line = comment.replace("#", "")
        parts = line.split(":")
        parts = [item.strip() for item in parts]
        if ":" not in line:
            for i in range(len(line), 1, -1):
                if line[i-1] == " ":
                    property_dic.update({line[:i].strip(): line[i:].strip()})
                    break
        else:
            try:
                property_dic[str(parts[0])] = float(parts[1])

            except ValueError:
                property_dic[str(parts[0])] = str(parts[1])

        first_sec.append(line)
        comment = stream.readline()

    for k, v in property_dic.items():
        print(k, ":", v)
    # print(property_dic)

    while True:
        count_line = stream.readline()
        if "@<TRIPOS>ATOM" in count_line:
            stream.readline()

            break
    # while count_line[0].isdigit:
    #     print(stream.readline())
    # return s


_read_block(None, open("ras.mol2", "r"))


# try to ask if you can do a pip install package that would not disappear
