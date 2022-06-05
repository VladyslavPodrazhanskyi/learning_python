import re
from typing import Optional, Dict

file_key = 'gl_accounts_iafa.csv'


"Compile a regular expression pattern, returning a Pattern object."
pattern = re.compile(
    r'(.+/)?'
    r'(?P<object_name>.+?)'
    r'_?(?P<object_type>data|schema)?'
    r'_?(?P<batch_id>\d{8}_\d{6})?'
    r'\.(?P<extension>[a-zA-Z]+)'
    r'\.?(?P<compression>.+)?'
)

re_group = pattern.match(file_key).groupdict()

print(re_group)


def get_extension(file_key: str) -> Optional[str]:
    regroup = _get_regroup(file_key)
    return regroup.get("extension")


def get_compression(file_key: str) -> Optional[str]:
    regroup = _get_regroup(file_key)
    return regroup.get("compression")


def _get_regroup(file_key: str) -> Dict[str, str]:
    _pattern = re.compile(
        r'(?P<object_name>.+?)'
        r'\.(?P<extension>[a-zA-Z]+)'
        r'\.?(?P<compression>.+)?'
    )
    return _pattern.match(file_key).groupdict()