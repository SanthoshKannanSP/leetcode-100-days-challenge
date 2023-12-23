class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        sources = set()

        for source, destination in paths:
            cities.add(source)
            cities.add(destination)
            sources.add(source)

        return (cities-sources).pop()