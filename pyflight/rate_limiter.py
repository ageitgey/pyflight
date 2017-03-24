"""
The Rate Limiter to limit the Requests being made to the API
"""
import asyncio

# By Default, set to the free quota
queries_per_day = 50


def set_queries_per_day(queries: int):
    """
    Set the maximum amount of Queries which should be sent out per day. 
    Omit this call if no rate limiting should be performed.
    """
    global queries_per_day
    queries_per_day = queries
    print(f'Set Rate Limit to {queries} Requests per Day.')


async def delay_request(loop):
    """
    Delay a new request by asynchronously sleeping.
    
    :param loop: The Loop from the requesting Unit 
    :return: Returns when done with Sleeping.
    """
    if queries_per_day == 0:
        # No Query set - no rate limiting
        pass
    else:
        # 24 / queries is the interval for requests in hours, * 60 * 60 is the interval in seconds
        await asyncio.sleep(24 / queries_per_day * 60 * 60, loop=loop)
