"""
Data casts that can be performed by painless script:
    explicit = ctx._source.some.field = (type)ctx._source.some.other.field;
    implicit = ctx._source.some.field = ctx._source.some.other.field;
    ...
"""
cast_table = {
    "byte": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit"
    },
    "short": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit",
    },
    "char": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit"
    },
    "integer": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit",
    },
    "long": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit",
        "date": "long_to_date",
    },
    "float": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit",
    },
    "double": {
        "byte": "explicit",
        "short": "explicit",
        "char": "explicit",
        "integer": "explicit",
        "long": "explicit",
        "float": "explicit",
        "double": "explicit"
    },
    "text": {
        "text": "implicit",
        "string": "implicit",
        "match_only_text": "implicit",
        "keyword": "implicit",
        "constant_keyword": "implicit",
        "wildcard": "implicit",
    },
    "string": {
        "text": "implicit",
        "string": "implicit",
        "match_only_text": "implicit",
        "keyword": "implicit",
        "constant_keyword": "implicit",
        "wildcard": "implicit"
    },
    "match_only_text": {
        "text": "implicit",
        "string": "implicit",
        "match_only_text": "implicit",
        "keyword": "implicit",
        "constant_keyword": "implicit",
        "wildcard": "implicit"
    },
    "keyword": {
        "text": "implicit",
        "string": "implicit",
        "match_only_text": "implicit",
        "keyword": "implicit",
        "constant_keyword": "implicit",
        "wildcard": "implicit"
    },
    "constant_keyword": {
        "text": "implicit",
        "string": "implicit",
        "match_only_text": "implicit",
        "keyword": "implicit",
        "constant_keyword": "implicit",
        "wildcard": "implicit"
    },
    "wildcard": {
        "text": "implicit",
        "string": "implicit",
        "match_only_text": "implicit",
        "keyword": "implicit",
        "constant_keyword": "implicit",
        "wildcard": "implicit"
    },
    "_complex": {
        "object": "implicit"
    },
    "object": {
        "_complex": "implicit"  # DEV'S PROBLEM, FIELDS IN COMPLEX MUST HAVE DEFAULT VALUES IF NOT PROVIDED
    },
    "date": {
        "long": "date_to_long"
    }
}
