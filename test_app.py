import pytest
from dash import html, dcc
from app import SoulFoods_dash as app


def _materialize():
    layout = app.layout
    return layout() if callable(layout) else layout


def _walk(node):
    yield node
    children = getattr(node, "children", None)
    if children is None:
        return
    if isinstance(children, (list, tuple)):
        for c in children:
            yield from _walk(c)
    else:
        yield from _walk(children)


def _by_id(root, target_id):
    for n in _walk(root):
        if getattr(n, "id", None) == target_id:
            return n
    return None

#test 1 header
def test_header():
    layout = _materialize()
    h1 = None
    for node in _walk(layout):
        if isinstance(node, html.H1):
            h1 = node
            break
    assert h1 is not None
    assert "pink morsel sales" in h1.children.lower()

#test graph
def test_graph():
    layout = _materialize()
    graph = _by_id(layout, "sales-graph")
    assert graph is not None
    assert isinstance(graph, dcc.Graph)

# test region picker
def test_region_picker():
    layout = _materialize()
    picker = _by_id(layout, "region")
    assert picker is not None
    assert isinstance(picker, dcc.RadioItems)
