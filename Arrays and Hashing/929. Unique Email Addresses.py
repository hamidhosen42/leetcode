from pyparsing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        count = set()

        for e in emails:
            l,d = e.split('@')
            l = l.split('+')[0]
            l = l.replace('.','')
            count.add((l,d))
        return len(count)
        

object = Solution()
print(object.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))