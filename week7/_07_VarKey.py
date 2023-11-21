def get(url, params=None, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:'Request' object.
    :param params: (optional) Dictionary, list of tuples o
        in the query string for the :class:'Request'.
    :param \*\*kwargs: Optional arguments that ''request''
    :return: :class:'Response <Reponse>' object
    :rtype: requests.Response
    """