class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        queue = deque(range(n))
        result =  [0] * n
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result
