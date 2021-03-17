from quote.lib import get_quote

def test_qoute_length():
	quote=get_quote()
	assert len(quote)!=0