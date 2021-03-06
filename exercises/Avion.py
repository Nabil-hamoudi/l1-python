route = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],

    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],

    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],

    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],

    ["ICN", "JFK"],
    ["JFK", "LGA"],

    ["EYW", "LHR"],

    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],

    ["SAN", "EYW"]
]

airports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
    "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"
    ]

startairport = "LGA"

possibleroute = []


for i in route:
    A = i.count(startairport)
    if A != 1:
        possibleroute.append(i)

print(possibleroute)
