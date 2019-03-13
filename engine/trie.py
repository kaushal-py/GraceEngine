from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
import json

class Trie:

    def showTree(self, root):
        print(RenderTree(root, style=AsciiStyle()).by_attr())
        
    
    def traverseTree(self, node, cmd:list, length:int, cnt:int):
        
        '''
            This function receives a tree and the instruction and then executes the command
            If it has to work with json, first convert it into a tree using import.read(filehandle)
        '''


        '''Split the input commands and check each keyword hierarchically'''
        key = cmd[cnt]

        for child in node.children:
            if child.name == key:
                if cnt == length-1:
                    if child.isLeaf == True:
                        card_id = child.code
                        return (card_id,None)
                    else:
                        suggestions = []
                        for c in child.children:
                            suggestions.append(c.name)
                        return (None,suggestions)
                code = self.traverseTree(child, cmd, length, cnt+1)
                return code


    def addNode(self, node, cmd:str, code:str, cnt:int, init:int):
        key = cmd.split(' ',init+1)[init]
        flag = 0
        corresponding_code = None
        for child in node.children:
            if child.name == key:
                flag = 1
                if init != cnt-1:
                    self.addNode(child,cmd,code,cnt,init+1)
                else:
                    if child.isLeaf == False:
                        child.isLeaf = True
                        print("isLeaf value of ",child," has changed")
                    else:
                        print("Node already exists")
                    return
        if flag == 0:
            isLeaf = False
            if init == cnt-1:
                isLeaf = True
                corresponding_code = code
            newNode = Node(key, parent=node, isLeaf=isLeaf, code=corresponding_code)
            # TODO: find a way to assign True to isLeaf for correct nodes
            if init != cnt-1:
                self.addNode(newNode,cmd,code,cnt,init+1)


    '''Convert the given tree into json'''
    def toJson(self, root):
        exporter = JsonExporter(indent=2, sort_keys=False)
        print(exporter.export(root))

        with open('trie_disk.json','w') as f:
            exporter.write(root,f)

    
    def get_tree(self, file_name):

        ''' This function is used to import json file and return anytree Node '''
        importer = JsonImporter()
        tree_file = open(file_name, "r")
        data = tree_file.read()
        tree_file.close()
        return importer.import_(data)

if __name__ == '__main__':
    t = Trie()
    root = Node("*")

    query = "create array integers"
    query = query.split(' ')
    t.addNode(root,query,len(query),0)


    query = "create array integers"
    query = query.split(' ')
    t.addNode(root,query,len(query),0)


    query = "create list integers"
    query = query.split(' ')
    t.addNode(root,query,len(query),0)


    query = "repeat while"
    query = query.split(' ')
    t.addNode(root,query,len(query),0)

    query = "repeat while"
    query = query.split(' ')
    t.traverseTree(root,query,len(query),0)

    t.showTree(root)