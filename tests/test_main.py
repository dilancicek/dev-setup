from veri_muhendisligi_staj.main import selamla


def test_selamla():
    sonuc = selamla("Dilan")
    assert sonuc == "Merhaba, Dilan! Stajın ilk günü kutlu olsun."
