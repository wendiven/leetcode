#!/usr/bin/env python2
'''
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        if not edges or len(edges) == 0:
            return [0]

        minHeight = n
        min_root = []
        for i in range(n):
            edges_t = edges[:]
            queue = [i]
            depth = 0
            while queue:
                new_queue = []
                while queue:
                    v = queue.pop(0)
                    for j in range(len(edges_t)-1, -1, -1):
                        if edges_t[j][0] == v:
                            new_queue.append(edges_t[j][1])
                            edges_t.pop(j)
                        elif edges_t[j][1] == v:
                            new_queue.append(edges_t[j][0])
                            edges_t.pop(j)
                queue = new_queue
                depth += 1
            if depth < minHeight:
                min_root = [i]
                minHeight = depth
            elif depth == minHeight:
                min_root.append(i)
        return min_root
'''
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        if not edges or len(edges) == 0:
            return [0]

        adjacency = {}
        for x,y in edges:
            if x not in adjacency:
                adjacency[x] = []
            adjacency[x].append(y)
            if y not in adjacency:
                adjacency[y] = []
            adjacency[y].append(x)


        minHeight = n
        min_root = []
        for i in range(n):
            queue = [i]
            depth = 0
            adjacency_t = {}
            for k,v in adjacency.items():
                adjacency_t[k] = v[:]
            while queue:
                new_queue = []
                while queue:
                    src = queue.pop(0)
                    dest = adjacency_t[src]
                    for d in dest:
                        adjacency_t[d].remove(src)
                    new_queue.extend(dest)
                queue = new_queue
                depth += 1
            if depth < minHeight:
                min_root = [i]
                minHeight = depth
            elif depth == minHeight:
                min_root.append(i)
        return min_root

s = Solution()
print s.findMinHeightTrees(252, [[0,1],[0,2],[2,3],[3,4],[2,5],[1,6],[5,7],[3,8],[6,9],[7,10],[4,11],[3,12],[10,13],[0,14],[6,15],[7,16],[10,17],[11,18],[0,19],[3,20],[14,21],[14,22],[22,23],[9,24],[17,25],[12,26],[15,27],[11,28],[4,29],[6,30],[26,31],[28,32],[30,33],[22,34],[33,35],[26,36],[1,37],[31,38],[4,39],[11,40],[22,41],[6,42],[12,43],[36,44],[13,45],[39,46],[2,47],[21,48],[27,49],[28,50],[35,51],[29,52],[29,53],[40,54],[36,55],[38,56],[27,57],[56,58],[8,59],[49,60],[25,61],[24,62],[54,63],[49,64],[52,65],[16,66],[59,67],[40,68],[62,69],[36,70],[40,71],[50,72],[59,73],[60,74],[26,75],[73,76],[76,77],[28,78],[21,79],[66,80],[41,81],[66,82],[32,83],[68,84],[73,85],[70,86],[54,87],[20,88],[44,89],[32,90],[81,91],[18,92],[16,93],[50,94],[10,95],[26,96],[76,97],[25,98],[10,99],[53,100],[37,101],[58,102],[36,103],[91,104],[47,105],[74,106],[62,107],[66,108],[4,109],[59,110],[31,111],[86,112],[103,113],[109,114],[32,115],[97,116],[90,117],[80,118],[108,119],[69,120],[28,121],[83,122],[44,123],[85,124],[10,125],[17,126],[104,127],[121,128],[25,129],[0,130],[73,131],[10,132],[95,133],[129,134],[37,135],[114,136],[55,137],[68,138],[112,139],[0,140],[122,141],[86,142],[108,143],[53,144],[49,145],[74,146],[52,147],[0,148],[114,149],[88,150],[73,151],[127,152],[113,153],[34,154],[146,155],[127,156],[5,157],[90,158],[2,159],[37,160],[90,161],[46,162],[152,163],[39,164],[107,165],[101,166],[93,167],[115,168],[111,169],[68,170],[132,171],[135,172],[69,173],[114,174],[35,175],[35,176],[52,177],[15,178],[144,179],[0,180],[141,181],[146,182],[147,183],[117,184],[121,185],[111,186],[104,187],[8,188],[43,189],[154,190],[97,191],[22,192],[189,193],[176,194],[61,195],[124,196],[82,197],[161,198],[133,199],[195,200],[125,201],[111,202],[17,203],[43,204],[18,205],[48,206],[167,207],[116,208],[199,209],[12,210],[45,211],[54,212],[212,213],[137,214],[8,215],[99,216],[163,217],[185,218],[177,219],[99,220],[183,221],[201,222],[111,223],[52,224],[120,225],[143,226],[35,227],[8,228],[228,229],[187,230],[169,231],[93,232],[231,233],[75,234],[5,235],[219,236],[168,237],[30,238],[130,239],[77,240],[218,241],[185,242],[40,243],[57,244],[135,245],[13,246],[24,247],[246,248],[126,249],[45,250],[237,251]])