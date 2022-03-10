from calc import calculadora


def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculadora, "sumar", lambda x: 4)
    cal = calculadora()
    assert cal.sumar() == 4
