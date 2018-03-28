from pyroutelib3 import Router # Import the router
router = Router("car") # Initialise it

start = router.data.findNode(4.36122,18.55496) # Find start and end nodes
end = router.data.findNode(4.1005,18.6584)

status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates

print(routeLatLons)
