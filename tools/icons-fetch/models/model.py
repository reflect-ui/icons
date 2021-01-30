class SingleIconConfig:
    def __init__(self, default_size, variant, family, host):
        self.default_size = default_size
        self.variant = variant
        self.family = family
        self.host = host

    def to_object(self):
        return {
            "default_size": self.default_size,
            "variant": self.variant,
            "family": self.family,
            "host": self.host
        }