from .crypt.passlib import PasslibPasswordCrypt


def provide_passlib_crypt():
    return PasslibPasswordCrypt()
