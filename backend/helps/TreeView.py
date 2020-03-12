class TreeView:

    '''
    组装列表
    格式： list = [[id, name, ... ], [id, name, ...]]
    '''
    def ListLayerTree(self, data, pid = None, level = 1):
        trees = []
        for obj in data:
           if obj['parent_id'] == pid:
                nextLevel = level + 1
                tree = {}
                tree['id'] = obj['id']
                tree['parent_id'] = pid
                tree['name'] = obj['name']
                tree['level'] = level
                tree['sort'] = obj['sort']
                tree['status'] = obj['status']
                tree['module'] = obj['module']
                tree['children'] = []
                
                children    = self.ListLayerTree(data, obj['id'], nextLevel)
                if children:
                    tree['children'] = children
                trees.append(tree)
        return trees

    '''
    组装列表
    格式： list = [[id, name, ... ], [id, name, ...]]
    '''
    def ListTree(self, data, pid = None, level = 1):
        trees = []
        for obj in data:
           if obj['parent_id'] == pid:
                nextLevel = level + 1
                tree = {}
                tree['id'] = obj['id']
                tree['parent_id'] = pid
                tree['name'] = obj['name']
                tree['level'] = level
                tree['sort'] = obj['sort']
                tree['status'] = obj['status']
                tree['module'] = obj['module']
                trees.append(tree)
                children    = self.ListTree(data, obj['id'], nextLevel)
                if children:
                    trees.extend(children)
        return trees

    '''
    组装options
    格式： choices = [[1, 'SH'], [2, 'BJ']]
    '''
    def ListOptions(self, data, pid = None, level = 1):
        options = []
        for obj in data:
            if obj['parent_id'] == pid:
                nextLevel = level + 1
                if level == 1:
                    nameStr = ''*level
                else:
                    nameStr = '―'*level
                tree = []
                tree.append(obj['id'])
                tree.append(nameStr + obj['name'])
                options.append(tree)

                children    = self.ListOptions(data, obj['id'], nextLevel)
                if children:
                    options.extend(children)
                
        return options