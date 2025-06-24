from app.services.memory_parser import MemoryParserAgent

memory_parser = MemoryParserAgent()

def test_parse_memory(parser = memory_parser):
    # Test the 'text' parser
    test_string = "Went to goa last weekend."
    result = parser.parse_memory("text", test_string)
    assert type(result) == dict