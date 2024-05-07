import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        try:
            self._view._txt_result.controls.clear()
            self._model._graph.clear()
            self._model._list_flight_selected = None

            min_distance = int(self._view._txtIn.value)
            self._model.popolaFlight(min_distance)
            self._view._txt_result.controls.append(ft.Text(self._model._graph))
            self._view.update_page()
            print(self._model._graph)
            for edge in self._model._graph.edges.data():
                self._view._txt_result.controls.append(ft.Text(f"ORIGIN: {edge[0]._name} "
                                                               f"DESTINATION: {edge[1]._name} "
                                                               f"WEIGHT: {edge[-1]['weight']}"))
                self._view.update_page()

        except ValueError:
            print('Inserire un intero positivo')
        pass
