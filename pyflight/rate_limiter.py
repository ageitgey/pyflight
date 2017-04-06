"""
The Rate Limiter to limit the Requests being made to the API
"""
import asyncio
import time

# By Default, disable it
queries_per_day = 0


def set_queries_per_day(queries: int):
    """Set the maximum amount of Queries which should be sent out per day.
     
    Parameters
    ----------
        queries : int
            The Amount of Queries to be sent out per day
            
    """
    global queries_per_day
    queries_per_day = queries


async def delay_async(loop):
    """Delay a new request by asynchronously sleeping.
    
    Arguments
    
        loop : asyncio event loop
            The Loop from the requesting Unit             
    """
    if queries_per_day == 0:
        return
    # 24 / queries is the interval for requests in hours, * 60 * 60 is the interval in seconds
    await asyncio.sleep(24 / queries_per_day * 60 * 60, loop=loop)


def delay_sync():
    """Delay a synchronous request."""
    if queries_per_day == 0:
        return
    time.sleep(24 / queries_per_day * 60 * 60)
