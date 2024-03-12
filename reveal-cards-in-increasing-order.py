class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans = [deck[0]]
        
        for card in deck[1:]:
            ans.insert(0,ans.pop())
            ans.insert(0,card)

        return ans