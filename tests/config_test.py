"""API Config Testing"""
import os
import unittest

from config import DevConfig, FactoryConfig, ProdConfig, TestConfig
from mock import patch


class TestConfigurationFactory(unittest.TestCase):
    def test_development_config(self):
        """Test Development Configuration Defaults"""
        config = FactoryConfig.create_config("development")()
        assert isinstance(config, DevConfig)


    def test_testing_config(self):
        """Test Testing Configuration Defaults"""
        config = FactoryConfig.create_config()()
        assert isinstance(config, TestConfig)


    def test_production_config(self):
        """Test Production Configuration Defaults"""
        config = FactoryConfig.create_config("production")()
        assert isinstance(config, ProdConfig)


    @patch('os.environ.get')
    def test_default_config(self, env_get):
        """Test Default Factory Configuration"""
        env_get.return_value = None
        config = FactoryConfig.create_config()()
        assert isinstance(config, DevConfig)
