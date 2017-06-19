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

    from numpy import (array, float64)
    from chimerax.core.atomic import AtomicStructure

    read_comments(session, stream)
    read_molecule(session, stream)
    # read_atom(session, stream)
    # read_bond(session, stream)
    # read_substructure(session, stream)

    # s = AtomicStructure(session)


def read_comments(session, stream):

    import ast
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

def read_molecule(sesson, stream):

    import ast
    while "@<TRIPOS>MOLECULE" not in stream.readline():
        pass
    molecular_dict = {}
    mol_lables = ["mol_name", ["num_atoms", "num_bonds", "num_subst", "num_feat", "num_sets"],\
    "mol_type", "charge_type", "status_bits"]
    print(len(mol_lables))

    for label in mol_lables:
        molecule_line = stream.readline().split()
        print(molecule_line)
        print(label)
        try:
            if all(isinstance(ast.literal_eval(item), int) for item in molecule_line):
                # print(molecule_line)
                pass

        except ValueError:
            print("VALUERROR")
        except SyntaxError:
            print("test")



    # Property Dictionary should be completed at this point

    # test print to check value types. Delete later
    # print()
    # for i in property_dict:
    #     val = property_dict[i]
    #     print(str(val) + " : " + str(type(val)))


def read_atom(session, stream):

    import ast
    while "@<TRIPOS>ATOM" not in stream.readline():
        pass

    ###TEMP STATEMENT. ADD HANNAH'S CODE###
    atom_count = 22
    ###

    atom_dict = {}

    for _ in range(atom_count):
        atom_line = stream.readline()
        if not atom_line[0].isdigit: ###THIS DOES NOT WORK
            print(atom_line)
            print("FAILED")
            break
        if not atom_line:
            print("no line found")
            return None
        parts = atom_line.split()
        if len(parts) != 9:
            print("error: not enough entries")
            return None
        # if not isinstance(int(parts[0]), int):
        #     print("error: first value is needs to be an integer")
        #     return None

        val_list = []
        atom_dict[int(parts[0])] = val_list
        for value in parts[1:]:
            try:
                val_list.append(ast.literal_eval(value))
            except (ValueError, SyntaxError):
                val_list.append(str(value))

    # PRINT TEST. DELETE LATER
    for key, value in atom_dict.items():
        print(key, ":", value)


def read_bond(session, stream):

    while "@<TRIPOS>BOND" not in stream.readline():
        pass

    ###TEMP STATEMENT. ADD HANNAH'S CODE###
    bond_count = 22
    ###

    bond_dict = {}

    for _ in range(bond_count):
        bond_line = stream.readline()
        parts = bond_line.split()
        if len(parts) != 4:
            print("error: not enough entries in under bond data")
        if not isinstance(int(parts[0]), int):
            print("error: first value is needs to be an integer")
            return None

        bond_dict[int(parts[0])] = parts[1:3]

    for key, value in bond_dict.items():
        print(key, ":", value)


def read_substructure(session, stream):

    while "@<TRIPOS>SUBSTRUCTURE" not in stream.readline():
        pass

    substructure_line = stream.readline().split()
    # substructure_prop = {
    # "subst_id" : ,
    # "subst_name" :,
    # "root_atom" : ,
    # "subst_type" : ,
    # "dict_type" : ,
    # }

    # stream.close()


# _read_block(None, open("ras.mol2", "r"))
_read_block(None, open("ras(short_version).mol2", "r"))


# note to self: try to ask if you can do a pip install package that would
# not disappear
