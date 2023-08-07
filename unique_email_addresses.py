class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local,domain = email.split("@")
            local = local.replace(".","")
            plus = local.find("+")
            if plus>=0:
                local = local[:plus]
            unique.add(local+"@"+domain)

        return len(unique)