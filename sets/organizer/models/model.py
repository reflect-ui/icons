class SingleIconConfig:
    def __init__(self, default_size, variant, family, host, version=None, category=None, tags=[]):
        self.default_size = default_size
        self.variant = variant
        self.family = family
        self.host = host
        self.version = version
        self.category = category
        self.tags = tags


    def to_object(self):
        return {
            "default_size": self.default_size,
            "variant": self.variant,
            "family": self.family,
            "host": self.host,
            "version": self.version,
            "category": self.category,
            "tags": self.tags
        }