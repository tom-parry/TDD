
# base class
class BaseConfig:
    TESTING = False

# class for development, testing off
class DevelopmentConfig(BaseConfig):
    pass

# class for testing, testing on
class TestingConfig(BaseConfig):
    TESTING = True

# class to use in production, testing off
class ProductionConfig(BaseConfig):
    pass
