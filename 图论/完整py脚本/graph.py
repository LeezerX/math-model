from typing import Optional

WEIGHT_TYPE = float  # 两节点之间的距离的类型


class Vertex:

    def __init__(self, id) -> None:
        self.__id = id
        self.__conneted_to: dict[Vertex, WEIGHT_TYPE] = {}  # 所连接的节点以及距离

    @property
    def id(self):
        """返回该节点的id
        """
        return self.__id

    def get_connetions(self)->Optional[set['Vertex']]:
        """返回该节点所有连接的节点

        Returns
        -------
        set[Vertex] or None
            所有连接的点的集合
        """        
        return self.__conneted_to.keys()

    def get_weight(self,nbr:'Vertex')->WEIGHT_TYPE:
        """返回该节点与另一节点的距离

        Parameters
        ----------
        nbr : Vertex
            节点实例
        """
        return self.__conneted_to[nbr]

    def add_neighbor(self,nbr:'Vertex',weight:WEIGHT_TYPE):
        """给该节点添加一个相邻节点

        Parameters
        ----------
        nbr : Vertex
            相邻的节点
        weight : WEIGHT_TYPE
            节点间的距离
        """
        self.__conneted_to[nbr] = weight

class Graph:
    def __init__(self):
        self.__vertex_list:dict[int,Vertex] = {} # 该图中的所有节点
        self.__vertex_num:int = 0 # 该图的节点数

    @property
    def size(self)->int:
        """返回图中的节点数

        Returns
        -------
        int
            节点个数
        """
        return self.__vertex_num

    def __contains__(self,v):
        return v in self.__vertex_list.values() or v in self.__vertex_list # 默认查询是否在keys

    def add_vertex(self,id):
        """新增节点

        Parameters
        ----------
        v : Vertex
            新增的节点
        """
        self.__vertex_num += 1
        v = Vertex(id)
        self.__vertex_list[id] = v

    def add_edge(self,f:int,t:int,weight:WEIGHT_TYPE):
        """给图中的两个节点新增一条边

        Parameters
        ----------
        f : int
            开始
        t : int
            终止
        weight : WEIGHT_TYPE
            权值
        """
        # 如果节点不在图中,则要添加到图中
        if f not in self.__vertex_list:
            self.add_vertex(f)
        if t not in self.__vertex_list:
            self.add_vertex(t)
        self.__vertex_list[f].add_neighbor(self.__vertex_list[t],weight)

    def __iter__(self):
        return iter(self.__vertex_list.values())

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)
    g.add_edge(3,5,3)
    for v in g:
        for w in v.get_connetions():
            print(f"({v.id},{w.id},{v.get_weight(w)})")
