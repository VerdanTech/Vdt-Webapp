def url_to_route_name(prefix: str, url: str) -> str:
    """
    Constructs a route operation ID / name from a URL.

    Args:
        url (str): the url to convert.

    Returns:
        str: the equivalent route ID.
    """
    url = url.replace("/", "_")
    return prefix + url
