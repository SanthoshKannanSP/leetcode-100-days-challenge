class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visits = defaultdict(int)

        for count_pairs in cpdomains:
            count,domain = count_pairs.split()
            domain_visits[domain] += int(count)

            while "." in domain:
                domain = domain.split(".",1)[-1]
                domain_visits[domain] += int(count)

        return [str(domain_visits[domain])+" "+domain for domain in domain_visits]