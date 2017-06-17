# vim: set expandtab shiftwidth=4 softtabstop=4:

import sys
print(sys.version + "\n" + sys.executable)
print("-"*50 + "\n")

# def open_mol2(session, stream, name):
#     structures = []
#     atoms = 0
#     bonds = 0
#     while True:
#         s = _read_block(session, stream)
#         if not s:
#             break
#         structures.append(s)
#         atoms += s.num_atoms
#         bonds += s.num_bonds
#     status = ("Opened mol2 file containing {} structures ({} atoms, {} bonds)".format
#               (len(structures), atoms, bonds))
#     return structures, status






def print_lines(stream, num_of_lines=None):
    """for testing purposes only. delete later"""
    if num_of_lines is None:
        num_of_lines = 1
    print("\n" + ("=")*30 + "\nbeginning test print...\n" + ("=")*30 + "\n")
    for _ in range(0, num_of_lines):
        print(stream.readline().strip())
    print("\n" + ("=")*30 + "\nending test print\n"+("=")*30 + "\n")




def _read_block(session, stream):
    """test docstring"""
    # First section should be commented out
    # Second section: "@<TRIPOS>MOLECULE"
    # Third section: "@<TRIPOS>ATOM"
    # Fourth section: "@<TRIPOS>BOND"
    # Fifth section: "@<TRIPOS>SUBSTRUCTURE"

    import ast
    from numpy import (array, float64)
    from chimerax.core.atomic import AtomicStructure

    # s = AtomicStructure(session)


    property_dict = {}

    comment = stream.readline()
    while comment[0] == "#":
        line = comment.replace("#", "")
        parts = line.split(":")
        parts = [item.strip() for item in parts]
        if ":" not in line:
            for i in range(len(line), 1, -1):
                if line[i-1] == " ":
                    property_dict[line[:i].strip()] = line[i:].strip()
                    break
        else:
            try:
                property_dict[str(parts[0])] = ast.literal_eval(parts[1])

            except ValueError:
                property_dict[str(parts[0])] = str(parts[1])

        comment = stream.readline()

    for key, value in property_dict.items():
        print(key, ":", value)

    while "@<TRIPOS>MOLECULE" not in stream.readline().strip():
        pass

    mol_dict = {}
    

    # Property Dictionary should be completed at this point

    ###test print. Delete later
    # print()
    # for i in property_dict:
    #     val = property_dict[i]
    #     print(str(val) + " : " + str(type(val)))


    while "@<TRIPOS>ATOM" not in stream.readline().strip():
        pass

    ###TEMP STATEMENT###
    atom_count = 20

    ###
    atom_dict = {}

    for n in range(atom_count):
        atom_line = stream.readline()
        if not atom_line:
            print("no line found")
            return None
        parts = atom_line.split()
        if len(parts) != 9:
            print("error: not enough entries")
            return None
        if not isinstance(int(parts[0]), int):
            print("error: first value is needs to be an integer")
            return None
        
        val_list = []
        atom_dict[int(parts[0])] = val_list
        for v in parts[1:]:
            try:
                val_list.append(ast.literal_eval(v))
            except ValueError:
                val_list.append(str(v))
            except SyntaxError:
                val_list.append(str(v))
    for key, value in atom_dict.items():
        print(key, ":", value)

        # try:
        #     # atom_dict[int(parts[0])] = 
        #     pass







        # stream.close()


# _read_block(None, open("ras.mol2", "r"))
_read_block(None, open("ras(short_version).mol2", "r"))


# note to self: try to ask if you can do a pip install package that would
# not disappear
