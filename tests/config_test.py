"""API Config Testing"""
import os

from config import FactoryConfig


def test_development_config():
    """Test Development Configuration Defaults"""
    config = FactoryConfig.create_config('development')()
    assert config.DEBUG
    assert config.TESTING is False


def test_testing_config():
    """Test Testing Configuration Defaults"""
    config = FactoryConfig.create_config()()
    assert config.DEBUG
    assert config.TESTING


def test_production_config():
    """Test Production Configuration Defaults"""
    config = FactoryConfig.create_config('production')()
    assert config.DEBUG is False
    assert config.TESTING is False
