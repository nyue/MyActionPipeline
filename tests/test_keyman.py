from snetwork import keyman

def test_keyman():
    assert(keyman.numKeys() > 0)
    pkm = keyman.PublicKeyManager()
    assert(pkm.valid())
