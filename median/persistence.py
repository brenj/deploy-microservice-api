"""Manage persistence of integers for the median API."""

import redis

REDIS_APP = redis.StrictRedis()
