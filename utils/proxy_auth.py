
def make_proxy_auth(login, password, proxy) -> dict[str, str]:

    proxy = {
        'http': f"socks5://{login}:{password}@{proxy}",
        'https': f"socks5://{login}:{password}@{proxy}",
    }

    return proxy
