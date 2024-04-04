class MixinRepr:

    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__.items()})."
