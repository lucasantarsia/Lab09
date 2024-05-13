import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()  # Tutti gli aeroporti
        self._flights = DAO.getAllFlights()  # Tutti i voli

        self._myGraph = nx.Graph()

        self._idMap = {}  # Definisco una mappa che ha come chiave l'id e come valore l'oggetto Aeroporto
        for a in self._airports:
            self._idMap[a.id] = a

    def buildGraph(self, distanzaMinima):
        """
        Creo il grafo pesato già filtrato, in modo tale da non avere gli archi in cui
        il peso (distanza media) è minore della distanza minima inserita dall'utente
        :param distanzaMinima: la distanza che inserisce l'utente nel dropdown
        """
        self._myGraph.clear()
        self._myGraph.add_nodes_from(self._airports)  # Inserisco tutti i nodi rappresentati da tutti gli aeroporti
        self.addEdge()  # Chiamo il metodo per aggiungere i nodi
        self.doFilterGraph(distanzaMinima)  # Chiamo il metodo che modifica e rimuove edges

    def addEdge(self):
        """
        Questo metodo aggiunge tutti gli archi presenti e ogni arco ha un proprio peso (attributo) che almeno
        inizialmente è rappresentato da una tupla: (numero di edges uguali che eventualmente si ripetono,
        somma delle distanze degli edges eventualmente ripetuti)
        """
        self._myGraph.clear_edges()
        for f in self._flights:
            airport1 = self._idMap[f.origin_airport_id]
            airport2 = self._idMap[f.destination_airport_id]
            if self._myGraph.has_edge(airport1, airport2):
                count = self._myGraph[airport1][airport2]["attr"][0] + 1
                sum = self._myGraph[airport1][airport2]["attr"][1] + f.distance
                self._myGraph[airport1][airport2]["attr"] = (count, sum)
            else:
                self._myGraph.add_edge(airport1, airport2, attr=(1, f.distance))

    def doFilterGraph(self, distanzaMinima):
        """
        Questo metodo ha due funzioni:
        1) Modifica gli edges: ogni edges ha come attributo la media delle distanze e non più una tupla
        2) Rimuove gli edges: tutti gli edges con distanza media >= distanzaMinima vengono eliminati
        """
        for u, v in self._myGraph.edges:  # Itero sulla lista degli edges
            sum = self._myGraph[u][v]["attr"][1]
            count = self._myGraph[u][v]["attr"][0]
            media = float(sum/count)
            if media >= distanzaMinima:  # Se la media è superiore diventa attributo dell'arco
                self._myGraph[u][v]["attr"] = media
            else:  # Altrimenti elimino l'arco (ma non i nodi)
                self._myGraph.remove_edge(u, v)

    """ 
    Questo metodo lo so uso nel caso abbia bisogno di filtrare (ed eliminare) archi
    del mio grafo, ma in questo caso non ne ho bisogno perché ho creato direttamente
    un grafo già filtrato in base alla distanza minima inserita dall'utente
    
    def getFilteredEdges(self, distanzaMinima):
        filteredEdges = []
        for u, v in self._myGraph.edges:
            distMedia = self._myGraph[u][v]["attr"]
            if distMedia >= distanzaMinima:
                filteredEdges.append((u, v, distMedia))
        return filteredEdges
        """

    def getNumNodes(self):
        return len(self._myGraph.nodes)

    def getNumEdges(self):
        return len(self._myGraph.edges)
