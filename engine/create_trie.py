'''
    This File is used to insert all the commands in trie_commands.csv into trie.json
'''


from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
from trie import Trie
import csv

t = Trie()

with open("trie.json","r") as f:
    importer = JsonImporter()
    csv_dict = [row for row in csv.DictReader(f)]
    if len(csv_dict) == 0:
        root = Node("*")
    else:
        root = t.get_tree('trie.json')

print(RenderTree(root))

with open("trie_commands.csv","r") as f:
    rows = csv.reader(f)
    for row in rows:
        print(row[0],row[1])

        t.addNode(root, row[0], row[1], len(row[0].split()), 0)
        '''Trie.addNode(root,query,corresponding_code,length_of_query,index)'''
            
t.toJson(root)