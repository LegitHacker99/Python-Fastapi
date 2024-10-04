from fastapi import Depends, HTTPException

'''
Dependencies can be added in 3 ways:
    -   we can add it as an arguments to the route handler
    -   we can add it as path configuration parameter, although in this method the attributes of the dependency can not be accessed in the route handler
    -   we can also add it as a global dependency in our fastapi app which adds it as a deps for every route declared using that router.
'''

# class user_dep:
#     def __init__(self, q: str | None = None):
#         self.q = q

# @Deps.get('/user_route', tags=["dep_injeksion"])
# def user_route_handler(user_deps = Depends(user_dep)):
#     if user_deps.q:
#         return "used dependency injection"
    
#     return "usused dependency injection"

def get_user_token(q: str):
    if q == 'KingSlayer':
        return "token check passed"
    
    raise HTTPException(status_code=401, detail='Unauthorised Access')
