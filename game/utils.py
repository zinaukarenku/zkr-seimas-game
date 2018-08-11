def try_parse_int(value):
    if value:
        try:
            return int(value)
        except ValueError:
            return None
