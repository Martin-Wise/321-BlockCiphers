import blockCiphers as bc

def test_padding1():
    assert bc.add_padding(bytes([0,10,11]), blocksize=16) == bytes([00,10,11,13,13,13,13,13,13,13,13,13,13,13,13,13])
    
def test_padding2():
    # should add a whole block of padding since the byte string is of length 16
    assert bc.add_padding(b"ThisIssixteenLen", blocksize=16) == b"ThisIssixteenLen" + bytes([16])*16

def test_padding3():
    # should add a whole block of padding but len is 8 insead of 16
    assert bc.add_padding(b"ThisIssixteenLen", blocksize=8) == b"ThisIssixteenLen" + bytes([8])*8

def test_padding4():
    assert bc.add_padding(b"ThisIsFiftenLen", blocksize=2) == b"ThisIsFiftenLen" + bytes([1])