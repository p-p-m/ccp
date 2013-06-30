from bio.models import Request, DBSignal


def test_signals():
    # create
    r = Request(meta='meta', path='path')
    r.save()
    signal = DBSignal.objects.latest()
    assert signal.table_name == Request.__name__
    assert signal.status == 'created'
    # update
    r.meta = 'meta2'
    r.save()
    signal = DBSignal.objects.latest()
    assert signal.table_name == Request.__name__
    assert signal.status == 'modified'
    # delete
    r.delete()
    signal = DBSignal.objects.latest()
    assert signal.table_name == Request.__name__
    assert signal.status == 'deleted'
