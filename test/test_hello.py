def test_hello(tracer):
    tracer.init()
    x = "hello world"  # LOAD_CONST, STORE_FAST
    y = x  # LOAD_FAST, STORE_FAST
    tracer.register()

    assert tracer.logger.changes == [
        {"target": "x", "value": "hello world", "sources": set()},
        {"target": "y", "value": "hello world", "sources": {"x"}},
    ]
