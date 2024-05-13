import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.controls.clear()
        if self.readDistanzaMinima() is None:
            self._view._txt_result.controls.append(ft.Text("Inserire una distanza minima!"))
            self._view.update_page()
            return
        self._model.buildGraph(self.readDistanzaMinima())
        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view._txt_result.controls.append(ft.Text("Grafo pesato creato correttamente."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nEdges} archi."))
        if nEdges != 0:
            self._view._txt_result.controls.append(ft.Text("Elenco di tutti gli archi:"))
            self.stampaEdges()
        self._view.update_page()

    def readDistanzaMinima(self):
        """
        Leggo il valore di quello che inserisce l'utente
        """
        try:
            return float(self._view._txtIn.value)
        except:
            return None

    def stampaEdges(self):
        """
        Stampo la lista degli edges
        """
        for edge in self._model._myGraph.edges:
            distMedia = self._model._myGraph.get_edge_data(edge[0], edge[1])['attr']
            self._view._txt_result.controls.append(ft.Text(f"{edge[0].airport} -> {edge[1].airport} -- AvgDist: {distMedia}"))
